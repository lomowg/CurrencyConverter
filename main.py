from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/converter', methods=['GET', 'POST'])
def converter():
    if request.method == 'POST':
        # Получаем данные из формы
        amount = request.form['amount']
        from_currency = request.form['fromCurrency']
        to_currency = request.form['toCurrency']

        return f'Перевод {amount} {from_currency} в {to_currency}'

    return render_template('converter.html')


if __name__ == '__main__':
    app.run(debug=True)
