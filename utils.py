# ecom_agent/utils.py

import sqlite3
import os

# Path to your database
DB_PATH = os.path.join("db", "ecommerce.db")

def get_db_schema() -> str:
    """
    Extracts all table names and their columns from the SQLite database.
    Returns a nicely formatted schema string.
    """
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found at {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema_str = ""
    for table_tuple in tables:
        table_name = table_tuple[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        schema_str += f"Table: {table_name}\nColumns: {', '.join(column_names)}\n\n"

    conn.close()
    return schema_str.strip()

def build_prompt(user_question: str) -> str:
    """
    Constructs a prompt for the LLM using the DB schema and user question.
    Returns a full prompt string ready for LLM input.
    """
    schema = get_db_schema()
    prompt = f"""
You are a helpful assistant that writes SQL queries based on the database schema and a user question.

Database Schema:
{schema}

User Question:
\"\"\"{user_question}\"\"\"

Write a syntactically correct SQLite SQL query to answer this question.
Only output the SQL query, nothing else.
""".strip()

    return prompt
