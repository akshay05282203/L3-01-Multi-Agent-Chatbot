
# 🛰️ Atlas — Multi-Agent Research Chatbot

An AI-powered research chatbot built with **LangChain, Groq, Tavily, BeautifulSoup, and Streamlit**. Atlas automates web research by searching for relevant information, extracting webpage content, generating a research report, and evaluating the report.

## 🎯 Features

* 🧩 Multi-agent research workflow
* 🕵️ Tavily-powered web search
* 📚 Web scraping with BeautifulSoup
* 🛠️ Custom tool calling
* ✍️ Automated research report generation
* 🧑‍⚖️ AI-based report evaluation
* 🔗 LCEL Writer and Critic chains
* 🧠 Groq LLM integration
* 🎛️ Streamlit interface
* 📦 Markdown report download
* 🔑 Environment-based API key management

## 🧬 Architecture

```text
User
 │
 ▼
Research Topic
 │
 ▼
🕵️ Search Agent
 │
 ▼
Tavily Search
 │
 ▼
📚 Reader Agent
 │
 ▼
BeautifulSoup Scraping
 │
 ▼
✍️ Writer Chain
 │
 ▼
🧑‍⚖️ Critic Chain
 │
 ▼
Final Research Report
```

### Agent Workflow

**Search Agent**

* Searches the web using Tavily
* Finds relevant titles, URLs, and snippets

**Reader Agent**

* Selects a relevant source
* Scrapes and cleans webpage content

### LCEL Workflow

The Writer and Critic use LangChain Expression Language:

```python
writer_chain = writer_prompt | llm | StrOutputParser()

critic_chain = critic_prompt | llm | StrOutputParser()
```

## 🛠️ Custom Tools

### `web_search`

Uses Tavily to search the web.

```python
@tool
def web_search(query: str) -> str:
    ...
```

### `scrape_url`

Uses Requests and BeautifulSoup to extract readable webpage content.

```python
@tool
def scrape_url(url: str) -> str:
    ...
```

## 🧠 LLM Configuration

The project uses Groq for LLM inference:

```python
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
```

## 🔗 Research Pipeline

```text
Research Topic
      ↓
Search Agent
      ↓
Tavily Results
      ↓
Reader Agent
      ↓
Scraped Content
      ↓
Writer Chain
      ↓
Research Report
      ↓
Critic Chain
      ↓
Evaluation
```

## 🎛️ Streamlit Interface

Atlas provides a simple Streamlit interface where users can enter a research topic and view:

* 📑 Research Report
* 🧾 Critique
* 🔗 Sources
* 📚 Scraped Content

Reports can be downloaded as Markdown files.

## 🗃️ Project Structure

```text
L3-01-Multi-Agent-Chatbot/
│
├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── README.md
└── .gitignore
```

| File               | Purpose                   |
| ------------------ | ------------------------- |
| `app.py`           | Streamlit interface       |
| `agents.py`        | Agents and LCEL chains    |
| `pipeline.py`      | Research workflow         |
| `tools.py`         | Search and scraping tools |
| `requirements.txt` | Dependencies              |

## ⚡ Technologies

* Python
* LangChain
* Groq
* Tavily
* BeautifulSoup
* Requests
* Streamlit
* LCEL
* Pydantic
* python-dotenv

## 🧰 Installation

### Clone Repository

```bash
git clone https://github.com/akshay05282203/L3-01-Multi-Agent-Chatbot.git
cd L3-01-Multi-Agent-Chatbot
```

### Create Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configuration

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Never commit API keys to GitHub.

Recommended `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

## 🚦 Run

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

The pipeline can also be executed directly:

```bash
python pipeline.py
```

## 🧩 Concepts Demonstrated

* Generative AI
* AI Agents
* Multi-Agent Systems
* Tool Calling
* LangChain
* LCEL
* Prompt Engineering
* Groq LLM
* Web Search
* Web Scraping
* Automated Research
* AI Evaluation
* Streamlit
* Modular Python Architecture

## 🔮 Future Improvements

* LangGraph state-based workflow
* Parallel research agents
* Source verification
* Citation-aware reports
* RAG and vector database integration
* PDF/DOCX export
* Research history
* Human-in-the-loop review
* Docker and cloud deployment

## 🧑‍💻 Author

**Akshay Chavan AI**

**Interests:** Artificial Intelligence, Machine Learning, Generative AI, Agentic AI, Multi-Agent Systems, LangChain, LangGraph, RAG, AI Automation, and Data Science.

## ⚖️ License

This project is developed for educational, portfolio, and learning purposes.
