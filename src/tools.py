import base64
from typing import Optional

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
import os
import openai
from .config import api_keys


api_key = api_keys()
print("API Key: ",api_key["OPENAI_API_KEY"])
vision_llm = ChatOpenAI(model="gpt-4o",api_key=api_key["OPENAI_API_KEY"])

def extract_text(img_path:str)->str:
    """Extract text from an image file using a multimodel model.

    Args:
        img_path (str): A local image file path

    Returns:
        str: A single string containing the concatenated text extracted from each image.
    """
    all_text = ""
    try:
        with open(img_path, "rb") as image_file:
            image_bytes = image_file.read()
            
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        
        messages = [
            HumanMessage(
                content=[
                    {"type":"text", 
                     "text": "Extract all the text from this image. Return only the text." 
                     },
                    
                    {"type":"image_url",
                     "image_url": {"url": f"data:image/png;base64,{image_base64}"}
                     },
                ]
            )
        ]
        
        response = vision_llm.invoke(messages)
        return response.content.strip()
    
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""
    
def divide(a:int, b:int) -> Optional[float]:
    """Divide a and b

    Args:
        a (int): Its an integer value
        b (int): Its an integer value

    Returns:
        Optional[float]: give the integer the float value.
    """
    try:
        return a/b
    except Exception as e:
        print(f"Error in divide: {e}")
        return ""