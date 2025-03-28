from fastapi import FastAPI
from app.api.v1.router import router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


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

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app',host='127.0.0.1', port=8000,reload=True)