from fastapi import APIRouter,HTTPException,status
from app.db.orm import UserOrm,ManageTrackOrm,ManagePlaylistOrm
from app.schemas.track import TrackMinSchemas, TrackSchemas, DeleteTrackSchemas, UpdateTrackSchemas
from app.schemas.user import UserSchemas,UserOutSchemas

router = APIRouter()

@router.post('/api/v1/user/register', tags=['User'])
async def create_user(user: UserSchemas) ->  UserOutSchemas:
    user = UserOrm.select_user(user.username)

    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User is exist'
        )
    
    result = UserOrm.register_user(user)

    return {'message': 'Users successfull create', 'detail': result}

@router.delete('/api/v1/user/delete', tags=['User'])
async def delete_user(user: UserSchemas):
    user = UserOrm.select_user(user.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User doesnt exist'
        )
    
    result = UserOrm.delete_user(user)

    return {'message': 'User delete', 'detail': result}


@router.get('/api/v1/track/choose-track',tags=['Track'])
async def get_one_track(track_title: str,track_artist: str, track_url: str):
    track = ManageTrackOrm.select_track(track_title,track_artist,track_url)

    if not track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Track not found'
        )
    
    return {'message': 'Get one track', 'detail': {'title': track_title,'artist':track_artist,'url':track_url}}


@router.post('/api/v1/track/upload-track',tags=['Track'])
async def upload_track(track: TrackSchemas):
    track = ManageTrackOrm.select_track(track.title,track.artist,track.url)

    if track:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Track is exist'
        )
    
    result = ManageTrackOrm.create_track(track)

    return {'message': 'upload track', 'detail': {'title': track.title,'artist':track.artist,'url':track.url}}

@router.patch('/api/v1/track/update-track',tags=['Track'])
async def update_track(track: UpdateTrackSchemas):
    track = ManageTrackOrm.select_track(track.title,track.artist,track.url)

    if not track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Track not found'
        )
    
    result = ManageTrackOrm.update_track(track)

    return {'message': 'update track', 'detail': {'title': track.title,'artist':track.artist,'url':track.url}}

@router.delete('/api/v1/track/delete-track',tags=['Track'])
async def delete_track(track: DeleteTrackSchemas):
    track = ManageTrackOrm.select_track(track.title,track.artist,track.url)

    if not track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Track not found'
        )
    
    result = ManageTrackOrm.delete_track(track)

    return {'message': 'remove track', 'detail': {'title': track.title,'artist':track.artist,'url':track.url}}


@router.get('/api/v1/playlist/choose-playlist',tags=['Playlist'])
async def get_playlist(playlist_title: str):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist not found'
        )
    
    return {'message': 'get playlist','detail': {'title': playlist_title,}}

@router.post('/api/v1/playlist/create-playlist',tags=['Playlist'])
async def create_playlist(playlist_title: str):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    if playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist exist'
        )
    
    result = ManagePlaylistOrm.create_playlist(playlist_title)

    return {'message': 'create playlist','detail': {'title': playlist_title,}}

@router.patch('/api/v1/playlist/update-playlist',tags=['Playlist'])
async def update_playlist(playlist_title: str, new_title: str):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist not found'
        )
    
    result = ManagePlaylistOrm.update_playlist(playlist_title,new_title)

    return {'message': 'create playlist','detail': {'old_title': playlist_title,'new_title': new_title}}

@router.delete('/api/v1/playlist/delete-playlist',tags=['Playlist'])
async def delete_playlist(playlist_title: str):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist not found'
        )
    
    result = ManagePlaylistOrm.delete_playlist(playlist_title)

    return {'message': 'create playlist','detail': {'title': playlist_title,'remover': True}}


@router.post('/api/v1/playlist/add-track',tags=['Playlist'])
async def add_track_to_playlist(playlist_title: str,track: TrackMinSchemas):
    playlist = ManagePlaylistOrm.select_playlist(playlist_title)

    #if not playlist:
    #    raise HTTPException(
    #        status_code=status.HTTP_404_NOT_FOUND,
    #        detail='Playlist not found'
    #    )
#
    #track = ManageTrackOrm.select_track(track.title,track.artist,track.url)
    #if not track:
    #    raise HTTPException(
    #        status_code=status.HTTP_404_NOT_FOUND,
    #        detail='Track not found'
    #    )
    
    result = ManagePlaylistOrm.add_track_to_playlist(playlist_title,track)

    return {'message': 'add track to playlist','detail': {'playlist':playlist_title,'title_track': track.title,'artist_track': track.artist,'url_track': track.url}}


@router.delete('/api/v1/playlist/delete-track',tags=['Playlist'])
async def delete_track_from_playlist(playlist_title: str,track: TrackMinSchemas):
    result = ManagePlaylistOrm.delete_track_from_playlist(playlist_title,track)

    return {'message': 'delete track from playlist','detail': {'playlist':playlist_title,'title_track': track.title,'artist_track': track.artist,'url_track': track.url}}

@router.get('/api/v1/playlist/all-track',tags=['Playlist'])
async def get_all_track_from_playlist(playlist_title: str):
    result = ManagePlaylistOrm.get_all_track_from_playlist(playlist_title)

    return result