# chatbot/ai.py

# def get_bot_response(user_input):
#     user_input = user_input.lower()

#     if "hello" in user_input:
#         return "Hi! How can I assist you with your event?"
#     elif "book" in user_input:
#         return "Sure! What type of event would you like to book?"
#     elif "thanks" in user_input:
#         return "You're welcome 😊"
#     else:
#         return "Sorry, I didn’t understand. Can you please rephrase?"




def get_chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "👋 Hello! I'm your Event Assistant. How can I help you today?"
    
    elif "book" in message or "booking" in message:
        return "🎫 Sure! You can book an event by going to our 'Events' page. Do you want to book a wedding, party, or conference?"
    
    elif "price" in message or "cost" in message or "charges" in message:
        return "💰 Our pricing depends on the type and scale of the event. Would you like to see the packages?"
    
    elif "theme" in message or "decoration" in message:
        return "🎨 We offer a wide range of themes! From floral to Bollywood, we've got you covered. Want to explore some themes?"

    elif "contact" in message or "help" in message:
        return "📞 You can reach out via our 'Contact Us' page. Or let me know your query, I’ll try to help here!"

    elif "location" in message or "venue" in message:
        return "📍 We operate in major cities. Please tell me your city or area so I can check available venues."

    elif "bye" in message or "thank you" in message:
        return "😊 You're welcome! Feel free to chat with me anytime. Have a great day!"

    else:
        return "🤖 I'm still learning. Could you please rephrase or ask about booking, pricing, themes, or contact info?"
