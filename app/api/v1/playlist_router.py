from fastapi import APIRouter,HTTPException,status
from app.db.orm import UserOrm,ManageTrackOrm,ManagePlaylistOrm
from app.schemas.track import TrackMinSchemas, TrackSchemas, DeleteTrackSchemas, UpdateTrackSchemas,TrackSearchSchemas, PlaylistSchemas
from app.schemas.user import UserSchemas

playlist = APIRouter(
    tags=['Playlist']
)

@playlist.get('/api/v1/playlist/choose-playlist')
async def get_playlist(playlist_title: str):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist not found'
        )
    
    return {'message': 'get playlist','detail': {'title': playlist_title,}}

@playlist.post('/api/v1/playlist/create-playlist',tags=['Playlist'])
async def create_playlist(username: str,playlist_title: str):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    if playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist exist'
        )
    
    result = ManagePlaylistOrm.create_playlist(username,playlist_title)

    return {'message': 'create playlist','detail': {'title': playlist_title}}

@playlist.patch('/api/v1/playlist/update-playlist',tags=['Playlist'])
async def update_playlist(playlist_title: str, new_title: str):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist not found'
        )
    
    result = ManagePlaylistOrm.update_playlist(playlist_title,new_title)

    return {'message': 'update playlist','detail': {'old_title': playlist_title,'new_title': new_title}}

@playlist.delete('/api/v1/playlist/delete-playlist',tags=['Playlist'])
async def delete_playlist(playlist_title: str):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist not found'
        )
    
    result = ManagePlaylistOrm.delete_playlist(playlist_title)

    return {'message': 'delete playlist','detail': {'title': playlist_title}}


@playlist.post('/api/v1/playlist/add-track',tags=['Playlist'])
async def add_track_to_playlist(playlist_title: str,track: TrackSearchSchemas):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)
    result = ManagePlaylistOrm.add_track_to_playlist(playlist_title,track)

    return {'message': 'add track to playlist','detail': {'playlist':playlist_title,'title_track': track.title,'artist_track': track.artist}}


@playlist.delete('/api/v1/playlist/delete-track',tags=['Playlist'])
async def delete_track_from_playlist(playlist_title: str,track: TrackSearchSchemas):
    result = ManagePlaylistOrm.delete_track_from_playlist(playlist_title,track)

    return {'message': 'delete track from playlist','detail': {'playlist':playlist_title,'title_track': track.title,'artist_track': track.artist}}

@playlist.get('/api/v1/playlist/all-track',tags=['Playlist'])
async def get_all_track_from_playlist(playlist_title: str):
    result = ManagePlaylistOrm.get_all_track_from_playlist(playlist_title)


    tracks = [{
        'id': track.id,
        'title': track.title,
        'artist': track.artist,
        'genre': track.genre,
        'url': track.url
    } for track in result['tracks']]

    return {'playlist': result['playlist'], 'tracks': tracks}