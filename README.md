# Bookshelf Backend

## Requirements

### Requirements: Docker

For running or testing all services you can use `Docker`. You can see instructions for installation
[here](https://docs.docker.com/engine/install/).

After installation you should init `swarm`
```shell
docker swarm init 
```

### Requirements: Python

For running or testing all services you can use `Python` environment. You can install Python on
your local machine directly (see [here](https://www.python.org/downloads/)) or use any wrappers
(`venv`, `pyenv`, `pipenv`, etc.).

**Python version: `3.11` or higher**

After installation Python you need install `poetry` (v1.6.1):
```shell
pip install poetry==1.6.1
```
And install all Python requirements:
```shell
poetry install --all-extras
```

## Test

### Test: Docker

For testing you should build full image

```shell
docker build -t bookshelf --target full . 
```

**Unit tests**
```shell
docker run bookshelf pytest /app/tests
```

### Run: Python

For running separate services, please, see documentation:
1. [Users](src/users/README.md)
