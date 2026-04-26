'''
    Single Source of Truth for all configuration constants.
    Any module that needs API. model name , retries, limits or path constants 
    import from here

    Which AI model to use, how many retries for API calls, where to find datasets?
    Where the files are stored?
    Whats the API key?
'''

import os
from pathlib import Path
from dotenv import load_dotenv

# Project Root directory
# Path(__file__).parent is the directory containing this config.py file
# .parent is used to get the parent directory, 
# which is the project root in the case 

PROJECT_ROOT = Path(__file__).parent

# Load environment variables from PROJECT_ROOT.env file in project root
load_dotenv(PROJECT_ROOT / ".env")

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Settings
DEFAULT_MODEL = "gemini-2.5-flash"

# Retry settings for API calls
MAX_RETRIES = 3
RETRY_DELAY = 2 

# Dataset Configuration
DEFAULT_DATASET = PROJECT_ROOT / "scam_detection_dataset.csv"
TEST_DATASET = PROJECT_ROOT / "test_scam_dataset.csv"

# Text column names to look for in datasets
TEXT_COLUMNS = ["text", "message_text", "message"]
LABEL_COLUMN = "label"

# Paths for outputs and logs
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create output directories if they don't exist
OUTPUTS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

def get_dataset_path(filename: str) -> Path:
    """
    Find dataset file in project directory.
    
    Args:
        filename: Name of the dataset file
        
    Returns:
        Path to the dataset file
        
    Raises:
        FileNotFoundError: If file not found
    """
    # Try direct path first
    if Path(filename).exists():
        return Path(filename)
    
    # Try project root
    project_path = PROJECT_ROOT / filename
    if project_path.exists():
        return project_path
    
    raise FileNotFoundError(f"Dataset '{filename}' not found")

