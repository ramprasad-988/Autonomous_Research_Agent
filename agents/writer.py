from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

print("API KEY:", os.getenv("GROQ_API_KEY")[:15])

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_report(topic, content):

    prompt = f"""
You are an expert research analyst.

Create a PROFESSIONAL research report.

Topic:
{topic}

Research Data:
{content}

Requirements:

1. Academic writing style
2. Clear headings
3. Detailed explanations
4. Bullet points where needed
5. Professional language
6. Minimum 1500 words

Format exactly as:

# Executive Summary

# Introduction

# Background

# Key Findings

# Benefits

# Challenges

# Real World Applications

# Future Scope

# Recommendations

# Conclusion

# References

Include detailed content under every section.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=4000
    )

    return response.choices[0].message.content