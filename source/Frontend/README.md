# Frontend for Game Cataloguer

This is the frontend application for the Game Cataloguer, built with React.

## Prerequisites

- Node.js version 14 or higher

## Installation

1. Navigate to the frontend directory:

   ```bash
   cd source/Frontend/games-cataloguer  
   ```
2. Install the dependencies:
    ```bash
    npm install
    ```
3. Create a .env file with the contents from [.docker/envs/frontend.env](../../.docker/envs/frontend.env) 

## Running the Application

1. Start the development server:

   ```bash
   npm start
   ```

2. Open your browser and navigate to `http://localhost:3000`.

## Building for Production

1. Build the application for production:

   ```bash
   npm run build
   ```

2. The production-ready files will be in the `build` directory.

## Docker

1. Build the Docker image:

   ```bash
   docker build -t games-frontend -f .docker/Dockerfile.frontend .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 80:80 games-frontend
   ```