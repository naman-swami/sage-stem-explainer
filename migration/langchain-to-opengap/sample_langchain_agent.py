from langchain.agents import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI

@tool
def calculate_trajectory(velocity: float, angle: float) -> str:
    """Calculate the trajectory of a projectile given its velocity and angle."""
    return f"Trajectory calculated for v={velocity} and a={angle}"

system_message = """You are Sage, an expert STEM explainer.
Your primary role is to break down complex physics and math topics from first principles.
You never skip steps in calculations."""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

llm = ChatOpenAI(model="gpt-4", temperature=0)
tools = [calculate_trajectory]

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Example run:
# agent_executor.invoke({"input": "Explain projectile motion and calculate for v=10, a=45"})
