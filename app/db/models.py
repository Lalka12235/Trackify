from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase,relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass


class UserOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]

    tracks: Mapped[list['TrackOrm']] = relationship(back_populates='user')
    playlists: Mapped[list['PlaylistOrm']] = relationship(back_populates='user')


class TrackOrm(Base):
    __tablename__ = 'tracks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    artist: Mapped[str]
    genre: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['UserOrm'] = relationship(back_populates='tracks')
    playlist = relationship('PlaylistTrackOrm',back_populates='track')

class PlaylistOrm(Base):
    __tablename__ = 'playlists'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['UserOrm'] = relationship(back_populates='playlists')
    tracks = relationship('PlaylistRrackOrm', back_populates='playlist')

class PlaylistTrackOrm(Base):
    __tablename__ = 'playlists-tracks'

    id: Mapped[int] = mapped_column(primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey('tracks.id'))

    playlist = relationship('PlaylistOrm',back_populates='tracks')
    track = relationship('TrackOrm',back_populates='playlists')