# 🧠 Multimodal AI Agent with Gradio & GPT-4o

This project is an **AI Assistant** that can:

✅ **Extract text from images (OCR)**\
✅ **Perform simple math operations (e.g., division)**\
✅ **Handle multimodal conversations (text + image)**

The agent is powered by **GPT-4o**, **LangGraph**, and a **Gradio UI**, making it interactive and extensible.

---

## 📌 Use Case

Imagine an assistant where you can:

- Upload an **image with text**, and ask:\
  **"Extract all text from this image."**
- Perform simple computations by asking:\
  **"What is 15 divided by 3?"**

This project demonstrates how to combine tools, LLMs, and images in an interactive workflow.

---

## 🗂️ Project Overview

```
src/
├── app.py              # Gradio interface
├── run_agent.py        # Runs the AI agent pipeline
├── agent_pipeline.py   # Defines the LangGraph agent & tool loop
├── tools.py            # Custom tools: OCR & division
└── config.py           # API key loading from .env
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

**(Optional)** If you don’t have `requirements.txt`, use:

```bash
pip install gradio langchain_openai langgraph langfuse openai python-dotenv pillow
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file in the **root directory**:

```
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=your_langfuse_host
OPENAI_API_KEY=your_openai_api_key
```

> **Note**: If you don't use **Langfuse**, remove the Langfuse parts in `run_agent.py`.

---

## 🚀 Run the App

```bash
python -m src.app
```

Gradio will start a local web server, usually at:

```
http://127.0.0.1:7860/
```

---

## 🥪 How It Works

1. Upload an image (optional)
2. Enter a query (e.g., "Extract text from this image" or "Divide 10 by 2")
3. The agent decides whether to:
   - Call the **OCR tool**
   - Perform **math**
   - Respond with text

---

## 🔧 Available Tools

| Tool Name         | Description                                     |
| ----------------- | ----------------------------------------------- |
| **extract\_text** | Extracts text from an image using GPT-4o vision |
| **divide**        | Divides two numbers safely                      |

---

## 🧰 Tech Stack

- **Gradio** – Web UI
- **LangGraph** – Tool orchestration & agent loop
- **OpenAI GPT-4o** – LLM & vision model
- **Langfuse** – Optional tracing
- **Pillow** – Image processing

---

## 💡 Example Inputs

### Image Text Extraction:

- Upload an image with text
- Input:
  ```
  Extract all text from the uploaded image.
  ```

### Division:

- Input:
  ```
  What is 20 divided by 5?
  ```

---

## 🗺️ Graph Visualization

If supported, the agent displays its execution graph using **LangGraph’s Mermaid diagram**.\
This helps visualize decision points between LLM responses and tool calls.

---

## 📈 Potential Enhancements

- Add more tools (summarization, image captioning, etc.)
- Use RAG (Retrieval Augmented Generation) for document processing
- Deploy on cloud platforms (e.g., Hugging Face Spaces, AWS)

---

## 🤝 Contributing

Pull requests and issues are welcome!\
For major changes, please open an issue first.

---

## 📝 License

MIT License

---

## 🔗 Links

- [LangGraph Documentation](https://github.com/langchain-ai/langgraph)
- [Gradio Documentation](https://www.gradio.app/)
- [OpenAI API Docs](https://platform.openai.com/docs)

