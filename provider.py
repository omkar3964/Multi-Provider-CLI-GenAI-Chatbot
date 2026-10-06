import config
import requests
from google import genai
from openai import OpenAI


def ask_openai(message):
    """Send a single message to OpenAI and return the response as text."""

    client = OpenAI(api_key=config.OPENAI_API_KEY)

    response = client.responses.create(
        model=config.OPENAI_MODEL,
        instructions=config.SYSTEM_PROMPT,
        input=message
    )

    return response.output_text


def ask_gemini(message):
    """Send a single message to Gemini and return the response as text."""

    client = genai.Client(api_key=config.GEMINI_API_KEY)

    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=message,
        config={
            "system_instruction": config.SYSTEM_PROMPT
        }
    )

    return response.text


def ask_ollama(message):
    """Send a single message to Ollama and return the response as text."""

    # Ollama runs locally, so no API key is required.
    try:
        response = requests.post(
            config.OLLAMA_BASE_URL + "/api/chat",
            json={
                "model": config.OLLAMA_MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": config.SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "stream": False,
            },
            timeout=120,
        )

    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Could not reach Ollama at "
            + config.OLLAMA_BASE_URL
            + ". Is Ollama running?"
        )

    response.raise_for_status()

    return response.json()["message"]["content"]