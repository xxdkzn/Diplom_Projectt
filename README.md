Для запуска проекта вам потребуется:

1. Клонировать репозиторий:
git clone https://github.com/xxdkzn/Diplom_Projectt.git

2. Перейти в директорию проекта:
cd diplom_project

3. Создать и активировать виртуальное окружение:
python -m venv venv
source venv/bin/activate | Windows: venv\Scripts\activate

4. Установить зависимости:
pip install -r requirements.txt

5. Выполнить миграции:
python manage.py migrate

6. Запустить сервер:
python manage.py runserver

Теперь ваше приложение доступно по адресу `http://127.0.0.1:8000/`.