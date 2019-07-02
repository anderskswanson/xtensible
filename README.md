# xtensible
Modular, python-based discord bot

#### Run via Docker
- create auth.json with your discord token, following app/resources/auth.json.example
`docker build . -t bot:latest`
`docker run -it bot:latest`

#### Run via command line
- create auth.json with your discord token, following app/resources/auth.json.example
- install dependencies with `make install`
- run bot with `make run`
