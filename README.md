# Тестовое задание для UTF.tech

### Разработчик : Лоскутова Татьяна (Loskutova Tatiana)

### Технологический стек
- Python - основной язык программирования.
- Django - фреймворк для разработки веб-приложений.
- Django REST framework - инструмент для создания веб-API на основе Django.

### Локальный запуск проекта:

**1)** Клонировать репозиторий и перейти в него в командной строке:

    https://github.com/TatianaLoskutova/Dishes

**2)** Cоздать и активировать виртуальное окружение:

    python -m venv venv

    venv/Scripts/activate

**3)** Установить зависимости из файла requirements.txt:

    python -m pip install --upgrade pip

    pip install -r requirements.txt

**4)** Выполнить миграции:

    python manage.py migrate

**5)** Запустить проект:

    python manage.py runserver

Условия ТЗ:
Стек: Django, DRF

Даны модели "Категория Блюд" и "Блюдо" для ресторана.
Даны сериализаторы.
В выборку попадают только Блюда у которых is_publish=True. Если в категории нет блюд (или все блюда данной категории имеют is_publish=False) - не включаем ее в выборку.
Запрос в БД сделать любым удобным способом: Django ORM (предпочтительно), Raw SQL, Sqlalchemy...
Написать View который вернет для API 127.0.0.1/api/v1/foods/ JSON следующего формата:

![image](https://github.com/TatianaLoskutova/Dishes/assets/108022607/7ba6ddf0-411c-41f6-91f2-0b9d410ece40)


