import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()       # loads everything from .env file

# Wrapper for Groq API
client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url = "https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user", "content": "Suggest one thing to do in Bangalore."}
    ]
)

print("Response: ", response, "\n")
print(response.choices[0].message.content, "\n")


###################################

client_2 = OpenAI()    # uses OPENAI_API_KEY

response_2 = client_2.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user", "content": "Suggest one thing to do in Bangalore."}
    ]
)

print("Response 2 : ", response_2, "\n")
print(response_2.choices[0].message.content, "\n")

