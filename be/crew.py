from job_manager import append_event
from agents import CompanyResearchAgents
from tasks import CompanyResearchTasks
from crewai import Crew

class CompanyResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.crew = None

    def setup_crew(self, companies: list[str], positions: list[str]):
        print(
            f"Setting up crew for {self.job_id} with companies {companies} and positions {positions}"
        )

        #SETUP AGENTS 
        agents = CompanyResearchAgents()
        research_manager = agents.research_manager(companies, positions)
        company_research_agent = agents.company_research_agent()

        #SETUP TASKS 
        tasks = CompanyResearchTasks()
        company_research_tasks = [
            #for every company, we are creating a task
            tasks.company_research(company_research_agent, company, positions) for company in companies
        ]
        
        #this agent aggregates all the data
        maange_research = tasks.manage_research(research_manager, companies, positions, company_research_tasks)
        

        #CREATE CREW
        self.crew = Crew(
            agents=[research_manager, company_research_agent],
            #spreads the list; for instance, in this case where you are passing the list as the parameter, it will only have the elements of the list 
            #in the specified list; meaning that it avoids creating a list of lists
            tasks=[*company_research_tasks, maange_research],
            verbose=2
        )

    
    def kickoff_crew(self):
        if not self.crew:
            print(f"No crew found for {self.job_id}")
            return 
        
        append_event(self.job_id, "Crew started")
        try: 
            print(f"Running crew for {self.job_id}")
            results = self.crew.kickoff()
            append_event(self.job_id, "Crew completed")
            return results
        except Exception as e:
            append_event(self.job_id, str(e))
            return str(e)
