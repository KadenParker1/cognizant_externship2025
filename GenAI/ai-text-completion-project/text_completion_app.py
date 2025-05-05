
# Set your huggingface API key here.

from huggingface_hub import InferenceClient

API_TOKEN = None
client = InferenceClient(provider="novita", api_key = API_TOKEN)
user_prompt = input("Please input your prompt: \n")
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ],
)
# context = input("Please share any valuable context: \n")

print(completion.choices[0].message.content)