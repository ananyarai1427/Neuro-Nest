# chatbot.py (Updated with Gemini API)

import google.generativeai as genai
from datetime import datetime
from pymongo import MongoClient
import os # Used to get API key from environment variables

# --- Configuration ---

# It's highly recommended to set your API key as an environment variable
# for better security, instead of pasting it directly in the code.
# Example: os.environ.get("GEMINI_API_KEY")
# For now, you can paste it directly to get started.
try:
    genai.configure(api_key="AIzaSyBhSQrYZL5ipQkw08qk1EWQx86_cY_KWT8") 
except Exception as e:
    print(f"Error configuring Gemini API: {e}")

# MongoDB Connection
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["neuronest"]
    chat_collection = db["chat_history"]
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")


# --- Main Chatbot Logic ---

# In chatbot.py

# ... (keep all your other functions like get_response, etc.)

def log_chat(user_msg, bot_response, user_id):
    """Logs the conversation to the database with a user ID."""
    try:
        # Note the new 'user_id' field being saved
        chat_collection.insert_one({
            "user_id": user_id,
            "user_msg": user_msg,
            "bot_response": bot_response,
            "timestamp": datetime.now()
        })
    except Exception as e:
        print(f"Error logging chat to MongoDB: {e}")

# In chatbot.py

def get_response(user_input, personality="calm therapist", user_id=None):
    """
    Gets a response from the Gemini API and logs it with the user's ID.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    You are a chatbot named NeuroNest. Your current personality is a '{personality}'.
    Keep your responses concise and conversational (2-3 sentences).
    
    User's message: "{user_input}"
    """
    
    try:
        api_response = model.generate_content(prompt)
        bot_response = api_response.text
        
        # Now, call log_chat with the user_id that was passed in
        if user_id:
            log_chat(user_input, bot_response, user_id)
        
        return bot_response

    except Exception as e:
        print(f"!!! GEMINI API ERROR: {e}")
        error_message = "I'm sorry, I'm having trouble connecting to my brain right now. Please try again in a moment."
        return error_message
    
    try:
        # Call the API to generate content
        api_response = model.generate_content(prompt)
        bot_response = api_response.text
        
        # Log the successful conversation to your database
        log_chat(user_input, bot_response)
        
        return bot_response

    except Exception as e:
        # Handle potential API errors gracefully
        print(f"!!! GEMINI API ERROR: {e}")
        error_message = "I'm sorry, I'm having trouble connecting to my brain right now. Please try again in a moment."
        return error_message