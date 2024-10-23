# Chatbot

A simple chatbot realized to test Docker, Ollama and Streamlit technologies

## Installation

Download Ollama docker image by running the following command:
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Download an LLM, for example Llama3, by using:
```bash
docker exec -it ollama ollama run llama3
```

Clone the repository:

```bash
git clone https://github.com/zambo990/chatbot.git
```

Enter the directory of the project:
```bash
cd chatbot
```
Start the Docker containers
```bash
docker compose up
```
