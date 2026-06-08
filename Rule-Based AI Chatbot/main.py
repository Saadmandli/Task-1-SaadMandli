#Project 1 - Rule Based Chatbot
import datetime
from responses import responses, fallback_response


# --- sanitize function ---
# this cleans the user input before checking it
# converts to lowercase and removes extra spaces from both sides

def sanitize_input(user_text):
    cleaned = user_text.lower().strip()
    return cleaned


# --- get response function --- this checks the cleaned input against the responses dictionary

def get_response(clean_text):

    reply = responses.get(clean_text, fallback_response)

    # handle the time token separately since it needs real-time value
    if reply == "TIME_TOKEN":
        now = datetime.datetime.now()
        formatted_time = now.strftime("%I:%M %p on %d %B %Y")
        reply = "Current time is: " + formatted_time + " 🕐"

    return reply


# --- main chatbot loop --- this is where we take user input, sanitize it, get a response, and print it out

def start_chat():
    print("=" * 55)
    print("     Matrix - Rule Based AI Chatbot 🤖")
    print("     Built by Saad Mandli| AI Enthusiast")
    print("=" * 55)
    print("  Type 'help' to see commands. Type 'exit' to quit.")
    print("-" * 55)

    while True:

        # phase 1 - take input from user
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            # handles ctrl+c so it doesn't crash with a big error
            print("\nMatrix: Alright, force quitting. Bye! 👋")
            break

        # ignore blank inputs - just loop again
        if user_input.strip() == "":
            continue

        # phase 2 - sanitize / normalize the input
        clean = sanitize_input(user_input)

        # phase 3 - get the bot's reply
        reply = get_response(clean)

        # check if it's an exit command
        # EXIT_TOKEN means user wants to stop the chatbot
        if reply == "EXIT_TOKEN":
            print("Matrix: Shutting down... Goodbye Engineer! Keep building 🚀\n")
            break

        # phase 4 - print the response
        print("Matrix: " + reply + "\n")

if __name__ == "__main__":
    start_chat()