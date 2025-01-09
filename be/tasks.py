from crewai import Task, Agent
from textwrap import dedent
from models import PositionInfoList, PositionInfo


class CompanyResearchTasks():
    def __init__ (self, job_id: str): 
        self.job_id = job_id

    def manage_research(self, agent: Agent, companies: list[str], positions: list[str], tasks: list[Task]): #list of tasks is passed into context, which is basically tasks that are passed to other tasks
        return Task(
            description=dedent(f"""Based on the list of companies {companies} and the positions {positions},
            use the results from the Company Research Agent to research each position in each company to put 
            together a JSON object containing the URLs for 3 blog articles, the URLs and title for 3 YouTube interviews for each position 
            each company. 
            """),
            agent=agent, 
            expected_output=dedent(
                """A JSON object containing the URLs for 3 blog article and the URLs and titles 
                for 3 YouTube interviews for each position in each company. """
            ), 
            callback=self.append_event_callback,
            context=tasks, 
            output_json=PositionInfoList
        )

    def company_research(self, agent: Agent, company: str, positions: list[str]): 
        return Task(
            description=dedent(f"""Research the position {positions} for the {company} company.
                For each position, find the URLs for 3 recent blog articles and the URLs and titles for
                3 recent YouTube interviews for the person in each positio.
                Return this collected information in a JSON object. 

                Helpful tips: 
                - To find the blog articles names and URLs, perform searches on Google such like the following: 
                    - "{company} [POSITION HERE] blog articles"
                - To find the YouTube interviews, perform searches on YouTube such as the following: 
                    - "{company} [POSITION HERE] interview"             

                Important: 
                - Once you have found the information, immediately stop searching for additional information. 
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information for each position in the company. 
                """),
                agent=agent, 
                expected_output="""A JSON object containing the researched information for each position in the company.""",
                callback=self.append_event_callback, 
                output_json=PositionInfo,
                async_execution=True
                

        )

