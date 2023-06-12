from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest
from players import Players, UDPlayers
from translate import Translate, UDTranslate
from company import Company, UDCompany
from books import Books, UDBooks

project = Flask(__name__)


@project.route('/')
def index():
    return render_template('index.html')


@project.route('/basketball_players', methods=['POST', 'GET'])
def basketball_players():
    if request.method == 'POST':
        data: dict = request.form.to_dict()
        data_list: list = [data[key] for key in data if data[key] != '']
        if len(data_list) == 0:
            return render_template('answers/players/basketball_players.html', result=Players.read_csv_to_html())
        return render_template('answers/players/basketball_players.html', result=Players(data).add_player_to_csv())
    if request.method == 'GET':
        word: str = request.args.get('search_players')
        return render_template('answers/players/basketball_players.html', result=Players.search(word))


@project.route('/basketball_players/delete', methods=['POST', 'GET'])
def delete_players():
    player_id: dict = request.form.to_dict()
    return render_template('answers/players/basketball_players.html', result=UDPlayers(player_id).delete())


@project.route('/basketball_players/update', methods=['POST', 'GET'])
def update_players():
    data: dict = request.form.to_dict()
    return render_template('answers/players/basketball_players.html', result=UDPlayers(data).update())


@project.route('/translate', methods=['POST', 'GET'])
def translate():
    if request.method == 'POST':
        if len(request.form['word_translate']) != 0:
            return render_template('answers/translate/translate.html',
                                   result=Translate(request.form['word_translate']).check_spelling())
        return render_template('answers/translate/translate.html', result=Translate.read_csv_to_html())
    if request.method == 'GET':
        word: str = request.args.get('search_words')
        return render_template('answers/translate/translate.html', result=Translate.search(word))


@project.route('/translate/delete', methods=['POST', 'GET'])
def delete_words():
    word_id: dict = request.form.to_dict()
    return render_template('answers/translate/translate.html', result=UDTranslate(word_id).delete())


@project.route('/translate/update', methods=['POST', 'GET'])
def update_words():
    data: dict = request.form.to_dict()
    return render_template('answers/translate/translate.html', result=UDTranslate(data).update())


@project.route('/company_employees', methods=['POST', 'GET'])
def company_employees():
    if request.method == 'POST':
        data: dict = request.form.to_dict()
        data_list: list = [data[key] for key in data if data[key] != '']
        if len(data_list) == 0:
            return render_template('answers/company/company_employees.html', result=Company.read_csv_to_html())
        return render_template('answers/company/company_employees.html', result=Company(data).add_employee_to_csv())
    if request.method == 'GET':
        word: str = request.args.get('search_employees')
        return render_template('answers/company/company_employees.html', result=Company.search(word))


@project.route('/company_employees/delete', methods=['POST', 'GET'])
def delete_employee():
    employee_id: dict = request.form.to_dict()
    return render_template('answers/company/company_employees.html', result=UDCompany(employee_id).delete())


@project.route('/company_employees/update', methods=['POST', 'GET'])
def update_employee():
    data: dict = request.form.to_dict()
    return render_template('answers/company/company_employees.html', result=UDCompany(data).update())


@project.route('/books', methods=['POST', 'GET'])
def books():
    if request.method == 'POST':
        data: dict = request.form.to_dict()
        data_list: list = [data[key] for key in data if data[key] != '']
        if len(data_list) == 0:
            return render_template('answers/books/books.html', result=Books.read_csv_to_html())
        return render_template('answers/books/books.html', result=Books(data).add_book_to_csv())
    if request.method == 'GET':
        word: str = request.args.get('search_books')
        return render_template('answers/books/books.html', result=Books.search(word))


@project.route('/books/delete', methods=['POST', 'GET'])
def delete_book():
    book_id: dict = request.form.to_dict()
    return render_template('answers/books/books.html', result=UDBooks(book_id).delete())


@project.route('/books/update', methods=['POST', 'GET'])
def update_book():
    data: dict = request.form.to_dict()
    return render_template('answers/books/books.html', result=UDBooks(data).update())


@project.route('/help')
def help_page():
    return render_template('codes/help_links.html')


@project.route('/help_players')
def help_ex_1():
    return render_template('codes/ex_1/codes_ex_1_template.html')


@project.route('/help_translate')
def help_ex_2():
    return render_template('codes/ex_2/codes_ex_2_template.html')


@project.route('/help_company')
def help_ex_3():
    return render_template('codes/ex_3/codes_ex_3_template.html')


@project.route('/help_books')
def help_ex_4():
    return render_template('codes/ex_4/codes_ex_4_template.html')


@project.errorhandler(BadRequest)
def bad_request(e):
    return render_template('errors/bad_request.html'), 400


@project.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    project.run(debug=True)
