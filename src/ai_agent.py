import os
from openai import OpenAI

# Tomamos la API key del entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai_about_dataset(context, question):
    """
    Envía al modelo la pregunta y el contexto del dataset para generar insights.
    """

    prompt = f"""
You are a Data Analyst AI.
Analyze the dataset described below and answer the user's question with actionable insights.

Dataset context:
{context}

User question:
{question}

Provide:
- Short analytical insights
- Suggested visualizations if applicable
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error calling OpenAI: {e}"