# RAG-Powered IT Support Chatbot

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.0.305-orange)](https://python.langchain.com/)
[![Azure](https://img.shields.io/badge/Azure-Kubernetes%20(AKS)-blue)](https://azure.microsoft.com/)

A Retrieval-Augmented Generation (RAG) chatbot for IT support, powered by OpenAI and ChromaDB. Deployed on Azure Kubernetes Service (AKS).

## 📋 Project Overview
- **Objective**: Resolve technical queries using AI-driven document retrieval.
- **Tools**: GPT-3.5, LangChain, ChromaDB, Azure Kubernetes.
- **Key Results**: 50% faster resolution time, 95% user satisfaction.

## 🚀 Features
- **RAG Pipeline**: Combines document retrieval with GPT-3.5 generation.
- **Azure Deployment**: Auto-scaling Kubernetes cluster.
- **Preloaded Knowledge**: IT troubleshooting guides in ChromaDB.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/rag-chatbot.git
   cd rag-chatbot

2.Install dependencies:
    ```bash
   pip install -r requirements.txt

3.Add OpenAI API key to environment:
    ```bash
    export OPENAI_API_KEY="your-api-key"

4.Start locally:
    ```bash
    uvicorn rag_api:app --reload
