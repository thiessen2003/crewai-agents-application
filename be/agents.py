from crewai import Agent
import google.generativeai as genai
from dotenv import load_dotenv
import os 

load_dotenv()


class CompanyResearchAgents(): 
    def __init__(self, company):
        print("Setting up agents for company research")
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.llm = genai.GenerativeModel("gemini-1.5-flash")
    
    def research_manager(self, companies: list[str], positions: list[str]) -> Agent: 
        return Agent(
            role="Company Research Manager", 
            goal=f"""Generate a list of JSON objects containing the urls for 3 recent blog articles and 
            the url and title for 3 recent YouTube interview, for each position in each compny.
            
            Companies: {companies}
            Positions: {positions}
            
            Important: 
            - The final list of JSON objects must include all companies and positions. Do not leave any out 
            - If you can't find information for a specific position, fill in the information with the word "MISSING".
            - Do not generate fake information. Only return the information you find. Nothing else! 
            - Do not stop researching until you find the requested information for each position in each company. 
            - All the companies and positions exist so keep research until you find the information for each one. 
            - Make sure you each researched position for each copany contains 3 blog articles and 3 YouTube interviews 
            """,
            backstory="""As a company research maanger, you are responsible for aggregating all the researched information into a list.""",
            llm=self.llm,
            tools=[self.searchInternetTool, self.youtubeSearchTool],
            verbose=True, 
            allow_delegation=True
        )
    
    def company_research_agent(self) -> Agent: 
        return Agent(
            role="Company Research Agent", 
            goal=f"""Look up the specific positions for a given company and find urls for 3 recent blog articles and 
            the url and title for 3 recent YouTube interviews for each person in the specified positions. It is your kob to return this collection of 
            information in a JSON object  
            """,
            backstory="""As a company research agent, you are responsible for looking up specific positions 
            within a company and gathering relevant information.
            
            Important: 
            - Once you have found the information, immediately stop searching for additional information. 
            - Only return the requested information. NOTHING ELSE!
            - Make sure you find the persons name who holds the position. 
            - Do not generate fake information. Only return the information you find. Nothing else!
            
            """,
            llm=self.llm,
            tools=[self.searchInternetTool, self.youtubeSearchTool],
            verbose=True, 
        )
    