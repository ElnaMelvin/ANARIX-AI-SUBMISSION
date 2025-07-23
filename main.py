# ecom_agent/main.py

from llm_handler import generate_sql_from_question
from query_executor import execute_query
import sys

def run_agent(user_question: str):
    print(f"\n🔍 Question: {user_question}")

    # Step 1: LLM generates SQL query
    generated_sql = generate_sql_from_question(user_question)
    print(f"\n🧠 Generated SQL:\n{generated_sql}")

    # Step 2: Execute SQL query
    result = execute_query(generated_sql)
    print(f"\n📊 Result:\n{result}")

if __name__ == "__main__":
    # You can change this question or take input from CLI
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("Ask a question about your e-commerce data: ")

    run_agent(question)
