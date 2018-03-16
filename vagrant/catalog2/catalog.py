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
    items = session.query(CategoryItem).order_by(CategoryItem.timeAdded.desc()).limit(10).all()
    return render_template('catalog.html', categories = categories, items = items)

@app.route('/catalog/<int:category_id>')
def showCategory(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    categoryItems = session.query(CategoryItem).filter_by(category_id = category.id)
    return render_template('category.html', category = category, items = categoryItems)

@app.route('/catalog/<int:category_id>/<int:item_id>')
def showItem(category_id, item_id):
    category = session.query(Category).filter_by(id = category_id).one()
    item = session.query(CategoryItem).filter_by(id = item_id).one()
    return render_template('item.html', category=category, item=item)

@app.route('/catalog/<int:category_id>/new', methods=['GET', 'POST'])
def newItem(category_id):
    if request.method == 'POST':
        newItem = CategoryItem(name = request.form['title'], description = request.form['description'], category_id = category_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategory', category_id = category_id))
    else:
        listOfCategories = session.query(Category).all()
        return render_template('newItem.html', category_id = category_id, listOfCategories = listOfCategories)

@app.route('/catalog/<int:category_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    editedItem = session.query(CategoryItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        # if request.form['course']:
        #     editedItem.course = request.form['course']

        session.add(editedItem)
        session.commit()
        return redirect(url_for('showCategory', category_id = category_id))
    else:
        listOfCategories = session.query(Category).all()
        return render_template('editItem.html', category_id=category_id, item_id=item_id, item = editedItem, listOfCategories = listOfCategories)

@app.route('/catalog/<int:category_id>/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    deletedItem = session.query(CategoryItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('showCategory', category_id = category_id))
    else:
        return render_template('deleteItem.html', category_id=category_id, item_id=item_id, item=deletedItem)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
