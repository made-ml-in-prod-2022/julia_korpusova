# Homework2

# Онлайн модель
Для сборки или загрузки контейнера:
~~~
docker build -t juliakorp/online_model:v1 .
~~~

Для запуска контейнера:
~~~
docker run --rm -p 8000:8000 --env-file .env juliakorp/online_model:v1
~~~
Для запуска скрипта:
~~~
python make_request.py
~~~