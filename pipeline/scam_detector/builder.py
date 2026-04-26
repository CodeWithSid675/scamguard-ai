from llm.prompts import generate_prompt

def build_prompt(message:str,startegy:str = "react") -> str:
    '''
    Build a prompt for the given message and strategy.

    Args:
        message (str): The message to build the prompt for.
        startegy (str): The strategy to use for building the prompt. Default is "react".

    Returns:
        str: The generated prompt.  
    '''
    if startegy == "react":
        return generate_prompt(message)
    else:
        raise NotImplementedError(f"Strategy {startegy} is not implemented yet.")

# def generate_prompt(message:str) -> str:


