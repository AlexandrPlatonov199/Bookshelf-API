# «API Сервис книжного магазина».

## Описание
Это веб-приложение для онлайн-книжного магазина, предназначенное для любителей чтения и поиска новых литературных шедевров.
На данный момент проект выполняет неполный функционал CRUD и не полностью покрыт тестами, его цель - отобразить структуру 
применяемую в коммерчиском проекте.

## Список сделанного:
- [x] Реализовать проект на основе асинхронного подхода
- [x] Реализовать миграции с помощью alembic
- [x] Создать образец relationship "многие ко многим"
- [x] Добавить слой который будет обрабатывать sqlalchemy запросы
- [x] Добавить admin-panel(sqladmin)
- [x] Добавить Аутентификация JWT / Авторизация
- [x] Добавить кастомные ошибки
- [x] Добавьте конфигурацию кэша с помощью fastapi-cache2 и redis
- [x] Добавьте тестирование unit и integrations c помощью pytest
- [x] Добавить стилизацию кода при помощи black, flake8, isort
- [x] Добавить loger при помощи python json logger
- [x] Добавить возможность отлавливать ошибки в коде при помощи Sentry
- [x] Добавить версионирование API c помощью fastapi-versioning
- [x] Добавить контейнеризацию Docker
- [x] Добавить мониторинг с помощью Grafana + Prometheus


## Порядок запуска проекта

1. Клонировать проект на локальный компьютер
```sh
git clone <SSH key>
```
2. Заполнить файлы .env и .env-non-dev своими данными
3. Запустить проект командой:
```sh
docker compose up
```
4. Для отображения БД [создать сервер](http://localhost:5050/browser/) со следующими параметрами

|       Параметр       | Значение |
|:--------------------:|:--------:|
| Host name/address    |    db    |
|         Port         |   5432   |
| Maintenance database | name_db  |
|       Username       | postgres |
|       Password       | postgres |


5. Для отображения API проекта и выполнения запросов перейти к [примерам запросов выполняемых сервисом](http://127.0.0.1:7777/v1/docs).

6. Для оценки выполняемых запросов:
- [Проверить prometheus](http://127.0.0.1:9090/targets?search=)

<p align="center">
  <img src="static\prometheus.png" align="center"/>
</p>

- Зайти на [Grafana](http://127.0.0.1:3000) вести admin/ admin

<p align="center">
  <img src="static\grafana_login.png" align="center"/>
</p>

- Перейти во [вкладку](http://127.0.0.1:3000/datasources/new) и выбрать Prometheus

<p align="center">
  <img src="static\prometheus_sourse.png" align="center"/>
</p>

- Указать URL prometheus и сохранить настройки

<p align="center">
  <img src="static\prometheus_url.png" align="center"/>
</p>

- [Перейти на ссылку](http://127.0.0.1:3000/dashboard/import) и в Import via panel json 
вставить данные из файла grafana-dashboard.json и нажать кнопку load

<p align="center">
  <img src="static\load.png" align="center"/>
</p>

- Сделать [запросы выполняемые сервисом](http://127.0.0.1:7777/v1/docs)
