#!/bin/bash

poetry export -f requirements.txt --output requirements.txt
docker-compose up --build