from crewai import Crew, Process
from agents import Researcher, Blogger
from tasks import Researcher_Task, Blogger_Task

crew = Crew(
    agents = [Researcher, Blogger],
    tasks = [Researcher_Task, Blogger_Task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)

result = crew.kickoff(inputs={'topic' : 'FREE Data Analyst Bootcamp'})
print(result)