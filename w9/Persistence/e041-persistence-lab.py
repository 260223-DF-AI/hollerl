import sqlite3
import re
from typing import Annotated, TypedDict
from langchain_aws import ChatBedrock
from langchain_core.messages import BaseMessage, HumanMessage
from langchain.agents import create_agent
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_ollama import ChatOllama
from langgraph.checkpoint.sqlite import SqliteSaver


# =====================================================================
# 1. State Definition
# =====================================================================
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], lambda x, y: x + y]

# =====================================================================
# 2. PII Masking Middleware (TODO)
# =====================================================================
def pii_middleware_node(state: AgentState):
    """
    Node that intercepts messages before the model sees them.
    Searches the last HumanMessage for a credit card number pattern
    and replaces it with '[REDACTED]' if found.
    """
    messages = state["messages"]

    # Find the last HumanMessage
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            content = msg.content

            # Regex for 13–16 digit credit card numbers (with spaces/dashes allowed)
            pattern = r'\b(?:\d[ -]*?){13,16}\b'

            # Replace matches with [REDACTED]
            redacted_content = re.sub(pattern, "[REDACTED]", content)

            # If something changed, return updated message
            if redacted_content != content:
                return {
                    "messages": [HumanMessage(content=redacted_content)]
                }

            break  # Only process the most recent HumanMessage

    # If nothing to redact, return empty update
    return {"messages": []}

# =====================================================================
# 3. Model Node
# =====================================================================
def model_node(state: AgentState):
    # Initialize the model
    model = ChatOllama(model="llama3.2")

    # Invoke the model with the conversation history
    response = model.invoke(state["messages"])

    # Return in graph-compatible format
    return {"messages": [response]}

# =====================================================================
# 4. Build the Graph
# =====================================================================
def build_graph():
    # TODO: Create a StateGraph(AgentState)
    graph = StateGraph(AgentState)
    # Add two nodes: "middleware" (pii_middleware_node) and "model" (model_node)
    # Set entry_point to "middleware"
    # Add edges: middleware -> model -> END
    graph.add_node("middleware", pii_middleware_node)
    graph.add_node("model", model_node)
    graph.set_entry_point("middleware")
    graph.add_edge("middleware", "model")
    graph.add_edge("model", END)
    
    # TODO: Create a SqliteSaver from sqlite3.connect(":memory:", check_same_thread=False)
    # Compile the graph with the checkpointer
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    checkpointer = SqliteSaver(conn)

    app = graph.compile(checkpointer=checkpointer)

    return app

# =====================================================================
# 5. Execution
# =====================================================================
def run_exercise():
    graph = build_graph()
    config = {"configurable": {"thread_id": "lab-session-001"}}
    
    print("=== e041: Persisting and Securing Agents ===")
    
    # Session 1: Send initial context (with fake PII)
    print("\n--- Session 1 ---")
    s1 = {"messages": [HumanMessage(content="My name is Alex. My card is 4111-2222-3333-4444.")]}
    # TODO: Invoke the graph (not stream) with session 1 input and config
    graph.invoke(s1, config=config)

    # Session 2: Ask a follow-up (without re-passing any context)
    print("\n--- Session 2 (Resume) ---")
    s2 = {"messages": [HumanMessage(content="What is my name? And what did I say about my card?")]}
    # TODO: Invoke the graph (not stream) with session 2 input and SAME config
    # Print the final AI message
    result = graph.invoke(s2, config=config)
    final_message = result["messages"][-1]
    print("\n--- Final AI Output ---")
    print(final_message.content)

if __name__ == "__main__":
    run_exercise()
