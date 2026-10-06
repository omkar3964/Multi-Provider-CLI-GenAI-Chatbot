# Multi-Provider CLI GenAI Chatbot

## What are we building?

A small Python chatbot that runs in your terminal and can talk to:

- **OpenAI** (cloud)
- **Google Gemini** (cloud)
- **Ollama** (a model running on your own computer)

You type a message, Python sends it to the model you picked, and the answer is printed back.

```text
You  ->  Python CLI  ->  LLM  ->  Response  ->  Terminal
```

This is a learning project, not a production application. The whole thing is about 150 lines of Python.

## What will I learn?

- How to call an LLM from Python
- How API keys work and why we keep them out of our code
- How to use a `.env` file with `python-dotenv`
- How to read configuration values in Python
- How to send a prompt and read the response
- How to build a simple CLI loop with `input()` and `while True`
- The difference between a cloud LLM API and a local LLM

## Project structure

```text
chatbot.py        The main program: the welcome message and the chat loop
config.py         Loads the settings from the .env file
providers.py      Three small functions, one per provider
.env.example      A template you copy to .env and fill in
.gitignore        Keeps .env and the virtual environment out of git
requirements.txt  The Python packages we need
README.md         This file
```

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 2. Install the packages

```bash
pip install -r requirements.txt
```

## Configure .env

Copy the example file and name the copy `.env`:

Windows (PowerShell):

```powershell
copy .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

Now open `.env` and pick **one** provider with `LLM_PROVIDER`. You only need to fill in the
settings for the provider you chose.

`SYSTEM_PROMPT` is the instruction given to the model before your message. Changing it is the
easiest way to change how the assistant behaves, for example
`SYSTEM_PROMPT=You are a Python tutor for complete beginners.`

### OpenAI

Create an API key at <https://platform.openai.com/api-keys>, then set:

```text
LLM_PROVIDER=openai
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
```

`OPENAI_MODEL` must be a model name that exists today and that your account can use. Model names
change over time, so check OpenAI's model list if you are unsure.

### Gemini

Create an API key at <https://aistudio.google.com/apikey>, then set:

```text
LLM_PROVIDER=gemini
GEMINI_API_KEY=
GEMINI_MODEL=gemini-2.0-flash
```

As with OpenAI, use a model name that is currently available.

### Ollama

Ollama runs a model on your own machine, so there is no API key. You need to:

1. Install Ollama from <https://ollama.com>.
2. Make sure it is running (it listens on `http://localhost:11434`).
3. Download a model first, for example `ollama pull llama3.2`.

Then set:

```text
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

The model in `OLLAMA_MODEL` must already exist on your computer. This project never downloads
models for you.

## Run

```bash
python main.py
```

## Example

```text
========================================
      Simple GenAI CLI Chatbot
========================================

Provider: openai
Model: gpt-4o-mini
Type /help for commands.

You: Hello

Assistant: Hello! How can I help you today?

You: Explain Python in simple words.

Assistant: Python is a programming language that reads a lot like English...

You: /exit

Goodbye!
```

Commands:

- `/help` shows the available commands
- `/exit` (or just `exit`) quits

## Troubleshooting

**`Error: OPENAI_API_KEY is missing.`**
You have not created `.env` yet, or the key line is empty. Copy `.env.example` to `.env` and paste
your key after the `=` sign, with no quotes and no spaces.

**`Error: LLM_PROVIDER is '...'`**
`LLM_PROVIDER` must be exactly `openai`, `gemini` or `ollama`, in lowercase.

**`Error: The model name for openai is missing.`**
Fill in `OPENAI_MODEL`, `GEMINI_MODEL` or `OLLAMA_MODEL` for the provider you chose.

**`Sorry, the request failed: ... model ... does not exist`**
The model name is wrong or your account cannot use it. Try another model name.

**`Sorry, the request failed: Could not reach Ollama ...`**
Ollama is not running. Start it and try again.

**`ModuleNotFoundError: No module named 'openai'`**
The packages are not installed, or your virtual environment is not activated. Activate it and run
`pip install -r requirements.txt` again.

**Gemini prints a long message about "automatic function calling".**
That is a warning from Google's library, not an error from your code. You can ignore it.

**Nothing is remembered between questions.**
That is expected. Each message is sent on its own, so the model does not know what you asked
before. Adding conversation history is a good next exercise.