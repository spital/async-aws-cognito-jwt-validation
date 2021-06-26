# Async AWS Cognito JWT validation in Python

## Requirements

### For production

See [Dockerfile](./Dockerfile) what to install

### For test

`sudo dnf install podman` or [Install Docker Engine](https://docs.docker.com/install/).

`sudo dnf install podman-compose` or [Install Docker Compose](https://github.com/docker/compose/releases/latest).

`sudo dnf install git` or [Install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).


## Build

Please note this is example development build. For production see `requirements`.

```bash
P=xxxxxx
U=yyyyy
git clone $U/$P
cd $P
podman-compose build

podman run -it localhost/$P bash

```

## Source tests

*TODO*: pylint, unittest, sonarqube, ...


## Run

### For production

```bash
# zzzzz
```

### For test

```bash
podman-compose up -d

# or if deps are installed in your env :
# python ppppppp
```

## Use

See specification

## Stop

```bash
podman-compose down
```

