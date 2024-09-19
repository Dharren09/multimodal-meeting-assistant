import streamlit as st
from crewai import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
from langchain_ollama import OllamaLLM
# from langchain_openai import AzureChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import  SerperDevTool
import os
import getpass
import logging

# setup logging configuration
logging.basicConfig(level=logging.INFO)

# set up streamlot tool
st.set_page_config(page_title="JeyMeetings.ai", layout="wide", page_icon="🤝")
st.title("Your AI meeting Partner")

# side Bar for API keys
st.sidebar.title("API Keys")
# azureopenai_endpoint = st.sidebar.text_input("AzureOpenai Endpoint", type="default")
# azureopenai_api_key = st.sidebar.text_input("AzureOpenai API Key", type='password')
anthropic_api_key = st.sidebar.text_input("Anthropic API Key", type="password")
gemini_api_key = st.sidebar.text_input("Gemini API key", type="password")
serper_api_key = st.sidebar.text_input("Serper API Key", type="password")

# checking if all api keys are set
api_keys = [anthropic_api_key, serper_api_key, gemini_api_key]
if all(api_keys):
    # set as environment variables
    
    # os.environ['AZUREOPENAI_ENDPOINT'] = azureopenai_endpoint
    # os.environ['AZUREOPENAI_API_KEY'] = azureopenai_api_key
    os.environ['ANTHROPIC_API_KEY'] = getpass.getpass(anthropic_api_key)
    os.environ['SERPER_API_KEY'] = getpass.getpass(serper_api_key)
    os.environ['GEMINI_API_KEY'] = getpass.getpass(gemini_api_key)
    
    # initialize the AI models and tools
    # o1 = AzureChatOpenAI(model_name="o1-mini")
    # gpt4 = AzureChatOpenAI(model_name="gpt-4o-mini")
    ollama = OllamaLLM(model="llama3.1")
    gemini_pro = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=gemini_api_key)
    claude = ChatAnthropic(model_name="Claude-3-5-sonnet-20240620", anthropic_api_key=anthropic_api_key)
    search_tool = SerperDevTool()
    
    # Input fields
    company_name = st.text_input("What's the Company Name:")
    meeting_objective = st.text_input("What's the meeting Objective:")
    attendees = st.text_area("Enter the attendees and their roles, each per line:")
    meeting_duration = st.selectbox("What's the meeting duration [in minutes]:", options=[15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180])
    focus_areas = st.text_input("What are the specific areas of concern:")
    
    # defining agents
    context_analyzer = Agent(
        role="Meeting context specialist",
        goal="Analyze and Summarize key background information for the meeting",
        backstory="You are an expert at quickly understanding complex business concepts, contexts and identifying critical \
            and fundamental information that is to the meeting objective and focus areas",
        verbose=True,
        allow_delegation=False,
        llm=claude,
        tools=[search_tool]
    )
    
    industry_insights_generator = Agent(
        role="Industry Expert",
        goal="Provide in-depth industry training, analysis and identify potential and business oriented key trends with utmost agile reasoning",
        backstory="You are a seasoned industry expert with a knack of spotting emerging trends and opportunities.",
        verbose=True,
        allow_delegation=False,
        llm=ollama,
        tools=[search_tool]
    )
    
    strategy_formulator = Agent(
        role="meeting Strategist",
        goal="Develop a tailored meeting strategy and detailed agenda and the stipulated time",
        backstory="You are an expert at developing and planning highly effective and professional meeting strategies and detailed agenda and \
            the stipulated time",
        verbose=True,
        allow_delegation=False,
        llm=gemini_pro,
        tools=[search_tool]
    )
    
    executive_briefing_creator = Agent(
        role="Communications Specialist",
        goal="Synthesize information into concise and imapctful briefs",
        backstory="You are an expert communicator, skilled at distilling complex information into a clear and actionable insights",
        verbose=True,
        allow_delegation=False,
        llm=claude,
        tools=[search_tool]
    )
    
    # more Agents can be defined
    
    # Defining Tasks
    context_analysis_tasks = Task(
        descriptions=f"""
            Analyze the context for the meeting with {company_name}, considering:
            1. The meeting objective: {meeting_objective}
            2. The attendees: {attendees}
            3. The meeting duration: {meeting_duration} minutes
            4. The focus areas: {focus_areas}
            5. Specific focus areas or concerns: {focus_areas}
            
            Research {company_name} for key insights, including:
            1. Recent news
            2. key products/services
            3. key competitors
            4. key customers
            5. key market trends
            """,
        agent=context_analyzer
    )
    
    industry_analysis_tasks = Task(
        descriptions=f""" """,
        agent=industry_insights_generator
    )
    
    strategy_development_tasks = Task(
        description=f""" """,
        agent=strategy_formulator
    )
    
    executive_briefing_tasks = Task(
        description=f""" """,
        agent=executive_briefing_creator
    )
    
    # More Tasks can be defined!!
    
    ## The Crew
    jeyCrew = Crew(
        agents=[context_analyzer, industry_insights_generator, strategy_formulator, executive_briefing_creator],
        tasks=[context_analysis_tasks, industry_analysis_tasks, strategy_development_tasks, executive_briefing_tasks],
        verbose=True,
        manager_agent=context_analyzer,
        manager_llm=claude,
        process=Process.hierarchical
    )
    
    # About hierarchical processes -> https://docs.crewai.com/core-concepts/Processes/#hierarchical-process
    
# else:
#     raise Exception("The API keys are either faulty or mal-configured")

# Run the crew once the user clicks the button
if st.button("Prepare Meeting", disabled=not all(api_keys)):
    logging.info("Starting the meeting preparation for %s", company_name)
    
    with st.spinner("Jey is preparing your meeting..."):
        try:
            result = jeyCrew.kickoff() # kicksoff the crew process
            st.markdown(result) # displays the result in a markdown format
        except Exception as e:
            logging.error(f"Error occured: {str(e)}")
            st.error(f"An eror occured when preparing the meeting: {str(e)}")
        
# How to use app instructions
st.sidebar.markdown(
    """
    ## How to use Jey:
    1. Enter your API keys (e.g. Your Claude API Key).
    2. Provide Meeting details:
       - **Company Name**: Name of the company (e.g., "Tech Corp").
       - **Meeting Objective**: Purpose of the meeting (e.g., "Discuss Q3 goals").
       - **Attendees**: List of attendees with roles (one per line).
       - **Meeting Duration**: Duration in minutes (e.g., "60").
       - **Focus Areas**: Specific concerns (e.g., "Budget allocation").
    3. Click 'Prepare Meeting' to generate a preparation package.
    
    Jey will:
    - Analyze the meeting context.
    - Provide industry insights.
    - Develop a strategy.
    - Create an executive brief.
    
    This could take a few minutes.
    """
)