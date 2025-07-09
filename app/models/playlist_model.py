from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.track_model import TrackModel
    from app.models.playlist_model import PlaylistModel, PlaylistTrackModel
    from app.models.user_model import UserModel


class PlaylistModel(Base):
    __tablename__ = 'playlists'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['UserModel'] = relationship(back_populates='playlists')
    tracks: Mapped[list['PlaylistTrackModel']] = relationship(back_populates='playlist')
class PlaylistTrackModel(Base):
    __tablename__ = 'playlists-tracks'

    id: Mapped[int] = mapped_column(primary_key=True)
    playlist_id: Mapped[int] = mapped_column(ForeignKey('playlists.id'))
    track_id: Mapped[int] = mapped_column(ForeignKey('tracks.id'))
    

    playlist: Mapped['PlaylistModel'] = relationship(back_populates='tracks')
    track: Mapped['TrackModel'] = relationship(back_populates='playlists')