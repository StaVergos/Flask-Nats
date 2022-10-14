# Flask-Nats
POC for Nats.io and Flask

## How to install
1. Create a virtual environment with python -m venv .venv
2. Activate it with .venv/bin/activate (MacOS)
3. Install dependancies with pip install -r requirements

### Nats
You need to have Nats install in your machine
For Mac you use brew:

brew install nats
brew tap nats-io/nats-tools
brew install nats-io/nats-tools/nats

Then activate the server with: nats-server

Or you can run the server from the Docker with
docker run -p 4222:4222 -ti nats:latest

### What the application does

It makes a call to the SWAPI, publish it into a nats subject and a sub prints the name and height of the hero from Star Wars


Cheers!
