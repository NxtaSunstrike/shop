from flask import Flask,render_template
from bot.databases.requests import get_cloths,get_cloth_by_id
from threading import Thread

app = Flask(__name__)


@app.route('/')
async def index():
    cloths = await get_cloths()
    return render_template('main_page.html',cloths = cloths,enumerate=enumerate)


@app.route('/<int:id>')
async def cloth(id):
    cloth = await get_cloth_by_id(id=id)
    return render_template('cloth.html',enumerate = enumerate,cloth = cloth)


def run():
    app.run(host='0.0.0.0', port=8080)


def alive():
  t = Thread(target=run)
  t.start()