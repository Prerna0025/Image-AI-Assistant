import os
from dotenv import load_dotenv


def api_keys():
    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'.env')
    load_dotenv(dotenv_path)
    
    return {
        "LANGFUSE_PUBLIC_KEY": os.getenv("LANGFUSE_PUBLIC_KEY"),
        "LANGFUSE_SECRET_KEY": os.getenv("LANGFUSE_SECRET_KEY"),
        "LANGFUSE_HOST": os.getenv("LANGFUSE_HOST"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
    }
    '''
    os.environ["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
    os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")
    os.environ["LANGFUSE_HOST"] = os.getenv("LANGFUSE_HOST")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    '''
