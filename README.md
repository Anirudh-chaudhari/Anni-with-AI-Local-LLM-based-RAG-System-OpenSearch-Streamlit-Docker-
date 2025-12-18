🧠 Anni with AI
Local LLM-Based Retrieval-Augmented Generation (RAG) System

Private • Offline • OpenSearch-Powered • Streamlit UI • Docker-Ready

📌 Abstract

Anni with AI is a fully offline, privacy-preserving Retrieval-Augmented Generation (RAG) system that enables intelligent question answering over user-provided documents using local Large Language Models (LLMs).
The system integrates hybrid document retrieval (BM25 + semantic vector search) using OpenSearch with local LLM inference via Ollama, eliminating dependency on cloud APIs.

This project is designed for secure document intelligence, making it suitable for enterprise, academic, and confidential data environments.

🔑 Keywords

Retrieval-Augmented Generation (RAG), Local LLMs, OpenSearch, Semantic Search, BM25, Offline AI, Privacy-Preserving AI, Document Intelligence

🚀 Overview

Modern AI assistants often rely on cloud-hosted APIs, which raises concerns related to:

Data privacy

Regulatory compliance

Internet dependency

Cost scalability

Anni with AI addresses these challenges by providing a completely local RAG pipeline, ensuring that all data, embeddings, and inference remain on the user’s machine.

🎯 Objectives

Build a fully offline RAG system

Enable hybrid document retrieval

Integrate local LLM-based answer generation

Maintain strict data privacy

Provide a simple and intuitive UI

Support containerized deployment

🧩 System Architecture
PDF Documents
   ↓
Text Extraction (OCR optional)
   ↓
Text Cleaning & Normalization
   ↓
Chunking
   ↓
Embedding Generation
   ↓
OpenSearch (BM25 + Vector Index)
   ↓
Relevant Context Retrieval
   ↓
Local LLM (Ollama)
   ↓
Final Answer Generation


This architecture combines lexical relevance with semantic understanding, resulting in accurate and context-aware responses.

🛠 Methodology
1. Document Ingestion

Upload PDF documents

Extract text using PyPDF2

OCR support via Tesseract for scanned PDFs

2. Text Processing

Noise removal and normalization

Chunking into fixed-size segments for efficient embedding

3. Embedding Generation

Sentence Transformer models generate dense vector embeddings

Each text chunk is embedded independently

4. Storage & Retrieval

OpenSearch stores:

Vector embeddings

Document metadata

Hybrid retrieval combines:

BM25 keyword search

Vector similarity search

5. Answer Generation

Retrieved context is injected into the prompt

Local LLMs generate responses using Ollama

Adjustable temperature and Top-K retrieval

⚡ Key Features

✅ Fully offline execution

🔐 Privacy-first design

🧠 Hybrid semantic + keyword search

🤖 Local LLM-powered chatbot

📄 End-to-end RAG pipeline

🎨 Modern Streamlit UI

🐳 Docker & Docker Compose support

🔧 Configurable retrieval parameters

🧩 Tech Stack
Component	Technology
LLM	Ollama
Vector Database	OpenSearch
Embeddings	Sentence Transformers
OCR	PyPDF2, Tesseract
Frontend	Streamlit
Backend	Python
Deployment	Docker
🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Anirudh-chaudhari/Anni-with-AI-Local-LLM-based-RAG-System-OpenSearch-Streamlit-Docker-.git
cd Anni-with-AI-Local-LLM-based-RAG-System-OpenSearch-Streamlit-Docker-

2️⃣ Create Conda Environment
conda create -n rag311 python=3.11 -y
conda activate rag311

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start OpenSearch (Recommended)
docker-compose up -d

5️⃣ Run the Application
streamlit run Welcome.py

🌐 Access the App
http://localhost:8501

🔧 Configuration

All configuration parameters are located in:

src/constants.py

Variable	Description
EMBEDDING_MODEL_PATH	SentenceTransformer model path
OLLAMA_MODEL_NAME	Local LLM name
OPENSEARCH_INDEX	Vector index name
TEXT_CHUNK_SIZE	Document chunk size
EMBEDDING_DIM	Embedding vector dimension
OPENSEARCH_HOST	Default: localhost
OPENSEARCH_PORT	Default: 9200
🧪 Experimental Setup

Python: 3.11

LLMs: llama3.2 (1B / 3B variants)

Embedding Model: nomic-embed-text

Deployment: Local machine / Docker

📊 Results & Observations

High-quality, context-aware responses

Improved retrieval relevance due to hybrid search

Zero dependency on external APIs

Suitable for confidential and offline environments

🧠 Applications

Enterprise document intelligence

Academic research assistants

Legal & medical document analysis

Secure internal knowledge bases

Offline AI chat systems

⚠ Limitations

Performance depends on local hardware

Larger LLMs require sufficient RAM

OCR accuracy depends on document quality

🔮 Future Enhancements

Multi-user authentication

Role-based access control

Streaming responses

Knowledge graph integration

Multi-modal document support

Domain-specific LLM fine-tuning

🖋 License

MIT License
© 2024 Anirudh Chaudhari

⭐ Support

If you find this project useful:

🌟 Star the repository

🍴 Fork the project

🐛 Report issues

💬 Suggest features

👨‍💻 Author

Anirudh Chaudhari
AI/ML Engineer | RAG Systems | Local LLMs | Computer Vision

🔗 GitHub:
https://github.com/Anirudh-chaudhari
