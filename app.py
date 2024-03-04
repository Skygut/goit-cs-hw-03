from flask import Flask

# Створюємо екземпляр класу Flask
app = Flask(__name__)


# Додаємо маршрут для головної сторінки
@app.route("/")
def hello():
    return "Привіт, це мій перший веб-додаток на Flask!"


# Запускаємо додатокstat
if __name__ == "__main__":
    app.run(debug=True)
