# Homework-1 (TechnoPark)

#### Dataset "Heart Disease Cleveland UCI" is described in notebooks/EDA.ipyng

Use Amazon s3 for data 

## Installation

`python -m venv .venv`

`source .venv/bin/activate`

`pip install -r requirements.txt`

## Usage 

Models - RandomForestClassifier or Gradien:

`export PYTHONPATH=.`

`python ml_project/train_pipeline.py —config-name="train_RFC_config"`

`python ml_project/train_pipeline.py —config-name="train_GBC_config"`

Prediction:

`python ml_project/predict_pipeline.py —config-name="predict_config"`

Tests:

`pytest ml_project/tests/`

## Project Organization

    ├── README.md             <- The top-level README for developers using this project.
    ├── data
    │   └── raw               <- The original, immutable data dump.
    │
    ├── models                <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks             <- Jupyter notebooks with exploratory data analys
    │    
    ├── requirements.txt      <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    │
    └── ml_project                   <- Source code for use in this project
        ├── __init__.py       <- Makes src a Python module
        │
        ├── data              <- Scripts to download or read data
        │
        ├── features          <- Scripts to turn raw data into features for modeling
        │
        ├── models            <- Scripts to train models and then use trained models to make
        │                   predictions
        │
        ├── tests             <- Scripts to test code 
        │
        ├──  train_pipeline.py   <- Scripts to train pipeline
        │
        ├──  predict_pipeline.py <- Scripts to predict pipeline


#### Самооценка

1. В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе **(1/1)**
2. В пулл-реквесте проведена самооценка, распишите по каждому пункту выполнен ли критерий или нет и на сколько баллов(частично или полностью) **(1/1)**
3. Выполнено EDA, закоммитьте ноутбук в папку с ноутбуками **(1/1)**
4. Написана функция/класс для тренировки модели, вызов оформлен как утилита командной строки, записана в readme инструкцию по запуску **(3/3)**
5. Написана функция/класс predict (вызов оформлен как утилита командной строки), которая примет на вход артефакт/ы от обучения, тестовую выборку (без меток) и запишет предикт по заданному пути, инструкция по вызову записана в readme **(3/3)**
6. Проект имеет модульную структуру **(2/2)**
7. Использованы логгеры **(2/2)**
8. Написаны тесты на отдельные модули и на прогон обучения и predict **(2/3)**
9. Для тестов генерируются синтетические данные, приближенные к реальным **(0/2)**
10. Обучение модели конфигурируется с помощью конфигов yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель **(2/3)**
11. Используются датаклассы для сущностей из конфига, а не голые dict **(2/2)**
12. Напишите кастомный трансформер и протестируйте его **(0/3)**
13. В проекте зафиксированы все зависимости (**(1/1)**
14. Настроен CI для прогона тестов, линтера на основе github actions **(0/3)**

**20*0.6=12**
