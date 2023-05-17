from flask import Flask, session, redirect, url_for, request, render_template
import os

def test():
    title = '''<body><h1>Список сотрудников компании "Импульс":</h1><p><l>Отдел разработки:</l></p><p>Отдел разбора говна</p></body>'''
    return title

# Создаём объект веб-приложения:
app = Flask(__name__)

app.add_url_rule('/', 'index', test)

if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run() 