# Instructions to run the project

## Clone the repo
```bash
git clone https://github.com/Ruhshan/date-server.git
```

## Navigate to the repo directory
```bash
cd date-server
```

## Run the server
```bash
docker compose up --scale web=3
```

## Access the endpoint
```bash
curl http://localhost:8000/date/
```