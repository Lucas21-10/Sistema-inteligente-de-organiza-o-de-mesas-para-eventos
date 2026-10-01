from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Sistema Inteligente de Organização de Mesas"

if __name__ == "__main__":
    app.run(debug=True)