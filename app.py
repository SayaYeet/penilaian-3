from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def igs():
    data = [1, 2, 3, 4]
    kata = "CODING IGS"
    return render_template('igs.html', data=data, kata=kata)

if __name__ == '__main__':
    app.run(debug=True)