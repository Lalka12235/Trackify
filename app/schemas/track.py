from pydantic import BaseModel


class TrackSchemas(BaseModel):
    title: str
    artist: str
    genre: str
    url: str

class TrackMinSchemas(BaseModel):
    title: str
    artist: str
    url: str

class UpdateTrackSchemas(BaseModel):
    title:str 
    artist:str 
    genre:str  

class DeleteTrackSchemas(BaseModel):
    title:str
    artist:str


class TrackSearchSchemas(BaseModel):
    title: str
    artist: str
