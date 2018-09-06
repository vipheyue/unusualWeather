from flask import Flask, request, url_for
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!!!!+++'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        username = request.form['username']
        return 'Hello, hello post' + username
    else:
        return 'get'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


# with app.test_request_context():
#     print(url_for('hello'))
#     print(url_for('hello', username='John Doe'))



if __name__ == '__main__':
    print("main")
    app.run()
