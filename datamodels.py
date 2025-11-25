# building a modular AI Agent framework
from pydantic import BaseModel
from typing import List, Callable, Union, Optional, Tuple, Dict

# used for tool functions that the agent can run
# Function that returns: A string, or Another Agent, or A dictionary
Function = Callable[[], Union[str, "Agent", dict]]

# An AI agent object.
class Agent(BaseModel):
    name: str = "ZeroAgent"
    model: str = "gpt-4o"
    instructions: Union[str, Callable[[], str]] = "You are a helpful agent."
    functions: List[Function] = []
    tool_choice: str = None
    parallel_tool_calls: bool = False
    examples: Union[List[Tuple[dict, str]], Callable[[], str]] = []
    handle_mm_func: Callable[[], str] = None # function for handling multimodal input
    agent_teams: Dict[str, Callable] = {} # multi-agent collaboration
