from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper
def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper
def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'
@app.route('/')
def hello_world():
    return 'Helrtlo, World!'

@app.route('/<username>/<int:post_id>')
def show_user_profile(username):
    return f'Htri {username}'

if __name__ == '__main__':
    app.run(debug=True)