# building a modular AI Agent framework
from pydantic import BaseModel
from typing import List, Callable, Union, Optional, Tuple, Dict

# used for tool functions that the agent can run
# Function that returns: A string, or Another Agent, or A dictionary
Function = Callable[[], Union[str, "Agent", dict]]


"""
How it works:
1. Agent receives a user message

2. LLM decides:
    → Respond normally
    OR
    → Call a tool (function)

3. The tool returns a Result

4. Framework wraps everything in a Response

5. Final answer is produced
"""

# Agent → describes an AI agent (its model, tools, instructions, etc.)
# An AI agent object.
class Agent(BaseModel):
    name: str = "ZeroAgent"
    model: str = "gpt-4o"
    instructions: Union[str, Callable[[], str]] = "You are a helpful AI agent." # variable can be either: ✔️ a string or ✔️ a function that takes no arguments and returns a string.
    functions: List[Function] = []
    tool_choice: str = None
    parallel_tool_calls: bool = False
    examples: Union[List[Tuple[dict, str]], Callable[[], str]] = [] # list of (dict, string) 
    handle_mm_func: Callable[[], str] = None # function for handling multimodal input
    agent_teams: Dict[str, Callable] = {} # multi-agent collaboration



# Response → represents the agent’s reply + internal state
# represents what the agent returns after interacting.
class Response(BaseModel):
    messages: List = [] # List of all conversation messages.
    agent: Optional[Agent] = None # The agent that produced the response.
    context_variables: dict = {} # Memory or intermediate data that is carried across steps.



# Result → represents the output from a tool/function
# what a tool function returns
class Result(BaseModel):
    value: str = "" # The output string
    agent: Optional[Agent] = None # Sometimes a tool returns a new agent.
    context_variables: dict = {} # Allows a tool to store memory
    image: Optional[str] = None # for visualization tools
