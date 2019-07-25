# realestate_webcrawler

## Requirements
Docker installed
Python 3+

## Getting Started
Create an empty psql database with docker

`
docker run -d \
        --name BI \
        -e POSTGRES_PASSWORD=admin \
	    -p 54320:5432 \
        -d postgres:latest

`

## Setting up a development python env
Starting in the root directory of the project, create a Python virtual environment.
`
python3 -m venv env
`

Install the project in editable mode (start from root directory of the project).
`
env/bin/pip install -e .
`
