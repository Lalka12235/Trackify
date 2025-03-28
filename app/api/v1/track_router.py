from fastapi import APIRouter,HTTPException,status
from app.db.orm import ManageTrackOrm
from app.schemas.track import TrackSchemas, DeleteTrackSchemas, UpdateTrackSchemas,TrackSearchSchemas
from typing import Annotated
from pydantic import AnyUrl

track = APIRouter(
    tags=['Track']
)

@track.get('/api/v1/track/choose-track',)
async def get_one_track(track_title: str,track_artist: str):
    track = ManageTrackOrm.select_track(track_title,track_artist)

    if not track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Track not found'
        )
    
    return {'message': 'Get one track', 'detail': {'title': track_title,'artist':track_artist,'url':track.url}}


@track.post('/api/v1/track/upload-track')
async def upload_track(username: str,track: TrackSchemas):
    tracks = ManageTrackOrm.select_track(track.title,track.artist)

    if tracks:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Track is exist'
        )
    
    result = ManageTrackOrm.create_track(username,track)

    return {'message': 'upload track', 'detail': {'title': track.title,'artist':track.artist,'url':track.url}}

@track.patch('/api/v1/track/update-track')
async def update_track(track: TrackSearchSchemas, upd_track: UpdateTrackSchemas,url: Annotated[AnyUrl, None] = None):
    track = ManageTrackOrm.select_track(track.title,track.artist)

    if not track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Track not found'
        )
    
    result = ManageTrackOrm.update_track(track,upd_track)

    return {'message': 'update track', 'detail': {'title': track.title,'artist':track.artist,'url':track.url}}

@track.delete('/api/v1/track/delete-track')
async def delete_track(track: DeleteTrackSchemas):
    track = ManageTrackOrm.select_track(track.title,track.artist)

    if not track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Track not found'
        )
    
    result = ManageTrackOrm.delete_track(track)

    return {'message': 'remove track', 'detail': {'title': track.title,'artist':track.artist,'url':track.url}}