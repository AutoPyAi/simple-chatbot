
"""
This simple_chatbot.py chatbot is same just like Api_chatgpt_bot.py 
except that This is created using simple methods without using class

While APi_chatgpt_bot.py is created using simple using class

"""


import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini with your API key
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("Error: Please set your GEMINI_API_KEY in the .env file")
    exit()

genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Start a new chat session
chat_session = model.start_chat(history=[])

# Store conversation history
conversation_history = []

# Default instructions for the assistant
assistant_instructions = "You are a helpful assistant."

# Function to update assistant instructions
def update_instructions(new_instructions):
    global assistant_instructions, chat_session, model
    
    assistant_instructions = new_instructions
    print(f"Instructions updated to: {assistant_instructions}")
    
    # Restart chat with new instructions
    chat_session = model.start_chat(history=[])
    conversation_history.clear()
    
    # Add instructions as first message
    add_to_history("user", assistant_instructions)
    
    try:
        response = chat_session.send_message(assistant_instructions)
        add_to_history("model", response.text)
        print(f"Assistant: {response.text}")
    except Exception as e:
        print(f"Error setting instructions: {e}")

# Function to add messages to history
def add_to_history(role, message):
    conversation_history.append({
        "role": role,
        "message": message,
        "timestamp": datetime.now().isoformat()
    })

# Function to export conversation
def export_conversation(format_type="text"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if format_type.lower() == "json":
        # Save as JSON
        filename = f"chat_export_{timestamp}.json"
        export_data = {
            "exported_at": datetime.now().isoformat(),
            "instructions": assistant_instructions,
            "messages": conversation_history
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"Conversation saved as JSON: {filename}")
    
    else:
        # Save as text
        filename = f"chat_export_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Chat Export - {datetime.now()}\n")
            f.write(f"Assistant Instructions: {assistant_instructions}\n")
            f.write("=" * 50 + "\n\n")
            
            for message in conversation_history:
                if message["role"] == "user":
                    f.write(f"You: {message['message']}\n\n")
                elif message["role"] == "model":
                    f.write(f"Assistant: {message['message']}\n\n")
        
        print(f"Conversation saved as text: {filename}")

# Function to display help
def show_help():
    print("\n=== Available Commands ===")
    print("Type your message to chat with the assistant")
    print("/instructions - Change assistant behavior")
    print("/export - Save conversation to file")
    print("/help - Show this help message")
    print("/quit - Exit the program")
    print("==========================\n")

# Main chat function
def start_chat():
    print("=== Simple Gemini Chat Bot ===")
    print(f"Current instructions: {assistant_instructions}")
    print("Type /help for available commands")
    print("=" * 30)
    
    # Start with instructions
    add_to_history("user", assistant_instructions)
    
    try:
        response = chat_session.send_message(assistant_instructions)
        add_to_history("model", response.text)
        print(f"Assistant: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for commands
            if user_input.lower() == '/quit':
                print("Goodbye!")
                break
            
            elif user_input.lower() == '/export':
                format_choice = input("Export as (text/json) [text]: ").strip().lower()
                if format_choice == 'json':
                    export_conversation("json")
                else:
                    export_conversation("text")
                continue
            
            elif user_input.lower() == '/instructions':
                new_instructions = input("Enter new instructions: ").strip()
                if new_instructions:
                    update_instructions(new_instructions)
                continue
            
            elif user_input.lower() == '/help':
                show_help()
                continue
            
            # Regular message - send to Gemini
            if user_input:
                add_to_history("user", user_input)
                
                # Get response from Gemini
                response = chat_session.send_message(user_input)
                
                # Add to history and print
                add_to_history("model", response.text)
                print(f"\nAssistant: {response.text}")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

# Start the chat
if __name__ == "__main__":
    start_chat()