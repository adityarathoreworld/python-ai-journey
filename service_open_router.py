import os 
from dotenv import load_dotenv
from openrouter import OpenRouter

load_dotenv()


def get_response(message, model="openai/gpt-4o-mini"):
    client = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))
    response = client.responses.send(
        model=model,
        input=message
    )
    if response.status != "completed":
        error = (
            response.error.message
            if response.error
            else f"Response ended as {response.status}"
        )
        raise RuntimeError(error)
    output_message = next(
        item for item in response.output
        if item.type == "message"
    )
    answer = next(
        part.text for part in output_message.content
        if part.type == "output_text"
    )

    return answer