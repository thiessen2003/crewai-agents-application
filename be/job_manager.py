from dataclasses import dataclass 
from typing import List, Dict 
from datetime import datetime

@dataclass
class Event: 
    timestamp: datetime 
    message: str

@dataclass #create methods like hash automatically for a class 
class Job: 
    status: str
    events: List[Event]
    result: str

def append_event(job_id: str, event_data: str):
    