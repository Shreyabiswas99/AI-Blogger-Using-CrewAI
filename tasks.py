from crewai import Task
from tools import tool
from agents import Researcher, Blogger

Researcher_Task = Task(
  description = ("Identify the video {topic}."
    "Gather detailed information about that video from the Youtube channel"
  ),
  expected_output = 'A 3 paragraph long report based on the {topic} of video content.',
  tools = [tool],
  agent = Researcher,
)

Blogger_Task = Task(
  description = ("Get the information from the Youtube channel on the {topic}."),
  expected_output = 'Summarize the contents from the video of the Youtube channel on the {topic} and create the blog contents',
  tools = [tool],
  agent = Blogger,
  async_execution = False,
  output_file = 'new-blog-post.md'  
)