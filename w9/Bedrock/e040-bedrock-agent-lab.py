from pydantic import BaseModel, Field
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama
# =====================================================================
# 1. Pydantic Structured Output Schema
# =====================================================================
# TODO: Define a 'StockRecommendation' class inheriting from BaseModel.
# Fields:
#   - ticker (str): The stock ticker (e.g. "TSLA")
#   - recommendation (str): "BUY", "SELL", or "HOLD"
#   - reasoning (str): A one-sentence justification.
class StockRecommendation(BaseModel):
    ticker: str
    recommendation: str
    reasoning: str

# =====================================================================
# 2. Tool Definition
# =====================================================================
# TODO: Define a @tool function named 'get_stock_sentiment'.
# It should accept 'ticker: str' and return a str.
# Write a clear docstring — the LLM reads it to know when to call this tool.
# Include mock sentiment data for at least 3 tickers (AAPL, TSLA, AMZN).

@tool
def get_stock_sentiment(ticker: str) -> str:
    """Returns the current stock sentiment for a given ticker symbol."""
    data = {"AAPL": "FEAR", "AMZN": "NEUTRAL", "GOOGL": "GREED", "TSLA": "GREED"}
    return data.get(ticker.upper(), "Ticker not found.")


# =====================================================================
# 3. Agent Initialization
# =====================================================================
# TODO: Use init_chat_model() to initialize Amazon Bedrock.
# Use model="us.anthropic.claude-3-5-sonnet-20240620-v1:0"
# Use model_provider="bedrock" and temperature=0

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# =====================================================================
# 4. Create the ReAct Agent
# =====================================================================
# TODO: Use create_react_agent with your llm, tools list, and a
# professional financial-analyst system_prompt (via state_modifier).

system_prompt = "You are a professional financial-analyst. Use the stock tool for any sentiment queries."
tools = [get_stock_sentiment]
agent = create_agent(llm, tools, system_prompt=system_prompt, response_format=StockRecommendation)

# =====================================================================
# 5. Stream the Agent Response
# =====================================================================
def run_exercise():
    query = {"messages": [("user", "What is your recommendation for Tesla (TSLA) stock?")]}
    
    # TODO: Stream the agent using .stream(query, stream_mode="values")
    # For each chunk, print the last message's type and content.
    print("=== e040: Your First Bedrock Agent ===")
    # YOUR CODE HERE
    for chunk in agent.stream(query, stream_mode="values"):
        message = chunk["messages"][-1]
        print(f"[{message.type.upper()}]: {message.content}")

if __name__ == "__main__":
    run_exercise()
