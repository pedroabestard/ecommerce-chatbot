from groq import Groq
import os

groq_smalltalk_client = Groq()

def talk_response(query):
    prompt = f'''You are an smart and cool chatbot designed to help users interact with flipkart webpage, answer questions related to products, FAQs and have friendly conversations.
    
    QUESTION: {query}'''

    completion = groq_smalltalk_client.chat.completions.create(
        model=os.environ['GROQ_MODEL'],
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None
    )

    model_response = ""
    for chunk in completion:
        model_response += chunk.choices[0].delta.content or ""
    return model_response