from fastapi import FastAPI
from app.api.v1.playlist_router import playlist
from app.api.v1.track_router import track
from app.api.v1.user_router import user
from app.auth.auth import auth
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title='Trackify',
    description='Trackify is a convenient application for managing your music collection that allows you to add, \
        update, and delete tracks and playlists. Save your favorite tracks, create personalized playlists, and share them with friends.',
        version='1.0',
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080/docs",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],
)


app.include_router(user)
app.include_router(track)
app.include_router(playlist)
app.include_router(auth)