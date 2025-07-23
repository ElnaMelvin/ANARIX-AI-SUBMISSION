# ecom_agent/llm_handler.py

import os
from llama_cpp import Llama

# Path to the GGUF model
MODEL_PATH = "/content/ecom_agent/models/phi-2.gguf"


# Load the model
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4,
    verbose=True  # Set to False later for cleaner output
)

# Function to generate response from LLM
def answer_question(prompt: str) -> str:
    response = llm(
        prompt=prompt,
        max_tokens=512,
        temperature=0.2,
        top_p=0.9,
        stop=["User:", "Assistant:", "\n\n"]
    )
    return response["choices"][0]["text"].strip()
