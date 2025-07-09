from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.track_model import TrackModel
    from app.models.playlist_model import PlaylistModel


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]

    tracks: Mapped[list['TrackModel']] = relationship(back_populates='user')
    playlists: Mapped[list['PlaylistModel']] = relationship(back_populates='user')