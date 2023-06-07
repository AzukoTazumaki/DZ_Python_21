from flask import Flask, render_template, request
from translate import Translate
from players import Players
from company import Company
from books import Books

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/basketball_players', methods=['POST', 'GET'])
def basketball_players():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_list = [data[key] for key in data if data[key] != '']
        if len(data_list) == 0:
            return render_template('answers/basketball_players.html', result=Players.read_csv_to_html())
        return render_template('answers/basketball_players.html', result=Players(data).add_player_to_csv())


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    if request.method == 'POST':
        if len(request.form['word_translate']) != 0:
            return render_template('answers/translate.html',
                                   result=Translate(request.form['word_translate']).check_spelling())
        return render_template('answers/translate.html', result=Translate.read_csv_to_html())


@app.route('/company_employees', methods=['POST', 'GET'])
def company_employees():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_list = [data[key] for key in data if data[key] != '']
        if len(data_list) == 0:
            return render_template('answers/company_employees.html', result=Company.read_csv_to_html())
        return render_template('answers/company_employees.html', result=Company(data).add_employee_to_csv())


@app.route('/books', methods=['POST', 'GET'])
def books():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_list = [data[key] for key in data if data[key] != '']
        if len(data_list) == 0:
            return render_template('answers/books.html', result=Books.read_csv_to_html())
        return render_template('answers/books.html', result=Books(data).add_book_to_csv())


@app.route('/help')
def help_page():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(debug=True)
