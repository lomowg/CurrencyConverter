from flask import Flask, render_template, request, redirect, url_for, jsonify
from convert_func import convert

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/converter', methods=['GET', 'POST'])
def converter():
    return render_template('converter.html', convert=convert)

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


if __name__ == '__main__':
    app.run(debug=True)