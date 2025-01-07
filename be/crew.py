class CompanyResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.crew = None

    def setup_crew(self, companies: list[str], positions: list[str]):
        print(
            f"Setting up crew for {self.job_id} with companies {companies} and positions {positions}"
        )

    
    def kickoff_crew(self):
        if not self.crew:
            print(f"No crew found for {self.job_id}")
            return 
        
        try: 
            print(f"Running crew for {self.job_id}")
            results = self.crew.kickoff()
            return results
        except Exception as e:
            return str(e)
