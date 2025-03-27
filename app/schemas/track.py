from pydantic import BaseModel, AnyUrl


class TrackSchemas(BaseModel):
    title: str
    artist: str
    genre: str
    url: AnyUrl

class TrackMinSchemas(BaseModel):
    title: str
    artist: str
    url: str

class UpdateTrackSchemas(BaseModel):
    title:str
    artist:str
    genre:str
    url:str

class DeleteTrackSchemas(BaseModel):
    title:str
    artist:str
    url:str

