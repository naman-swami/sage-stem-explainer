from crewai import Agent, Crew, Process, Task
import yaml

with open('sample_crew.yaml', 'r') as file:
    agents_config = yaml.safe_load(file)['agents']

researcher = Agent(
  config=agents_config['researcher']
)

writer = Agent(
  config=agents_config['writer']
)

# Tasks and Crew definition would follow here...
