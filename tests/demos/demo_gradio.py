import sys

import gradio as gr

from dotenv import load_dotenv
import os

sys.path.insert(0, './agency-swarm')

from agency_swarm import set_openai_key, Agent
from agency_swarm.agency.agency import Agency
from agency_swarm.tools.oai import FileSearch, CodeInterpreter

# Load the environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
set_openai_key(api_key)

ceo = Agent(name="CEO",
            description="Responsible for client communication, task planning and management.",
            instructions="Analyze uploaded files with myfiles_browser tool.", # can be a file like ./instructions.md
            tools=[FileSearch, CodeInterpreter])


test_agent = Agent(name="Test Agent1",
                     description="Responsible for testing.",
                     instructions="Read files with myfiles_browser tool.", # can be a file like ./instructions.md
                     tools=[FileSearch])

test_agent2 = Agent(name="Test Agent2",
                     description="Responsible for testing.",
                     instructions="Read files with myfiles_browser tool.", # can be a file like ./instructions.md
                     tools=[FileSearch])



agency = Agency([
    ceo, test_agent, test_agent2
], shared_instructions="")

agency.demo_gradio()

# print(agency.get_completion("Hello", recipient_agent=test_agent, yield_messages=False))

