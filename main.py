from flask import Flask, render_template, url_for
import os

def index():
    return render_template('index.html')

def develop():
    return render_template('develop.html')

def finance():
    return render_template('finance.html')

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)
 
app.add_url_rule('/', 'index', index)
app.add_url_rule('/develop', 'develop', develop)
app.add_url_rule('/finance', 'finance', finance)


# Запускаем веб-сервер:
app.run()
