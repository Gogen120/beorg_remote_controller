# Remote Directory Controller
Тестовое задание для beorg

## Локальный запуск
Для запуска должен быть устоновлен `docker` и `docker-compose`, для запуска контейнера с `rabbit`. Желательно создать виртуальное окружение с `python3.7` и установить нужные зависимости: `pip install -r requirements.txt`

### Переменные окружения
Для запуска приложения нужны следующие переменные окружения:

**BROKER_HOST** - имя хоста `rabbit` (по-умолчанию можно использовать `localhost`)

**DIR_PATH** - имя каталога, содержимое которого надо обновлять (по-умолчанию используется текущая директория)

**RABBITMQ_DEFAULT_USER**, **RABBITMQ_DEFAULT_PASS** - креды для подключения к `rabbit`

Эти переменные можно либо определить в `env` файле, либо создать используя `export` (для линукса)

### Запуск контейнера с брокером

Перед запуском сервера с клиентом надо запустить контейнер с брокером. Это можно сделать следующей командой: `docker-compose -f dc.dev.yaml up --build -d`

### Запуск сервера и клиента

Дальше надо запустить сервер: `python server.py`
И затем в отдельном окне запустить клиент `python client.py`
