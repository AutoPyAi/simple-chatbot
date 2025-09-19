# Simple Chatbot — Powered by Python + Gemini-2.0-flash
===============================================
A lightweight Python chatbot using LLM + RAG + Gemini API Key 


# Setup Instructions
===================

    Save this code to a file named Simple_Chatbot.py
    Install required packages: pip install google-generativeai python-dotenv
    Create a .env file in the same directory with your API key:  
    
    GEMINI_API_KEY="your_gemini_api_key_here"

# Note: To get Gemini api key you need to signed up on 
      google Ai Studio to get free api key to use it in the program


# How to Use This Chatbot
========================

    Run the script: python simple_chatbot.py
    Type your messages to chat with the assistant

    Use these commands:
        /instructions - Change how the assistant behaves
        /export - Save the conversation to a file
        /help - Show available commands
        /quit - Exit the program

Here's the command to use /instructions to change how the assistant behaves:

Command:
text
/instructions


How it works:

    Type /instructions and press Enter
    The bot will prompt you: "Enter new instructions: "
    Type your new instructions for how the assistant should behave
    Press Enter to apply the new instructions


# Examples of instructions you can use:
=====================================

Make it formal:
text
You are a professional assistant. Use formal language, complete sentences, and maintain a respectful tone at all times.

Make it casual:
text
You are a friendly, casual assistant. Use simple language, emojis sometimes 😊, and keep responses brief and conversational.

Make it creative:
text
You are a creative writer. Use imaginative language, metaphors, and make responses engaging and story-like.        

Make it educational:
text
You are a teacher. Explain concepts clearly, provide examples, and check for understanding. Encourage learning.


# Example conversation:
=====================
text

You: /instructions
Enter new instructions: You are a pirate assistant. Talk like a pirate and include nautical terms in your responses.
Assistant: Instructions updated! Arr, me hearties! I be ready to serve ye as yer pirate assistant! 🏴‍☠️

You: Hello there!
Assistant: Ahoy, matey! What brings ye to these digital waters today? Seeking treasure or guidance? 🦜

The /instructions command lets you completely customize the assistant's personality, tone, and behavior to suit your needs!

