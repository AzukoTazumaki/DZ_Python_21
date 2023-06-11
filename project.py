from flask import Flask, render_template, request
from players import Players, UD
from translate import Translate
from company import Company
from books import Books

project = Flask(__name__)


@project.route('/')
def index():
    return render_template('index.html')


@project.route('/basketball_players', methods=['POST', 'GET'])
def basketball_players():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_list = [data[key] for key in data if data[key] != '']
        if len(data_list) == 0:
            return render_template('answers/players/basketball_players.html', result=Players.read_csv_to_html())
        return render_template('answers/players/basketball_players.html', result=Players(data).add_player_to_csv())
    if request.method == 'GET':
        word = request.args.get('search_players')
        return render_template('answers/players/basketball_players.html', result=Players.search(word))


@project.route('/basketball_players/delete', methods=['POST', 'GET'])
def delete_player():
    player_id = request.form.to_dict()
    return render_template('answers/players/basketball_players.html', result=UD(player_id).delete())


@project.route('/translate', methods=['POST', 'GET'])
def translate():
    if request.method == 'POST':
        if len(request.form['word_translate']) != 0:
            return render_template('answers/translate/translate.html',
                                   result=Translate(request.form['word_translate']).check_spelling())
        return render_template('answers/translate/translate.html', result=Translate.read_csv_to_html())
    if request.method == 'GET':
        word = request.args.get('search_words')
        return render_template('answers/translate/translate.html', result=Translate.search(word))


@project.route('/company_employees', methods=['POST', 'GET'])
def company_employees():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_list = [data[key] for key in data if data[key] != '']
        print(data)
        if len(data_list) == 0:
            return render_template('answers/company/company_employees.html', result=Company.read_csv_to_html())
        return render_template('answers/company/company_employees.html', result=Company(data).add_employee_to_csv())
    if request.method == 'GET':
        word = request.args.get('search_employees')
        return render_template('answers/company/company_employees.html', result=Company.search(word))


@project.route('/books', methods=['POST', 'GET'])
def books():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_list = [data[key] for key in data if data[key] != '']
        if len(data_list) == 0:
            return render_template('answers/books/books.html', result=Books.read_csv_to_html())
        return render_template('answers/books/books.html', result=Books(data).add_book_to_csv())
    if request.method == 'GET':
        word = request.args.get('search_books')
        return render_template('answers/books/books.html', result=Books.search(word))


@project.route('/help')
def help_page():
    return render_template('help.html')


if __name__ == '__main__':
    project.run(debug=True)
