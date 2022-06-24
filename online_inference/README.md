# Homework2

## Api for model
Build docker container:
~~~
docker build -t juliakorp/online_model:v1 .
~~~

Run docker container:
~~~
docker run --rm -p 8080:8080 --env-file .env juliakorp/online_model:v1
~~~

Run script for request:
~~~
python make_request.py
~~~

Run test:
~~~
export $(cat .env)
pytest
~~~

## Самооценка:
#### Основная часть

1. Оберните inference вашей модели в rest сервис на FastAPI, должен быть endpoint /predict **(3/3)**
2. Напишите endpoint /health **(1/1)** 
3. Напишите unit тест для /predict **(2/3)**
4. Напишите скрипт, который будет делать запросы к вашему сервису **(2/2)*
5. Напишите dockerfile, соберите на его основе образ и запустите локально контейнер **(4/4)**
6. опубликуйте образ в https://hub.docker.com/, используя docker push (вам потребуется зарегистрироваться) **(0/2)**
7. напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель **(0.5/1)** 
8. проведите самооценку **(1/1)**

13.5 * 0/6 = 8.1 