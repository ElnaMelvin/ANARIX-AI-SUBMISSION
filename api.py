# ecom_agent/api.py

from fastapi import FastAPI, Query
from pydantic import BaseModel
from llm_handler import generate_sql_from_question
from query_executor import execute_query
import uvicorn

app = FastAPI(title="E-commerce Agent API")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QuestionRequest):
    user_question = request.question

    # Step 1: Generate SQL from the LLM
    generated_sql = generate_sql_from_question(user_question)

    # Step 2: Execute SQL on the database
    result = execute_query(generated_sql)

    return {
        "question": user_question,
        "generated_sql": generated_sql,
        "result": result
    }

# Optional: Run the API directly using `python api.py`
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
