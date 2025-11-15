🧠 Anni with AI – Local LLM-based RAG System
Private • Offline • OpenSearch-Powered • Streamlit UI • Docker Ready
<div align="center"> <img src="images/anni_banner_dark.png" width="750"/> </div>
🚀 Overview

Anni with AI is a fully offline Retrieval-Augmented Generation (RAG) system using:

🧠 Local LLMs via Ollama

🔍 OpenSearch for vector + BM25 hybrid search

🎨 Streamlit for a clean chatbot interface

🐳 Full Docker support for deployment

This system allows you to:

✔ Upload and index your PDF documents
✔ Extract and clean text (OCR optional)
✔ Generate high-quality embeddings
✔ Store vectors + metadata inside OpenSearch
✔ Query documents using a RAG-powered chatbot
✔ Keep everything offline — 100% private

🖼 User Interface
<div align="center"> <img src="images/ui_preview.png" width="850"/> </div>
🧩 System Architecture
<div align="center"> <img src="images/anni_rag_architecture.png" width="900"/> </div>
⚡ Key Features
🔐 100% Local & Privacy-Friendly

Everything runs on your device — no external APIs, no cloud involvement.

🧠 Hybrid Search (BM25 + Semantic)

Powered by OpenSearch for:

keyword matching (BM25)

vector similarity search

🤖 Local LLM Chatbot (Ollama)

Supports any local model:

llama3.2:1b (fastest)

llama3.2:3b

nomic-embed-text

or any model available via Ollama

📄 Full RAG Pipeline

PDF → OCR → Clean Text → Chunking → Embeddings → OpenSearch → Answer

🎨 Modern Streamlit UI

Beautiful sidebar

Logo branding

Temperature slider

RAG enable/disable toggle

Chat history memory

🐳 Docker Support

Spin up the entire stack using:

docker-compose up -d

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


🌐 App will open automatically at:
👉 http://localhost:8501

🔧 Configuration

All settings are inside:

src/constants.py

Variable	Description
EMBEDDING_MODEL_PATH	Path to SentenceTransformer model
OLLAMA_MODEL_NAME	Local LLM name (e.g., llama3.2:1b)
OPENSEARCH_INDEX	Vector DB index name
TEXT_CHUNK_SIZE	Chunk size for splitting documents
EMBEDDING_DIM	Dimension of embedding vectors
OPENSEARCH_HOST	Default: localhost
OPENSEARCH_PORT	Default: 9200
🧩 Tech Stack Overview
Component	Technology
LLM	Ollama
Vector DB	OpenSearch
Embeddings	Sentence Transformers
OCR	PyPDF2 / Tesseract
Frontend	Streamlit
Backend	Python
Deployment	Docker
✨ Optional Enhancements (Included)

✔ Delete documents from database
✔ Metadata-powered search
✔ Auto-clean text
✔ Chat history in prompts
✔ Temperature control slider
✔ Adjustable Top-K retrieval
✔ Debug logs for ingestion + search

🖋 License
MIT License
Copyright (c) 2024 Anirudh

⭐ Support

If this project helps you:

🌟 Star the repo
🍴 Fork it
🐛 Report an issue
💬 Request new features

👨‍💻 Author

Anirudh Chaudhari
Creator of Anni with AI – Local LLM-based RAG Chatbot

🔗 GitHub:
https://github.com/Anirudh-chaudhari
