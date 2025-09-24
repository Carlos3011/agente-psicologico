import os
import logging
from pathlib import Path
from dotenv import load_dotenv
import vertexai
import google.auth
from google.cloud import logging as google_cloud_logging
from google.adk.agents import LlmAgent
from . import prompts

root_dir = Path(__file__).parent.parent
dotenv_path = root_dir / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Use default project from credentials if not in .env
_, project_id = google.auth.default()
#Google cloud and Vertex AI configuration
PROJECT_ID = os.environ.setdefault("GOOGLE_CLOUD_PROJECT", "zenith-472804")
LOCATION = os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "us-central1")
GENAI_USE= os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


logging_client = google_cloud_logging.Client()
logger = logging_client.logger("agent_psicologico")

NAME = "Agente_Psicologico"
MODEL = "gemini-2.0-flash"
DESCRIPTION = "Agente de apoyo emocional para estudiantes de universidad"


agent = LlmAgent(
    name=NAME,
    model=MODEL,
    description=DESCRIPTION,
    instruction=prompts.PROMPT_AGENT_PSICOLIGO,
)    
root_agent = agent