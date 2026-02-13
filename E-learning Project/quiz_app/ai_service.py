import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

#Loading the environment variables
load_dotenv()

#Configuring the Google API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz_json(topic, difficulty="beginner"):
    """
    Generates a quiz using Google Gemini 2.5 Flash.
    """
    try:
        # Initialize the Model
        # 'gemini-2.5-flash' is the fastest and cheapest (free-tier eligible) model
        # Enforcing 'application/json' so it NEVER returns conversational text
        model = genai.GenerativeModel(
            'gemini-2.5-flash',
            generation_config={"response_mime_type": "application/json"}
        )

        # Define the Prompt
        prompt = f"""
        You are a quiz generator. Create a {difficulty} level quiz about '{topic}' with 5 questions.
        
        Output valid JSON using this exact schema:
        {{
            "title": "A short, catchy title for the quiz",
            "questions": [
                {{
                    "id": 1,
                    "text": "The question text",
                    "options": ["Option A", "Option B", "Option C", "Option D"],
                    "correct_index": 0 
                }}
            ]
        }}
        """

        # Generate Content
        response = model.generate_content(prompt)
        
        # Parse and Return
        # 'response_mime_type', guarantees response.text to be JSON string
        quiz_data = json.loads(response.text)
        return quiz_data

    except Exception as e:
        print(f"Error generating quiz with Gemini: {e}")
        return None