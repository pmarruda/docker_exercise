# Game Cataloguer
Game Cataloguer is a web application made for a docker training exercise that allows users to browse and manage a catalog of games, including adding games to their wishlist.

## Features
- User authentication (login and signup)
- Browse games
- Add games to wishlist
- View wishlist
- Compare games (not implemented)
- Get recommendations based on previously liked games (not implemented)

## Project Structure
```
.
├── .docker/
├── scripts/
│   └── init_db.sql
├── source/
│   ├── Backend/
│   └── Frontend/
└── README.md
```       
  
## Pre-requisites

- Docker & Docker-compose  
#### Alternatively
- Node.js version 14 or higher
- Python 3.10 or higher
- PostgreSQL
- Docker


## Getting Started

### Clone the Repository

To get started, clone the repository using the following command:

```bash
git clone <repository-url>
```

### Starting the Project with Docker Compose
1. Navigate to the `.docker` directory:

```bash 
cd .docker 
```

2. Start the services using `docker-compose`:

```bash 
docker-compose up --build 
```

Open your browser and navigate to `http://localhost` to access the application.

## Alternative Setup
### Refer to the individual README files for individual setup instructions:
- Backend and DB: [Backend/README.md](source/Backend/README.md)
- Frontend: [Frontend/README.md](source/Frontend/README.md)