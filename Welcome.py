import logging
import os

import streamlit as st

from src.utils import setup_logging

# Initialize logger
setup_logging()  # Set up logging configuration
logger = logging.getLogger(__name__)

# Set page config with title, icon, and layout
st.set_page_config(
    page_title="Anni with AI – RAG Chatbot", page_icon="🤖"
)


# Custom CSS to style the page and sidebar (UNCHANGED)
def apply_custom_css() -> None:
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f8ff;
            color: #002B5B;
        }
        .sidebar .sidebar-content {
            background-color: #006d77;
            color: white;
            padding: 20px;
            border-right: 2px solid #003d5c;
        }
        .sidebar h2, .sidebar h4 {
            color: white;
        }
        .block-container {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .stColumn {
            text-align: center;
        }
        .footer-text {
            font-size: 1.1rem;
            font-weight: bold;
            color: black;
            text-align: center;
            margin-top: 10px;
        }
        .stButton button {
            background-color: #118ab2;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
        }
        .stButton button:hover {
            background-color: #07a6c2;
            color: white;
        }
        h1, h2, h3, h4 {
            color: #006d77;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    logger.info("Applied custom CSS styling.")


# Function to display logo (BRANDING UPDATED + CENTERED)
def display_logo(logo_path: str) -> None:
    if os.path.exists(logo_path):
        st.sidebar.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-bottom: 15px;">
                <img src="{logo_path}" width="220">
            </div>
            """,
            unsafe_allow_html=True,
        )
        logger.info("Logo displayed.")
    else:
        st.sidebar.markdown("### Logo Placeholder")
        logger.warning("Logo not found, displaying placeholder.")


# Function to display main content (BRANDING UPDATED ONLY)
def display_main_content() -> None:
    st.title("Anni with AI – Personal Document Assistant 📄🤖")
    st.markdown(
        """
        Welcome to **Anni with AI – Your Local RAG Chatbot** 👋
                
        This app allows you to interact with your own documents using a **Local LLM + Hybrid RAG System**, completely offline and privacy-friendly.
        
        **Features:**
        - **Chatbot:** Talk to your documents using the integrated LLM.
        - **Document Upload:** Upload PDFs and retrieve high-quality answers powered by OpenSearch + Embeddings.

        **Choose a page from the sidebar to begin.**
        """
    )
    logger.info("Displayed main welcome content.")


# Function to display sidebar content (BRANDING ONLY)
def display_sidebar_content() -> None:
    st.sidebar.markdown(
        "<h2 style='text-align: center;'>Anni with AI</h2>", unsafe_allow_html=True
    )
    st.sidebar.markdown(
        "<h4 style='text-align: center;'>RAG Conversational Platform</h4>",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        """
        <div class="footer-text">
            © 2025 Anni with AI – RAG Chatbot
        </div>
        """,
        unsafe_allow_html=True,
    )
    logger.info("Displayed sidebar content.")


# Main execution
if __name__ == "__main__":
    apply_custom_css()
    display_logo("images/anni_logo.png")   # <-- Updated with your logo
    display_sidebar_content()
    display_main_content()
