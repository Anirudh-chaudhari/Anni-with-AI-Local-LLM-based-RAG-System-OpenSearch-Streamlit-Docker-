import logging
import os
import time

import streamlit as st
from PyPDF2 import PdfReader

from src.constants import OPENSEARCH_INDEX, TEXT_CHUNK_SIZE
from src.embeddings import generate_embeddings, get_embedding_model
from src.ingestion import (
    bulk_index_documents,
    create_index,
    delete_documents_by_document_name,
)
from src.opensearch import get_opensearch_client
from src.utils import chunk_text, setup_logging

# Initialize logger
setup_logging()
logger = logging.getLogger(__name__)

# ---------------- BRANDING UPDATE ----------------
st.set_page_config(page_title="Anni with AI – Upload Documents", page_icon="📂")
# -------------------------------------------------

# Custom CSS (UNCHANGED)
st.markdown(
    """
    <style>
    body { background-color: #f0f8ff; color: #002B5B; }
    .sidebar .sidebar-content { background-color: #006d77; color: white; padding: 20px; border-right: 2px solid #003d5c; }
    .sidebar h2, .sidebar h4 { color: white; }
    .block-container { background-color: white; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); }
    .footer-text { font-size: 1.1rem; font-weight: bold; color: black; text-align: center; margin-top: 10px; }
    .stButton button { background-color: #118ab2; color: white; border-radius: 5px; padding: 10px 20px; font-size: 16px; }
    .stButton button:hover { background-color: #07a6c2; color: white; }
    .stButton.delete-button button { background-color: #e63946; color: white; font-size: 14px; }
    .stButton.delete-button button:hover { background-color: #ff4c4c; }
    h1, h2, h3, h4 { color: #006d77; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- BRANDING UPDATE ----------------
# Replace old logo with your logo
logo_path = r"C:\Users\asus\build_your_local_RAG_system\images\Chatbot.png"
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=280)
else:
    st.sidebar.markdown("### Logo Placeholder")
    logger.warning("Logo not found – showing placeholder.")

# Sidebar header
st.sidebar.markdown(
    "<h2 style='text-align: center;'>Anni with AI</h2>",
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    "<h4 style='text-align: center;'>RAG Document Assistant</h4>",
    unsafe_allow_html=True,
)

# Footer
st.sidebar.markdown(
    """
    <div class="footer-text">
        © 2025 Anni with AI – RAG Chatbot
    </div>
    """,
    unsafe_allow_html=True,
)
# -------------------------------------------------


def render_upload_page() -> None:
    st.title("Upload Documents")
    
    model_loading_placeholder = st.empty()

    if "embedding_models_loaded" not in st.session_state:
        with model_loading_placeholder:
            with st.spinner("Loading models for document processing..."):
                get_embedding_model()
                st.session_state["embedding_models_loaded"] = True
        logger.info("Embedding models loaded.")
        model_loading_placeholder.empty()

    UPLOAD_DIR = "uploaded_files"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    with st.spinner("Connecting to OpenSearch..."):
        client = get_opensearch_client()
    index_name = OPENSEARCH_INDEX

    create_index(client)

    st.session_state["documents"] = []

    query = {
        "size": 0,
        "aggs": {"unique_docs": {"terms": {"field": "document_name", "size": 10000}}},
    }
    response = client.search(index=index_name, body=query)
    buckets = response["aggregations"]["unique_docs"]["buckets"]
    document_names = [bucket["key"] for bucket in buckets]
    logger.info("Retrieved document names from OpenSearch.")

    for document_name in document_names:
        file_path = os.path.join(UPLOAD_DIR, document_name)
        if os.path.exists(file_path):
            reader = PdfReader(file_path)
            text = "".join([page.extract_text() for page in reader.pages])
            st.session_state["documents"].append(
                {"filename": document_name, "content": text, "file_path": file_path}
            )
        else:
            st.session_state["documents"].append(
                {"filename": document_name, "content": "", "file_path": None}
            )
            logger.warning(f"File '{document_name}' does not exist locally.")

    if "deleted_file" in st.session_state:
        st.success(
            f"The file '{st.session_state['deleted_file']}' was successfully deleted."
        )
        del st.session_state["deleted_file"]

    uploaded_files = st.file_uploader(
        "Upload PDF documents", type="pdf", accept_multiple_files=True
    )

    if uploaded_files:
        with st.spinner("Uploading and processing documents. Please wait..."):
            for uploaded_file in uploaded_files:
                if uploaded_file.name in document_names:
                    st.warning(
                        f"The file '{uploaded_file.name}' already exists in the index."
                    )
                    continue

                file_path = save_uploaded_file(uploaded_file)
                reader = PdfReader(file_path)
                text = "".join([page.extract_text() for page in reader.pages])
                chunks = chunk_text(text, chunk_size=TEXT_CHUNK_SIZE, overlap=100)
                embeddings = generate_embeddings(chunks)

                documents_to_index = [
                    {
                        "doc_id": f"{uploaded_file.name}_{i}",
                        "text": chunk,
                        "embedding": embedding,
                        "document_name": uploaded_file.name,
                    }
                    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings))
                ]
                bulk_index_documents(documents_to_index)
                st.session_state["documents"].append(
                    {
                        "filename": uploaded_file.name,
                        "content": text,
                        "file_path": file_path,
                    }
                )
                document_names.append(uploaded_file.name)
                logger.info(f"File '{uploaded_file.name}' uploaded and indexed.")

        st.success("Files uploaded and indexed successfully!")

    if st.session_state["documents"]:
        st.markdown("### Uploaded Documents")
        with st.expander("Manage Uploaded Documents", expanded=True):
            for idx, doc in enumerate(st.session_state["documents"], 1):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(
                        f"{idx}. {doc['filename']} - {len(doc['content'])} characters extracted"
                    )
                with col2:
                    delete_button = st.button(
                        "Delete",
                        key=f"delete_{doc['filename']}_{idx}",
                        help=f"Delete {doc['filename']}",
                    )
                    if delete_button:
                        if doc["file_path"] and os.path.exists(doc["file_path"]):
                            try:
                                os.remove(doc["file_path"])
                                logger.info(
                                    f"Deleted file '{doc['filename']}' from filesystem."
                                )
                            except FileNotFoundError:
                                st.error(
                                    f"File '{doc['filename']}' not found in filesystem."
                                )
                        delete_documents_by_document_name(doc["filename"])
                        st.session_state["documents"].pop(idx - 1)
                        st.session_state["deleted_file"] = doc["filename"]
                        time.sleep(0.5)
                        st.rerun()


def save_uploaded_file(uploaded_file) -> str:
    UPLOAD_DIR = "uploaded_files"
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    logger.info(f"File '{uploaded_file.name}' saved to '{file_path}'.")
    return file_path


if __name__ == "__main__":
    if "documents" not in st.session_state:
        st.session_state["documents"] = []
    render_upload_page()
