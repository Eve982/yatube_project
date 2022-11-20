## **Описание проекта:**

Социальная сеть для авторов и подписчиков. Пользователи могут подписываться на авторов, оставлять и удалять комментарии к постам, оставлять посты на главной странице и в тематических группах, прикреплять изображения к публикуемым постам.

При создании проекта использован следующий стек технологий:
```
Python 3.7
Django 2.2
Pytest
```

Приложение доступно для ознакомления на хостинге PythonAnyWhere по ссылке:

```
http://eve982.pythonanywhere.com/
```

## **Как запустить проект:**
Все команды необходимо выполнять в командной строке Вашего ПК. Первую команду следует выполнять в той локальной папке своего ПК, в которую Вы хотите склонировать проект из стороннего репозитория.
Клонировать репозиторий выполнением следующей команды в командной строке:

```
git clone <сссылка на проект>
```
если Вы используете SSH-подключение, то, вместо <сссылка на проект>, укажите:

```
git clone git@github.com:Eve982/yatube_project.git
```
для HTTPS-подключений укажите следующую ссылку:

```
https://github.com/Eve982/yatube_project.git
```
Перейти в клонированый проект командой:

```
cd yatube_project
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
Запустить виртуальное окружение:

```
source venv/bin/activate
```
Обновить пакетный менеджер pip во избежание проблем при установке зависимостей приложения:

```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Данный проект реализован мною в рамках обучения на курсе "Python-разработчик" онлайн-школы Яндекс Практикум.