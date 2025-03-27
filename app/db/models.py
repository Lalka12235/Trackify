from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase,relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]

    tracks: Mapped[list['TrackModel']] = relationship(back_populates='user')
    playlists: Mapped[list['PlaylistModel']] = relationship(back_populates='user')


class TrackModel(Base):
    __tablename__ = 'tracks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    artist: Mapped[str]
    genre: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    url: Mapped[str]

    user: Mapped['UserModel'] = relationship(back_populates='tracks')
    playlist = relationship('PlaylistTrackModel',back_populates='track')

class PlaylistModel(Base):
    __tablename__ = 'playlists'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['UserModel'] = relationship(back_populates='playlists')
    tracks = relationship('PlaylistTrackModel', back_populates='playlist')

class PlaylistTrackModel(Base):
    __tablename__ = 'playlists-tracks'

    id: Mapped[int] = mapped_column(primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey('tracks.id'))

    playlist = relationship('PlaylistModel',back_populates='tracks')
    track = relationship('TrackModel',back_populates='playlists')