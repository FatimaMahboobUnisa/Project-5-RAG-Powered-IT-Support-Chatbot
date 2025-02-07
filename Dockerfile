FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY rag_api.py .
COPY chroma_db /app/chroma_db  # Preloaded ChromaDB data

CMD ["uvicorn", "rag_api:app", "--host", "0.0.0.0", "--port", "8000"]
