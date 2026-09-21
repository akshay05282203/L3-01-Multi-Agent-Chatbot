from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search , scrape_url
from dotenv import load_dotenv
load_dotenv()
import os
#model_setup
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


print("GROQ KEY LOADED:", os.getenv("GROQ_API_KEY"))  

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

# 1 agent - search
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt=(
            "You are a research search agent. "
            "Call the web_search tool ONCE with a well-formed query. "
            "Then immediately summarize the results, preserving all titles and URLs. "
            "Do NOT call the tool more than twice. Do not search again once you have results."
        ),
    )

# 2- agnet - scrap
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
        system_prompt=(
            "You are a reader agent. "
            "Pick the single most relevant URL from the provided search results and "
            "call scrape_url ONCE on it. Then summarize the scraped content and stop. "
            "If scraping fails, say so and stop — do not retry more than once."
        ),
    )

#writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm  | StrOutputParser()


#critic_chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])


critic_chain = critic_prompt | llm | StrOutputParser()