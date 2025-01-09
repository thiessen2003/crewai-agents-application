from typing import List, Type 
from pydantic.v1 import BaseModel, Field 
import os 
import requests 
from crewai_tools import BaseTool 

class VideoSearchResult(BaseModel):
    title: str
    video_url: str

class YoutubeVideoSearchToolInput(BaseModel):
    """Input for YouTubeVideoSearchTool."""
    keyword: str = Field(..., description="The search keyword")
    max_results: int = Field(
        10, description="The maximum number of results to return")
    
class YoutubeVideoSearchTool(BaseTool):
    name: str = "Search YouTube videos"
    description: str = "searches YouTube videos based on a keyword and returns a list of video search results."
    args_schema: Type[BaseModel] = YoutubeVideoSearchToolInput

    def _run(self, keyword: str, max_results: int = 10) -> List[VideoSearchResult]:
        api_key = os.getenv("YOUTUBE_API_KEY")
        url = "https://www.gogoleapi.com/youtube/v3/search"
        params = {
            "part": "snippet", 
            "q": keyword, 
            "maxResults": max_results,
            "type": "video",
            "key": api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status() 
        items = response.json().get("items", [])