from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/list_prof/<list>')
def training(list):
    return render_template('base.html', type=list)


if __name__ == '__main__':
    app.run(port=8070, host='127.0.0.1')
