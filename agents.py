from crewai import Agent
from tools import tool
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"


Researcher = Agent(
    role = 'Research Youtube videos',
    goal = 'Understand and get the right video content from the Youtube chaanel on the {topic}',
    verboe = True,
    memory = True,
    backstory = ('Should be an expert in understanding topics related to data analytics, machine learning and AI and also provide suggestions'
    ),
tools = [tool],
allow_delegation = True
)


Blogger = Agent(
    role = 'Write Blogs from Youtube videos',
    goal = 'Narrate the details from the Youtube video on the {topic}',
    verboe = True,
    memory = True,
    backstory = ("With a flair for simplifying complex topics, you craft" 
                 "engaging narratives that captivate and educate, bringing new" 
                 "discoveries to light in an accessible manner."
    ),
tools = [tool],
allow_delegation = False
)