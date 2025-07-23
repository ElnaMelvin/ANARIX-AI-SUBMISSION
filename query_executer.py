# ecom_agent/query_executor.py

import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join("db", "ecommerce.db")

def execute_sql_query(query: str) -> str:
    try:
        # Connect to the SQLite DB
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty:
            return "Query executed successfully, but no data was returned."
        else:
            return df.head(10).to_markdown(index=False)  # limit output for readability

    except Exception as e:
        return f"Error executing query: {e}"
