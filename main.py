import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<h1 style="text-align: center;">Курс валют</h1>'
    text += '<table style="width: 100%; border-collapse: collapse;">'
    text += '<tr style="background-color: #f2f2f2;">'
    for key in valutes[0].keys():
        text += f'<th style="padding: 8px; border-bottom: 1px solid #ddd;">{key}</th>'
    text += '</tr>'

    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td style="padding: 8px; border-bottom: 1px solid #ddd;">{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()