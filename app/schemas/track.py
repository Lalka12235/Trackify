from pydantic import BaseModel, AnyUrl


class TrackSchemas(BaseModel):
    title: str
    artist: str
    genre: str
    user_id: str
    url: AnyUrl

class UpdateTrackSchemas(BaseModel):
    title:str
    artist:str
    genre:str
    url:str

class DeleteTrackSchemas(BaseModel):
    title:str
    artist:str
    url:str


class PlaylistTrackSchemas(BaseModel):
    pass