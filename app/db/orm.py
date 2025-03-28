from sqlalchemy import select,insert,update,delete
from app.db.session import Session
from app.db.models import UserModel, TrackModel, PlaylistModel, PlaylistTrackModel
from app.schemas.track import TrackSchemas,UpdateTrackSchemas,DeleteTrackSchemas, TrackMinSchemas,TrackSearchSchemas, PlaylistSchemas
from app.schemas.user import UserSchemas
from fastapi import HTTPException,status
from app.services.hash import make_hash_pass,verify_pass


class UserOrm:

    @staticmethod
    def select_user(username: str):
        with Session() as session:
            stmt = select(UserModel).where(UserModel.username == username)
            user = session.execute(stmt).scalar_one_or_none()
            return user

    @staticmethod
    def register_user(username: str,password: str):
        with Session() as session:
            users = UserOrm.select_user(username)
            hash_pass = make_hash_pass(password)

            if users:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Users is exist'
                )
            
            stmt = insert(UserModel).values(username=username,password=hash_pass)
            result = session.execute(stmt).scalar()

            session.commit()
            return {'message': 'User create'}
        
    @staticmethod
    def delete_user(user: UserSchemas):
        with Session() as session:
            users = UserOrm.select_user(user.username)

            if not users:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Users isn"t exist'
                )
            
            stmt = delete(UserModel).where(UserModel.username==user.username,UserModel.password==user.password)
            result = session.execute(stmt)

            session.commit()
            return 
        

class ManageTrackOrm:

    #all track artist add

    @staticmethod
    def get_all_track_artist(track_artist: str):
        with Session() as session:
            exist_artist = select(
                TrackModel.title,
                TrackModel.artist,
                TrackModel.genre,
                TrackModel.url,
                ).where(TrackModel.artist == track_artist)

            if not exist_artist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Arist not found'
                )
            
            result = session.execute(exist_artist)

            return {'message': 'Get all track artist','detail': result}

    @staticmethod
    def select_track(track_title: str,track_artist: str):
        with Session() as session:
            stmt = select(TrackModel).where(
                TrackModel.title==track_title,
                TrackModel.artist==track_artist,
                )
            
            exist_track = session.execute(stmt).scalar_one_or_none()

            return exist_track
            
            
        
    @staticmethod
    def create_track(username: str,track: TrackSchemas):
        with Session() as session:
            user = UserOrm.select_user(username)
            exist_track = ManageTrackOrm.select_track(track.title,track.artist)


            if exist_track:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Track is exist'
                )
            
            new_track = TrackModel(
                title=track.title,
                artist=track.artist,
                genre=track.genre,
                user_id=user.id,
                url=track.url
            )

            session.add(new_track)
            session.commit()
            return {'Create': True,'detail': {'title': track.title,'artist':track.artist,'url':track.url} }
        
    
    @staticmethod
    def update_track(track: TrackSearchSchemas, upd_track: UpdateTrackSchemas):
        with Session() as session:
            exist_track = ManageTrackOrm.select_track(track.title,track.artist)
  
            if not exist_track:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Track not found'
                )
            
            stmt = update(TrackModel).where(
                TrackModel.title==track.title,
                TrackModel.artist==track.artist,
            ).values(
                title=upd_track.title,
                artist=upd_track.artist,
                genre=upd_track.genre
            )
            result = session.execute(stmt)

            session.commit()
            return {'Update': True,'Track update': result}
        
    @staticmethod
    def delete_track(track: DeleteTrackSchemas):
        with Session() as session:
            stmt1 = select(TrackModel).where(
                TrackModel.title==track.title,
                TrackModel.artist==track.artist,
                )
            
            exist_track = session.execute(stmt1).scalar_one_or_none()

            if not exist_track:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Track not found'
                )
            
            stmt = delete(TrackModel).where(
                TrackModel.title==track.title,
                TrackModel.artist==track.artist,
            )

            result = session.execute(stmt)
            session.commit()

            return {'Delete': True, 'Track': result}
        

class ManagePlaylistOrm:

    @staticmethod
    def select_playlist(playlist_title: str):
        with Session() as session:
            stmt = select(PlaylistModel).where(PlaylistModel.name==playlist_title)
            result = session.execute(stmt).scalar_one_or_none()
            return result

    @staticmethod
    def create_playlist(username: str,playlist_title: str):
        with Session() as session:
            playlists = ManagePlaylistOrm.select_playlist(playlist_title)
            user = UserOrm.select_user(username)

            if playlists:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Playlist is exist'
                )

            stmt = insert(PlaylistModel).values(name=playlist_title,user_id=user.id)
            result = session.execute(stmt)
            session.commit()

            return {'Playlist': True,'Detail': result}
            
    @staticmethod
    def update_playlist(playlist_title: str, new_title: str):
        with Session() as session:
            playlists = ManagePlaylistOrm.select_playlist(playlist_title)

            if not playlists:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Playlist not found'
                )
            
            stmt = update(PlaylistModel).values(name=new_title).where(PlaylistModel.name==playlist_title)
            result = session.execute(stmt)

            session.commit()
            return {'Update': True,'Detail': result}
        
    @staticmethod
    def delete_playlist(playlist_title: str):
        with Session() as session:
            playlists = ManagePlaylistOrm.select_playlist(playlist_title)

            if not playlists:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Playlist not found'
                )
            
            stmt = delete(PlaylistModel).where(PlaylistModel.name==playlist_title)
            result = session.execute(stmt)

            session.commit()
            return {'Update': True,'Detail': result}

    @staticmethod
    def add_track_to_playlist(playlist_title: str,track: TrackSearchSchemas):
        with Session() as session:
            playlist = ManagePlaylistOrm.select_playlist(playlist_title)

            if not playlist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Playlist not found'
                )
            
            track = ManageTrackOrm.select_track(track.title,track.artist)

            if not track:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Track not found'
                )
            
            stmt = insert(PlaylistTrackModel).values(playlist_id=playlist.id,track_id=track.id)
            session.execute(stmt)
            session.commit()

            return {'message': 'Track added to playlist',}


    
    @staticmethod
    def delete_track_from_playlist(playlist_title: str,track: TrackSearchSchemas):
        with Session() as session:
            playlist = ManagePlaylistOrm.select_playlist(playlist_title)

            if not playlist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Playlist not found'
                )
            
            track = ManageTrackOrm.select_track(track.title,track.artist)

            if not track:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Track not found'
                )
            
            stmt = delete(PlaylistTrackModel).where(
                PlaylistTrackModel.playlist_id == playlist.id,
                PlaylistTrackModel.track_id == track.id
            )
            session.execute(stmt)
            session.commit()

            return {'message': 'Track removed from playlist'}



    @staticmethod
    def get_all_track_from_playlist(playlist_title: str):
        with Session() as session:
            playlist = ManagePlaylistOrm.select_playlist(playlist_title)

            if not playlist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Playlist not found'
                )
            
            stmt = select(TrackModel).join(PlaylistTrackModel).where(PlaylistTrackModel.playlist_id == playlist.id)
            tracks = session.execute(stmt).scalars().all()

            if not tracks:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Tracks not found'
                )
            
            return {'playlist': playlist_title, 'tracks': tracks}
