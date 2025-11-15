🧠 Anni with AI – Local LLM-based RAG System
Private • Offline • OpenSearch-Powered • Streamlit UI • Docker Ready

Welcome to Anni with AI, a fully offline Retrieval-Augmented Generation (RAG) system built using Local LLMs (Ollama), OpenSearch, and Streamlit, with full Docker support for easy deployment.

This system helps you:

🔹 Upload & index PDF documents

🔹 Extract text (OCR optional)

🔹 Create high-quality embeddings

🔹 Store vectors + metadata inside OpenSearch

🔹 Query them with a RAG-powered chatbot

🔹 Completely offline — 100% private

🖼 System Architecture
<p align="center"> <img src="images/anni_rag_architecture.png" width="800"> </p>
⚡ Key Features
🔐 100% Local & Privacy-Friendly

Everything runs on your machine — no cloud requests, no external APIs.

🧠 Hybrid Search (BM25 + Semantic)

OpenSearch combines keyword ranking + vector similarity for precise retrieval.

🤖 Local LLM Chatbot (Ollama)

Powered by your chosen model:

llama3.2:1b (fastest)

llama3.2:3b

nomic-embed

or any model available in Ollama.

📄 Document Upload + Full RAG Pipeline

PDF → Text → Cleaning → Chunking → Embeddings → OpenSearch → Query → Answer

🎨 Beautiful Streamlit UI

Clean sidebar, logo, sliders, chatbot interface — optimized for readability.

🐳 Docker Support

Run the complete stack (Streamlit + OpenSearch + OCR + LLM) in containers.

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Anirudh-chaudhari/Anni-with-AI-Local-LLM-based-RAG-System-OpenSearch-Streamlit-Docker-.git
cd Anni-with-AI-Local-LLM-based-RAG-System-OpenSearch-Streamlit-Docker-

2️⃣ Create Conda Environment
conda create -n rag311 python=3.11 -y
conda activate rag311

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start OpenSearch (Recommended via Docker)
docker-compose up -d

5️⃣ Run the Local RAG App
streamlit run Welcome.py


➡ The app opens automatically at:
👉 http://localhost:8501

🔧 Configuration

All main settings are inside src/constants.py

Variable	Description
EMBEDDING_MODEL_PATH	SentenceTransformer embedding model
OLLAMA_MODEL_NAME	Local LLM for chat responses
OPENSEARCH_INDEX	Index name for vector DB
TEXT_CHUNK_SIZE	Chunk size for document splitting
EMBEDDING_DIM	Embedding vector dimension
OPENSEARCH_HOST	Host address (default: localhost)
OPENSEARCH_PORT	Port (default: 9200)
🧩 Tech Stack Overview
Component	Technology
LLM	Ollama (llama3.2:1b, etc.)
Vector DB	OpenSearch
Embeddings	Sentence Transformers
OCR	PyPDF2 / Tesseract
Frontend	Streamlit
Backend	Python
Deployment	Docker
✨ Optional Enhancements / Add-ons Included

📁 Delete documents from database

🧹 Auto-clean text before embedding

📌 Metadata-powered search

💬 Chat history memory inside prompt template

🚦 Temperature slider (controls creativity)

🔍 Adjustable retrieval window (top-k chunks)

🛠 Debug logs for ingestion + search pipeline

🖋 License
MIT License  
Copyright (c) 2024 Anirudh

⭐ Support

If you find this project helpful:

⭐ Star this repository
🍴 Fork it
🐛 Report issues
💬 Suggest new features

👨‍💻 Author
Anirudh Chaudhari

Creator of Anni with AI – Local RAG Chatbot

🔗 GitHub:
https://github.com/Anirudh-chaudhari
