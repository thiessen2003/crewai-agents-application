class CompanyResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id

    def setup_crew(self, companies: list[str], positions: list[str]):
        print(
            f"Setting up crew for {self.job_id} with companies {companies} and positions {positions}"
        )

    
    def kickoff_crew(self):
        