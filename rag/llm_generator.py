import openai

openai.api_key = "YOUR_API_KEY_HERE"

def generate_explanation(query, recommendations):
    assessment_list = "\n".join(
        [f"- {row}" for row in recommendations]
    )

    prompt = f"""
User query:
{query}

Recommended SHL assessments:
{assessment_list}

Explain briefly why these assessments are suitable.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content
