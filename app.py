from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/basketball_players', methods=['POST', 'GET'])
def basketball_players():
    new_player = request.form
    return render_template('answers/basketball_players.html')


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    new_word = request.form
    return render_template('answers/translate.html')


@app.route('/company_employees', methods=['POST', 'GET'])
def company_employees():
    new_employee = request.form
    return render_template('answers/company_employees.html')


@app.route('/books', methods=['POST', 'GET'])
def books():
    new_book = request.form
    return render_template('answers/books.html')


@app.route('/help')
def help_page():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(debug=True)
