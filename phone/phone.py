from flask import Flask
import phone


app = Flask(__name__)



@app.route('/')
def hello_world():
    phone.phone.get_html_url()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

