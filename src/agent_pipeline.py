from typing import TypedDict, Annotated,Optional,List
from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage
from langgraph.graph.message import add_messages
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import convert_to_openai_tool

from .tools import divide, extract_text
from .config import api_keys

api_key = api_keys()
llm = ChatOpenAI(model='gpt-4o',api_key=api_key["OPENAI_API_KEY"])
tools = [divide,extract_text]
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

class AgentState(TypedDict):
    input_file: Optional[str]
    messages: Annotated[List[AnyMessage],add_messages]
    
    
def assistant(state: AgentState) -> AgentState:
    """LLM Assistant that decides to respond or call a tool."""
    textual_description_of_tool="""
    extract_text(image_path:str) -> str:
        Extract text froma an image file using a multimodel model.
        
        Args:
            img_path: A local image file path (strings).
            
        Returns:
            A single string containing the concatenated text extracted from each image.
            
    divide(a:int, b:int) -> float:
    Divide a and b     
         
    """
    image = state['input_file']
    sys_message = SystemMessage(
        content= f"You are an helpful agent that can analyse some images and run some computations with provided tools: \n{textual_description_of_tool} \n You have access to some optional images. currently the loaded images is: {image}")
    
    return {"messages": [llm_with_tools.invoke([sys_message] + state["messages"])], "input_file": state["input_file"]}


def build_graph():
    """Construct the agent tool loop graph"""
    
    builder = StateGraph(AgentState)
    builder.add_node("assistant",assistant)
    builder.add_node("tools",ToolNode(tools))
    
    builder.add_edge(START,"assistant")
    builder.add_conditional_edges("assistant",tools_condition)
    builder.add_edge("tools","assistant")
    
    return builder.compile()   
'''
def final_answer():
    Astate = AgentState()
    
    for m in Astate['messages']:
        m.pretty_print()
'''

