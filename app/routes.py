from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from app import app
import sqlite3
from flask import g

def get_db_connection(db_path='C:/Users/Win10/Desktop/ice_cream_parlor_app/instance/new_ice_cream_parlor.db'):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  
    return conn

@app.route('/flavors')
def view_flavors():
    conn = get_db_connection()
    flavors_data = conn.execute('SELECT * FROM seasonal_flavors').fetchall()
    conn.close()

    flavors = []
    for flavor in flavors_data:
        flavor_dict = {
            'name': flavor['flavor_name'],
            'description': flavor['description'],
            'price': flavor['price'],
            'image': "https://via.placeholder.com/250x180?text=" + flavor['flavor_name'].replace(' ', '+')
        }
        flavors.append(flavor_dict)

    return render_template('index.html', flavors=flavors)

@app.route('/suggestions')
def view_suggestions():
    conn = get_db_connection()
    suggestions_data = conn.execute('SELECT * FROM user_suggestions').fetchall()
    conn.close()

    suggestions = [{'user_name': suggestion['user_name'], 'contact': suggestion['contact'], 'suggestion_text': suggestion['suggestion_text']} for suggestion in suggestions_data]
    return render_template('suggestions.html', suggestions=suggestions)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    flavor_id = request.json.get('flavor_id')  
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(flavor_id)
    session.modified = True
    conn = get_db_connection() 
    cart_items = get_flavors_from_ids(session['cart'], conn) 
    conn.close()

    return jsonify({'cart_items': cart_items})

def get_flavors_from_ids(flavor_ids, conn):
    placeholders = ', '.join('?' * len(flavor_ids))
    query = f'SELECT * FROM seasonal_flavors WHERE flavor_id IN ({placeholders})'
    rows = conn.execute(query, tuple(flavor_ids)).fetchall()
    return [dict(row) for row in rows]

@app.route('/remove_from_cart/<int:cart_id>', methods=['POST'])
def remove_from_cart(cart_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM cart WHERE cart_id = ?', (cart_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    conn = get_db_connection()
    cart_ids = session.get('cart', []) 
    if cart_ids:
        cart_items = get_flavors_from_ids(cart_ids, conn)
    else:
        cart_items = [] 
    total_price = sum(item['price'] for item in cart_items)
    conn.close()

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)


@app.route('/ingredients')
def view_ingredients():
    return render_template('ingredients.html')

@app.route('/search_flavors', methods=['GET'])
def search_flavors():
    search_term = request.args.get('search', '').lower()
    price_filter = request.args.get('price', '')
    query = 'SELECT flavor_name, price FROM seasonal_flavors WHERE availability = 1'

    if search_term:
        query += ' AND flavor_name LIKE ?'

    if price_filter == 'low':
        query += ' AND price < 150'
    elif price_filter == 'high':
        query += ' AND price >= 150'

    conn = get_db_connection()
    if search_term:
        flavors = conn.execute(query, ('%' + search_term + '%',)).fetchall()
    else:
        flavors = conn.execute(query).fetchall()
    conn.close()

    filtered_flavors = [{'flavor_name': flavor['flavor_name'], 'price': flavor['price']} for flavor in flavors]

    return jsonify(filtered_flavors)

# Main route
@app.route('/')
def home():
    conn = get_db_connection()
    flavors_query = 'SELECT * FROM seasonal_flavors WHERE availability = 1'
    flavors = conn.execute(flavors_query).fetchall()
    conn.close()
    return render_template('index.html', flavors=flavors)


@app.route('/checkout', methods=['POST'])
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'  
    app.run(debug=True)