from fastapi import FastAPI
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from pydantic import BaseModel

app = FastAPI()
embeddings = OpenAIEmbeddings(openai_api_key="your-api-key")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
llm = OpenAI(temperature=0)

class Query(BaseModel):
    text: str

@app.post("/ask")
def ask_question(query: Query):
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return {"answer": qa.run(query.text)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
