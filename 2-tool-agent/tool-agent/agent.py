from google.adk.agents import Agent
from google.adk.tools import google_search
import datetime


def get_time(format: str): #default values dont work in adk
    """
    Get the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current-time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# root_agent = Agent(
#     model='gemini-2.0-flash-001',
#     name='tool_agent',
#     description='A helpful assistant for user questions.',
#     instruction="""
#         Answer user questions using the following tools:
#         -google-search
#         """,
#         tools=[google_search],
#         # tools=[google_search, get-time] doesnt work
# )
root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='tool_agent',
    description='A helpful assistant for user questions.',
    instruction="""
        Answer user questions using the following tools:
        -get_time
        """,
        tools=[get_time],
        # tools=[google_search, get-time] doesnt work
)