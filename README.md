🧠 Anni with AI – Local LLM-based RAG System
Private · Offline · OpenSearch-Powered · Streamlit UI · Docker Ready
Local · Private · Intelligent
<p align="center"> <img src="images/anni_banner_dark.png" width="80%"> </p>

Welcome to Anni with AI, a fully offline Retrieval-Augmented Generation (RAG) system built using Local LLMs (Ollama), OpenSearch, and Streamlit, with full Docker support for seamless deployment.

This system allows you to:

🔹 Upload & index PDF documents
🔹 Extract text (OCR optional)
🔹 Create high-quality embeddings
🔹 Store vectors + metadata in OpenSearch
🔹 Query with a RAG-powered AI Chatbot
🔹 Fully offline — 100% privacy preserved

🖼 System Architecture
<p align="center"> <img src="images/anni_rag_architecture_dark.png" width="85%"> </p>
⚡ Key Features
🔐 100% Local & Privacy-Friendly

Everything runs on your machine — no cloud, no external API calls.

🧠 Hybrid Search (BM25 + Semantic)

OpenSearch combines keyword scoring + vector similarity.

🤖 Local LLM Chatbot (Ollama)

Supports any Ollama model:

llama3.2:1b (fastest)

llama3.2:3b

nomic-embed

Any model available in Ollama

📄 Full RAG Pipeline

PDF → Text → Cleaning → Chunking → Embeddings → OpenSearch → Retrieval → LLM Answer

🎨 Beautiful Streamlit UI

Custom branded theme, clean sidebar, sliders, chat view.

🐳 Docker Support

Run the entire stack reproducibly inside containers.

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Anirudh-chaudhari/Anni-with-AI-Local-LLM-based-RAG-System-OpenSearch-Streamlit-Docker-.git
cd Anni-with-AI-Local-LLM-based-RAG-System-OpenSearch-Streamlit-Docker-

2️⃣ Create Conda Environment
conda create -n rag311 python=3.11 -y
conda activate rag311

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start OpenSearch (Recommended: Docker)
docker-compose up -d

5️⃣ Run the Streamlit App
streamlit run Welcome.py


➡ Visit: http://localhost:8501

🔧 Configuration

Edit file: src/constants.py

Variable	Description
EMBEDDING_MODEL_PATH	SentenceTransformer model
OLLAMA_MODEL_NAME	Local LLM
OPENSEARCH_INDEX	Vector index name
TEXT_CHUNK_SIZE	Chunk size for splitting
EMBEDDING_DIM	Embedding dimension
OPENSEARCH_HOST	Host (default: localhost)
OPENSEARCH_PORT	Port (default: 9200)
🧩 Tech Stack Overview
Component	Technology
LLM	Ollama (llama3.2:1b, etc.)
Vector DB	OpenSearch
Embeddings	Sentence Transformers
OCR	PyPDF2 / Tesseract
UI	Streamlit
Backend	Python
Deployment	Docker
✨ Extra Enhancements Included

✔ Delete documents from index
✔ Auto-clean text
✔ Metadata-based search
✔ Chat history memory
✔ Temperature control
✔ Adjustable Top-K retrieval
✔ Debug logs for ingestion & search

🖋 License

MIT License
Copyright © 2024 Anirudh

⭐ Support

If this project helped you:

⭐ Star the repo
🍴 Fork it
🐛 Report bugs
💡 Suggest improvements

👨‍💻 Author

Anirudh Chaudhari
Creator of Anni with AI – Local RAG Chatbot
🔗 GitHub: https://github.com/Anirudh-chaudhari
