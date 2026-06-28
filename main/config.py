"""
Configuration for GitLab Weekly Report Generator
"""

import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

# -----------------------------
# Environment Variables
# -----------------------------

GITLAB_BASE_URL = os.getenv("GITLAB_BASE_URL")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
LLM_MODEL = os.getenv("LLM_MODEL")
LLM_URL = os.getenv("LLM_URL")
GRAPHQL_ENDPOINT = os.getenv("GRAPHQL_ENDPOINT")

# -----------------------------
# Project Directories
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent

CACHE_DIR = BASE_DIR / "cache"
RAW_CACHE_DIR = CACHE_DIR / "raw"
NORMALIZED_CACHE_DIR = CACHE_DIR / "normalized"

OUTPUT_DIR = BASE_DIR / "output"

PROMPT_DIR = BASE_DIR / "prompts"

folders = [
    CACHE_DIR, 
    RAW_CACHE_DIR, 
    NORMALIZED_CACHE_DIR, 
    OUTPUT_DIR, 
    PROMPT_DIR
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Network
# -----------------------------

REQUEST_TIMEOUT = 60

MAX_CONCURRENT_REQUESTS = 5

# -----------------------------
# Output files
# -----------------------------

MARKDOWN_FILE = OUTPUT_DIR / "weekly_report.md"

PDF_FILE = OUTPUT_DIR / "weekly_report.pdf"
