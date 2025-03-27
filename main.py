from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title='Music Tracker',
    description='API for add/update/delete track and playlist'
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