from flask import Flask, render_template

# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

app = Flask(__name__)

@app.route('/')
@app.route('/news/')
def students():
    news = [{'title': 'News1', 'description': 'Description1', 'date': '2024-02-11'},
            {'title': 'News2', 'description': 'Description2', 'date': '2024-01-01'},
            {'title': 'News3', 'description': 'Description3', 'date': '2024-01-25'}]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
