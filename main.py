from common.convert_func import convert
from common.cur_codes import CODES
from common.get_interest_rates import get_interest_rate
from common.Moscow_exchange import get_imoex_index
import plotly.express as px
import pandas as pd
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/converter', methods=['GET', 'POST'])
def converter():
    return render_template('converter.html', convert=convert, codes=CODES)


@app.route('/convert1', methods=['POST'])
def convert1():
    input_currency = request.json['inputCurrency'].upper()
    output_currency = request.json['outputCurrency'].upper()
    input_value = request.json['inputValue']
    result = convert(input_currency, output_currency, input_value)

    return jsonify(result=result)


@app.route('/convert2', methods=['POST'])
def convert2():
    input_currency = request.json['inputCurrency'].upper()
    output_currency = request.json['outputCurrency'].upper()
    input_value = request.json['inputValue']
    result = convert(input_currency, output_currency, input_value, reverse=True)

    return jsonify(result=result)

@app.route('/interest_rate')
def interest_rate():

    data = pd.DataFrame(get_interest_rate('01.12.2013', datetime.now()), columns=['Дата', '%'])

    fig = px.line(data, x='Дата', y='%', title='Ключевая ставка')
    fig.update_layout(xaxis_title='Дата', yaxis_title='Ставка (% годовых)', height=600, plot_bgcolor='#DCDCDC', paper_bgcolor='#f4f4f4')
    fig.update_traces(line=dict(color='#B22222'))

    graph_html = fig.to_html(full_html=False)

    return render_template('interest_rate.html', graph_html=graph_html, data=data)


@app.route('/imoex_index')
def imoex_index():

    data = get_imoex_index(start_day='2013-03-05', end_day=datetime.now())

    fig = px.line(data, x='Дата', y='Значение', title='Индекс МосБиржи')
    fig.update_layout(xaxis_title='Дата', yaxis_title='Значение',height=600, plot_bgcolor='#DCDCDC', paper_bgcolor='#f4f4f4')
    fig.update_traces(line=dict(color='#B22222'))

    graph_html = fig.to_html(full_html=False)

    return render_template('imoex_index.html', graph_html=graph_html, data=data)


if __name__ == '__main__':
    app.run(debug=True)