# Chatbot Responses Database
# All response messages and fallback text for the Matrix chatbot

responses = {

    # greetings
    "hello"           : "Hey! I'm Matrix. What's up?",
    "hi" : "Hi there! How can I help you today?",
    "hii" : "Hii there! How can I help you today?",
    "hey"             : "Hey hey! What do you wanna know?",
    "good morning"    : "Good morning! Hope you're ready to learn some AI today 😄",
    "good night"      : "Good night! Don't forget to push your code before sleeping 😄",

    # asking about the bot
    "who are you"     : "I'm Matrix 🤖 - a simple rule-based chatbot built during my internship!",
    "what are you"    : "I'm a chatbot that works on pure logic. No machine learning, just good old if-else and dictionaries.",
    "your name"       : "My name is Matrix! Nothing fancy, but it works.",
    "are you a robot" : "Technically yes, but I prefer 'logic-powered assistant' 😎",
    "are you human"   : "Nope! But I was built by one 😄",

   
    # basic AI/tech stuff i learned
    "what is ai"          : "AI stands for Artificial Intelligence. It's basically teaching machines to do things that normally need human thinking.",
    "what is python"      : "Python is a programming language. It's super popular for AI and data science because the syntax is clean and easy.",
    "what is a chatbot"   : "A chatbot is a program that can have a conversation with you. Some use rules (like me), some use machine learning.",
    "what is machine learning" : "Machine learning is when a computer learns from data instead of being explicitly programmed. That's more advanced stuff - maybe project 2!",
    "what is deep learning"    : "Deep learning uses layers of neural networks. Very powerful but complex. Baby steps first - gotta master the basics!",
    "what is an llm"      : "LLM = Large Language Model. Think ChatGPT or Claude. They're probabilistic - meaning not always 100% right. That's why rule-based guardrails exist!",
    "rule based ai"       : "Rule based AI works on fixed rules written by the developer. It's predictable and transparent - you always know why it said what it said.",

    # help stuff
    "help"            : "You can ask me about AI, Python, or just chat. Try: 'what is ai' or 'tell me a joke' or 'what time is it'",
    "commands"        : "Some things you can try: hello / who are you / what is ai / what is python / joke / motivate me / time / bye",
    "what can you do" : "I can answer basic questions, tell jokes, give the time, and have a short chat. Nothing crazy - I'm just getting started!",

    # small talk / fun
    "how are you"      : "I'm doing great! Running on 0 bugs today (hopefully) 😄",
    "are you smart"    : "I know what I was taught. Which isn't that much yet, but I'm learning!",
    "tell me a joke"   : "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
    "joke"             : "A SQL query walks into a bar, walks up to two tables and asks 'Can I join you?' 😄",
    "another joke"     : "Why was the developer broke? Because they used up all their cache 😭",
    "motivate me"      : "Every single expert was once a beginner who just refused to quit. Keep going 💪",
    "i am tired"       : "Same honestly. Take a break, drink some water, then come back. You got this!",
    "i am bored"       : "Go build something! Even a small project teaches you more than just reading. Trust me.",
    "thank you"        : "You're welcome! Happy to help 😊",
    "thanks"           : "Anytime!",

    # time - handled separately inside get_response since it changes every second
    "time"             : "TIME_TOKEN",
    "what time is it"  : "TIME_TOKEN",
    "current time"     : "TIME_TOKEN",

    # exit words - using a token so i can handle them cleanly in the loop
    "bye"      : "Bye! Keep coding and learning. See you at the next milestone 👋",
    "goodbye"  : "Goodbye! Hope I was helpful. Keep being awesome 🎓",
    "exit"     : "EXIT_TOKEN",
    "quit"     : "EXIT_TOKEN",
    "stop"     : "EXIT_TOKEN",
}

# default message when bot doesn't understand something
fallback_response = "Hmm, I don't know about that yet. Try typing 'help' to see what I can answer!"
