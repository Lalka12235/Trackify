from sqlalchemy import select,insert,update,delete
from app.db.session import Session
from app.db.models import UserModel, TrackModel, PlaylistModel, PlaylistTrackModel
from app.schemas.track import TrackSchemas, PlaylistTrackSchemas, UpdateTrackSchemas,DeleteTrackSchemas
from app.schemas.user import UserSchemas, UserOutSchemas
from fastapi import HTTPException,status


class UserOrm:

    @staticmethod
    def select_user(username) -> UserOutSchemas:
        with Session() as session:
            stmt = select(UserModel).where(UserModel.username == username)
            result = session.execute(stmt)
            if result:
                return {'User': 'exist'}
            else:
                return {'User': 'Doesnt exist'}

    @staticmethod
    def register_user(user: UserSchemas) -> UserOutSchemas:
        with Session() as session:
            users = UserOrm.select_user(user.username)

            if users:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Users is exist'
                )
            
            stmt = insert(UserOrm).values(username=user.username,password=user.password)
            result = session.execute(stmt)

            session.commit()
            return {'Create': True}
        
    @staticmethod
    def delete_user(user: UserSchemas) -> any:
        with Session() as session:
            users = UserOrm.select_user(user.username)

            if not users:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Users isn"t exist'
                )
            
            stmt = delete(UserModel).where(username=user.username,password=user.password)
            result = session.execute(stmt)

            session.commit()
            return {'Delete': True}
        

class ManageTrackOrm:

    #all track artist add

    @staticmethod
    def select_track(track: TrackSchemas):
        with Session() as session:
            exist_track = select(TrackModel).where(title=track.title,artist=track.artist,url=track.url)

            if not exist_track:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Track not found'
                )
            
            return {'Select': True,'Track': exist_track}
        
    @staticmethod
    def create_track(track: TrackSchemas):
        with Session() as session:
            exist_track = select(TrackModel).where(title=track.title,artist=track.artist,url=track.url)

            if exist_track:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Track is exist'
                )
            
            new_track = TrackModel(
                title=track.title,
                artist=track.artist,
                genre=track.genre,
            )

            stmt = insert(TrackModel).values(title=track.title,artist=track.artist,genre=track.genre,url=track.url)
            result = session.execute(stmt)

            session.commit()
            return {'Create': True,'Track': result}
        
    
    @staticmethod
    def update_track(track: UpdateTrackSchemas):
        with Session() as session:
            exist_track = select(TrackModel).where(title=track.title,artist=track.artist,url=track.url)

            if not exist_track:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Track not found'
                )
            
            stmt = update(TrackModel).where(
                title=track.title,
                artist=track.artist,
                #genre
            )
            result = session.execute(stmt)

            session.commit()
            return {'Update': True,'Track update': result}
        
    @staticmethod
    def delete_track(track: DeleteTrackSchemas):
        with Session() as session:
            exist_track = select(TrackModel).where(title=track.title,artist=track.artist,url=track.url)

            if not exist_track:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Track not found'
                )
            
            stmt = delete(TrackModel).where(
                title=track.title,
                artist=track.artist,
                url=track.url
            )

            result = session.execute(stmt)

            return {'Delete': True, 'Track': result}
        

class ManagePlaylistOrm:

    @staticmethod
    def select_playlist(playlist_title: str):
        with Session() as session:
            stmt = select(PlaylistModel).where(name=playlist_title)
            result = session.execute(stmt)

            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Playlist doesnt exist'
                )
            return {'Playlist': result}

    @staticmethod
    def create_playlist(playlist_title: str):
        with Session() as session:
            try:
                playlists = ManagePlaylistOrm.select_playlist(playlist_title)
                if playlists:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail='Playlist is exist'
                    )
                stmt = insert(PlaylistModel).values(name=playlist_title)
                result = session.execute(stmt)

                session.commit()
                return {'Playlist': True,'Detail': result}
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Something wrong'
                )
            
    @staticmethod
    def update_playlist(playlist_title: str, new_title: str):
        with Session() as session:
            playlists = ManagePlaylistOrm.select_playlist(playlist_title)

            if not playlists:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Playlist not found'
                )
            
            stmt = update(PlaylistModel).where(name=new_title)
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
            
            stmt = delete(PlaylistModel).where(name=playlist_title)
            result = session.execute(stmt)

            session.commit()
            return {'Update': True,'Detail': result}
        

class ManagePlaylistTrackOrm:

    @staticmethod
    