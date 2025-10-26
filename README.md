# Volleyball Scoreboard

A simple web-based volleyball scoreboard application built with FastAPI. Track scores and sets for two teams in real-time with an easy-to-use interface.

## Features

- Live score tracking for two teams
- Set count management
- Team name customization
- REST API for scoreboard control
- Admin interface for managing the game
- Display interface for showing the scoreboard

## Running with Docker

### Build the Docker image

```bash
docker build -t volleyball-scoreboard .
```

### Run the container

```bash
docker run -d -p 8000:8000 volleyball-scoreboard
```

The application will be accessible at:
- **Scoreboard Display**: http://localhost:8000/scoreboard.html
- **Admin Interface**: http://localhost:8000/admin.html
- **API Documentation**: http://localhost:8000/docs

## API Endpoints

- `GET /` - Get current state of both teams
- `PUT /scores/{team}` - Update points or sets for a team (0 = Home, 1 = Away)
- `PUT /names/{team}` - Change team name (0 = Home, 1 = Away)

## Local Development

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
uvicorn main:app --reload
```
