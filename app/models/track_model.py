from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey
from app.models.base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.user_model import UserModel
    from app.models.playlist_model import PlaylistTrackModel

class TrackModel(Base):
    __tablename__ = 'tracks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    artist: Mapped[str]
    genre: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    url: Mapped[str]

    user: Mapped['UserModel'] = relationship(back_populates='tracks')
    playlists: Mapped[list['PlaylistTrackModel']]= relationship(back_populates='track')
