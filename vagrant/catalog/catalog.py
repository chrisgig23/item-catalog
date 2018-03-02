from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = create_engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).all()
    return render_template('catalog.html', categories = categories)

@app.route('/catalog/<int: category_id>')
def showCategory(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    categoryItems = session.query(CategoryItems).filter_by(category_id = category.id)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)