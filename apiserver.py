from fastapi import FastAPI
from retriever import get_cdp_answer

app = FastAPI()

@app.get("/ask")
async def ask(question: str):
    answer = get_cdp_answer(question)
    return {"question": question, "answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
