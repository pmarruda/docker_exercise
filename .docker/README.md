# Docker Setup for Game Cataloguer

This directory contains the Docker setup for the Game Cataloguer application, Dashboard and respective services.

## Structure
```
.docker/
├── docker-compose.yaml
├── Dockerfile.backend
├── Dockerfile.frontend
├── envs/
│   ├── backend.env
│   └── frontend.env
├── grafana/
│   ├── csv/
│   ├── pdf/
│   ├── plugins/
│   │   └── grafana-lokiexplore-app/
│   └── png/
├── heimdall-custom/
│   ├── app.sqlite
│   ├── init/
│   ├── Dockerfile
│   └── heimdall-config/
│       ├── .migrations
│       ├── copy.txt
│       ├── keys/
│       ├── log/
│       ├── nginx/
│       ├── php/
│       └── www/
│
└── prometheus.yml
```

## Services

- **games-backend**: FastAPI backend service
- **games-frontend**: React frontend service
- **postgres**: PostgreSQL database service
- **heimdall**: Heimdall dashboard service
- **glances**: Glances monitoring service
- **grafana**: Grafana monitoring service

## Usage

1. Navigate to the `.docker` directory:

```bash
cd .docker
```

2. Start the services using `docker-compose`:

```bash
docker-compose up --build
```

## Custom Configurations

- **heimdall-custom**: Contains custom configurations for the Heimdall dashboard service. The `init/` directory includes a script that handles first-run initialization by copying pre-configured settings.
- **grafana**: Contains custom configurations for the Grafana monitoring service.
- **prometheus.yml**: Configuration file for the Prometheus monitoring service.


## Environment Variables

Environment variables for the backend and frontend services are defined in the `envs` directory:

- `envs/backend.env`
- `envs/frontend.env`