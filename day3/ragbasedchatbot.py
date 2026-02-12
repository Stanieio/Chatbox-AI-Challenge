import langchain
from openai import OpenAI
client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key="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")
document=[
"india has income tax laws.",
"tax is calculation based income tax slabs.",
"gst is only 18 for many goods ",
]
questions="EXPLAIN TAX CALCULATION..?"
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        
            {"role": "system","content": "answer only from the given document"},
            {"role": "user","content": f"Document: {document}\n\nQuestion: {questions}"}
        
    ],
)
print(response.choices[0].message.content)
