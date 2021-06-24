from flask import request
from model import *
from database import *


@app.route('/')
def home():
    return Index()

@app.route('/add', methods=['POST'])
def add():
    return addcontact()
    

@app.route('/edit/<id>')
def contact(id):
    return onecontact(id)


@app.route('/update', methods =[ "POST"])
def edit():
    if request.method == 'POST':
        return update()


@app.route('/delete/<string:id>')
def onedel(id):
    return delete(id)


if __name__ == '__main__':
    app.run(port = 3000, debug =True)