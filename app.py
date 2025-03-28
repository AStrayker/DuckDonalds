from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Меню "Дак Дональдс"
menu = {
    "Бургеры": [
        {"name": "ДакКриспи", "price": 120, "image": "dakcrispy.jpg"},
        {"name": "ДакКриспи Смоки Бекон", "price": 140, "image": "dakcrispy_bacon.jpg"},
        {"name": "Чизбургер", "price": 60, "image": "cheeseburger.jpg"},
        {"name": "Гамбургер", "price": 50, "image": "hamburger.jpg"},
        {"name": "Биг Дак", "price": 150, "image": "bigdak.jpg"},
    ],
    "Напитки": [
        {"name": "Кола (маленькая)", "price": 35, "image": "cola_small.jpg"},
        {"name": "Кола (большая)", "price": 50, "image": "cola_large.jpg"},
        {"name": "Спрайт (маленькая)", "price": 35, "image": "sprite_small.jpg"},
        {"name": "Кофе ДакКофе", "price": 45, "image": "dakcoffee.jpg"},
    ],
    "Картофель": [
        {"name": "Картофель Фри (маленький)", "price": 40, "image": "fries_small.jpg"},
        {"name": "Картофель Фри (большой)", "price": 60, "image": "fries_large.jpg"},
    ],
    "Десерты": [
        {"name": "ДакФлурри", "price": 70, "image": "dakflurry.jpg"},
        {"name": "Пирожок с вишней", "price": 35, "image": "cherry_pie.jpg"},
    ]
}

# Корзина
cart = []

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    category = request.form['category']
    item_name = request.form['item']
    item = next(i for i in menu[category] if i["name"] == item_name)
    cart.append(item)
    return redirect(url_for('index'))

@app.route('/cart')
def show_cart():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/clear_cart')
def clear_cart():
    cart.clear()
    return redirect(url_for('index'))

@app.route('/confirm_order')
def confirm_order():
    total = sum(item['price'] for item in cart)
    cart.clear()
    return render_template('confirm.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
