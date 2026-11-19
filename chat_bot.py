import service_open_router

def chat_bot(message):
    answer = service_open_router.get_response(message)
    return(answer)

def main():
    user_input = input("Ask me anything to continue: ")
    bot_answer = chat_bot(user_input)
    print(bot_answer)

if __name__ == "__main__":
    main()