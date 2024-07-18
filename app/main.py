from flask import Blueprint, render_template, request, send_file
from .scraper import scrape_and_save

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        urls = request.form.getlist('urls')
        file_path = scrape_and_save(urls)
        return send_file(file_path, as_attachment=True)

    return render_template('index.html')
