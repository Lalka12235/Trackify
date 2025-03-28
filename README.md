# 🎵 Trackify


Trackify is a convenient application for managing your music collection that allows you to add, update, and delete tracks and playlists. Save your favorite tracks, create personalized playlists, and share them with friends.

## 🛠 Tech Stack

- **Backend**: Python (FastAPI)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Containerization**: Docker
- **Authentication**: JWT

## 🚀 Installation & Setup

### Local Installation

```bash
# 1. Clone repository
git clone https://github.com/yourusername/trackify.git
cd trackify

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt
Docker Setup
bash
Copy
# Build images
docker-compose build

# Start containers
docker-compose up
The application will be available at: http://localhost:8000

🔐 Authentication
JWT authentication is required to work with the API.

Register
POST /api/v1/auth/register

Request: json


{
  "username": "your_username",
  "password": "your_password"
}

Response: json


{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
Login
POST /api/v1/auth/login

Request: json


{
  "username": "your_username",
  "password": "your_password"
}

Response: Same as registration

🎧 Track Management
Get Track
GET /api/v1/track/choose-track

Parameters:

username (string)

track_title (string)

track_artist (string)

Response: json


{
  "message": "Get one track",
  "detail": {
    "title": "track_title",
    "artist": "track_artist",
    "url": "track_url"
  }
}


Upload Track
POST /api/v1/track/upload-track

Request: json


{
  "title": "track_title",
  "artist": "track_artist",
  "url": "track_url"
}


📂 Playlist Management
Create Playlist
POST /api/v1/playlist/create-playlist

Request: json


{
  "title": "playlist_title"
}
Response: json


{
  "message": "create playlist",
  "detail": {
    "title": "playlist_title"
  }
}

📌 Additional Information
API Documentation http://127.0.0.1:8000/docs#/


 ```
<div align="center"> <sub>Built with ❤️ for music lovers</sub> </div>
