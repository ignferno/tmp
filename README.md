# TMP
Templates for various web development setups. The idea is to create a fork for each possible setup, with the master fork mostly containing documentation on the other forks in the repo.

The readme file for each fork will give some info on how to setup the runtime and a short description of included software.

Install docker
- manage docker as non-root user
- - docker gives various errors when not executed with sudo or as root
https://docs.docker.com/engine/install/linux-postinstall/

cmds:
docker ps
docker log

# dependencies
- Docker
Most other dependencies should be installed via docker and is therefore not necessary to list here
- JS stack: React, npm etc

# This repo below
# Minimal `flask` + `docker-compose` + `redis` + external `css`
This application is designed to be as small and clean as possible while displaying as many as possible features. It is intended to be forked for developing similar examples with small variations e.g. other database servers than redis, or including javascript frameworks.
## Notes
remember to use `ctrl+shift+R` to hard refresh, otherwise cached static files will be used instead of updated ones

