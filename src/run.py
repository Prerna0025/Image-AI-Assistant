from langfuse.langchain import CallbackHandler
from langchain_core.messages import HumanMessage
from IPython.display import Image, display

from src.agent_pipeline import build_graph
from .config import api_keys
import os
def main():
    
    api_key = api_keys()
    os.environ["LANGFUSE_PUBLIC_KEY"] = api_key["LANGFUSE_PUBLIC_KEY"]
    os.environ["LANGFUSE_SECRET_KEY"] = api_key["LANGFUSE_SECRET_KEY"]
    os.environ["LANGFUSE_HOST"] = api_key["LANGFUSE_HOST"]
    langfuse_handler = CallbackHandler()
    
    graph = build_graph()
    
    try:
        
        img = Image(graph.get_graph(xray=True).draw_mermaid_png())
        display(img)
        
    except Exception:
        print("Graph visualization skipped")
        
    messages = [HumanMessage(content="Divide 6790 by 5")]
    output = graph.invoke({
        "messages": messages,
        "input_file":None
    },
        config = {"callbacks":[langfuse_handler]}
        )
    print(output)
    
    
    
    for m in output['messages']:
        m.pretty_print()
       
if __name__ == "__main__":
    main()