# README

Материалы к курсу 'Введение в программирование'

Набор скриптов для скачивания и обработки Гражданского кодекса РФ.

## Подготовка к работе

```shell
# установить зависимости проекта
pip install -r requirements.txt
# установить инструменты разработки
pip install -r requirements-dev.txt
# подцепить pre-commit к git
pre-commit install
```

## Выкачивание и обработка текстов

Мы запускаем папку скрипт **как модуль** (с опцией `-m`):

Вывод справки (help):

```shell
python -m scripts --help
python -m scripts -h
```

Команды для работы:

```shell
# Показать используемые папки
python -m scripts show_paths
# Скачать 'Гражданский кодекс РФ'
python -m scripts download_html
# Извлечь текст из html
python -m scripts html_to_txt
```
