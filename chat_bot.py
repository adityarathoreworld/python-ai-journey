import service_open_router
def chat_bot(message, summary_text):
    prompt = summary_text + "\nUser: " + message
    answer = service_open_router.get_response(prompt)
    updated_summary = (
        prompt + "\nAssistant: " + answer
    )
    return answer, updated_summary

def main():
    user_input = input("Ask me anything to continue: ")
    summary_text = ""
    while user_input.lower() != "exit":
        bot_answer, summary_updated = chat_bot(user_input, summary_text)
        summary_text = summary_updated
        print("AI:", bot_answer)
        print("Summary:", summary_text)
        user_input = input("Ask me anything or type 'exit': ")

if __name__ == "__main__":
    main()