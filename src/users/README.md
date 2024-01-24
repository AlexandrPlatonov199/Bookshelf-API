# Bookshelf Users App

## Preparation

### Migrate

```shell
python -m src users database migrations apply 
```

### Fixtures

```shell
python -m src users database fixtures apply autotests
```

## Run

```shell
python -m src users run
```
