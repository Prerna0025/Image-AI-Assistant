from langfuse.langchain import CallbackHandler
from langchain_core.messages import HumanMessage
from IPython.display import Image, display

from src.agent_pipeline import build_graph
from .config import api_keys
import os

def run_agent(input_text:str, image_file:None) ->str:
    
    api_key = api_keys()
    os.environ["LANGFUSE_PUBLIC_KEY"] = api_key["LANGFUSE_PUBLIC_KEY"]
    os.environ["LANGFUSE_SECRET_KEY"] = api_key["LANGFUSE_SECRET_KEY"]
    os.environ["LANGFUSE_HOST"] = api_key["LANGFUSE_HOST"]
    langfuse_handler = CallbackHandler()
    
    graph = build_graph()
    image_path=None
    if image_file:
        image_path="temp_user_image.png"
        image_file.save(image_path)
    try:
        
        img = Image(graph.get_graph(xray=True).draw_mermaid_png())
        display(img)
        
    except Exception:
        print("Graph visualization skipped")
        
    messages = [HumanMessage(content=input_text)]
    output = graph.invoke({
        "messages": messages,
        #"input_file":image_file
        "input_file":image_path
    },
        config = {"callbacks":[langfuse_handler]}
        )

    
    if image_path:
        os.remove(image_path)
    #os.remove(image_path)    
    return (output['messages'][-1].content)
    
    
'''   
    for m in output['messages']:
        m.pretty_print()
       
if __name__ == "__main__":
    main()
'''