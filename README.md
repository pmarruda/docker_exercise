# Game Cataloguer and Dashboard

This repository contains a Game Cataloguer application along with a dashboard to monitor various services using Docker Compose.

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

## Game Cataloguer Features
- User authentication (login and signup)
- Browse games
- Add games to wishlist
- View wishlist
- Compare games (not implemented)
- Get recommendations based on previously liked games (not implemented)
  
## Dashboard Services

- **heimdall**: Heimdall dashboard service
- **games-backend**: FastAPI backend service
- **games-frontend**: React frontend service
- **postgres**: PostgreSQL database service
- **glances**: Glances monitoring service
- **grafana**: Grafana monitoring service
- **prometheus**: Prometheus monitoring service
- **node-exporter**: Node-Exporter monitoring service

## Pre-requisites

- Docker & Docker-compose  
#### Alternatively (for Game Cataloguer backend and frontend only)
- Node.js version 14 or higher
- Python 3.10 or higher
- PostgreSQL


## Getting Started

### Clone the Repository

To get started, clone the repository using the following command:

```bash
git clone https://github.com/pmarruda/docker_exercise.git
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

## Game Cataloguer

The Game Cataloguer application allows users to browse and manage a catalog of games, including adding games to their wishlist. It consists of a FastAPI backend and a React frontend.
- Access it via `http://127.0.0.1`
### Testing
Seed data has been provided to simulate the state of the application.  
Many different games are added to the db by default and a user with credentials:
- Username: `testuser`
- Password: `testpwd`

## Dashboard

The dashboard includes Heimdall for service management and Glances, Prometheus, Node-Exporter and Grafana for system monitoring and data visualization. 
- Access it via `http://localhost:8081`  


## Alternative Setup (Game Cataloguer backend and frontend only)
### Refer to the individual README files for individual setup instructions:
- Backend and DB: [Backend/README.md](source/Backend/README.md)
- Frontend: [Frontend/README.md](source/Frontend/README.md)
