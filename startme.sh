#! /usr/bin/env bash

# docker-compose run --rm jupyter python3 create_workshop.py
# docker-compose -f workshop_python_edition_01.yml up -d

docker compose run --rm jupyter ssh -o StrictHostKeyChecking=no alice@ubuntu "getent passwd alice"