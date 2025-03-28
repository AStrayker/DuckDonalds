from flask import Flask, render_template, request, redirect, url_for
from flask_frozen import Freezer

app = Flask(__name__)

# Меню "Дак Дональдс"
menu = {
    "Бургеры": [
        {"name": "ДакКриспи", "price": 120, "image": "dakcrispy.jpg"},
        {"name": "ДакКриспи Смоки Бекон", "price": 140, "image": "dakcrispy_bacon.jpg"},
        {"name": "Чизбургер", "price": 60, "image": "cheeseburger.jpg"},
        {"name": "Гамбургер", "price": 50, "image": "hamburger.jpg"},
        {"name": "Биг Дак", "price": 150, "image": "bigdak.jpg"},
        {"name": "ДакТейсти", "price": 160, "image": "daktasty.jpg"},
        {"name": "ДакЧикен", "price": 110, "image": "dakchicken.jpg"},
    ],
    "Напитки": [
        {"name": "Кола (маленькая)", "price": 35, "image": "cola_small.jpg"},
        {"name": "Кола (большая)", "price": 50, "image": "cola_large.jpg"},
        {"name": "Спрайт (маленькая)", "price": 35, "image": "sprite_small.jpg"},
        {"name": "Спрайт (большая)", "price": 50, "image": "sprite_large.jpg"},
        {"name": "Фанта (маленькая)", "price": 35, "image": "fanta_small.jpg"},
        {"name": "Кофе ДакКофе", "price": 45, "image": "dakcoffee.jpg"},
        {"name": "Чай (зелёный)", "price": 40, "image": "greentea.jpg"},
    ],
    "Картофель": [
        {"name": "Картофель Фри (маленький)", "price": 40, "image": "fries_small.jpg"},
        {"name": "Картофель Фри (большой)", "price": 60, "image": "fries_large.jpg"},
        {"name": "Картофель по-деревенски", "price": 65, "image": "country_fries.jpg"},
        {"name": "ДакНаггетсы, 6 шт.", "price": 80, "image": "daknuggets_6.jpg"},
    ],
    "Десерты": [
        {"name": "ДакФлурри", "price": 70, "image": "dakflurry.jpg"},
        {"name": "Пирожок с вишней", "price": 35, "image": "cherry_pie.jpg"},
        {"name": "Пирожок с яблоком", "price": 35, "image": "apple_pie.jpg"},
        {"name": "Мороженое ванильное", "price": 50, "image": "vanilla_icecream.jpg"},
        {"name": "Мороженое шоколадное", "price": 50, "image": "choco_icecream.jpg"},
    ],
    "Салаты": [
        {"name": "Салат Цезарь", "price": 90, "image": "caesar_salad.jpg"},
        {"name": "Салат с курицей", "price": 85, "image": "chicken_salad.jpg"},
        {"name": "Овощной салат", "price": 70, "image": "veggie_salad.jpg"},
    ],
    "Соусы": [
        {"name": "Кетчуп", "price": 15, "image": "ketchup.jpg"},
        {"name": "Сырный соус", "price": 20, "image": "cheese_sauce.jpg"},
        {"name": "Барбекю", "price": 15, "image": "bbq_sauce.jpg"},
        {"name": "Горчичный соус", "price": 15, "image": "mustard_sauce.jpg"},
    ],
    "Завтраки": [
        {"name": "ДакМаффин с яйцом", "price": 70, "image": "dakmuffin_egg.jpg"},
        {"name": "ДакМаффин с беконом", "price": 80, "image": "dakmuffin_bacon.jpg"},
        {"name": "Овсяная каша", "price": 50, "image": "oatmeal.jpg"},
    ]
}

# Корзина
cart = {}

@app.route('/')
def index():
    return render_template('index.html', menu=menu, cart=cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    category = request.form['category']
    item_name = request.form['item']
    item = next(i for i in menu[category] if i["name"] == item_name)
    
    if item_name in cart:
        cart[item_name]["quantity"] += 1
    else:
        cart[item_name] = {"price": item["price"], "quantity": 1}
    
    return redirect(url_for('index'))

@app.route('/clear_cart')
def clear_cart():
    cart.clear()
    return redirect(url_for('index'))

@app.route('/confirm_order')
def confirm_order():
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    cart.clear()
    return render_template('confirm.html', total=total)

# Настройка Frozen-Flask
freezer = Freezer(app)

# Добавляем маршруты для заморозки
@freezer.register_generator
def url_generator():
    yield 'index', {}
    yield 'confirm_order', {}

if __name__ == '__main__':
    # Для заморозки страниц
    freezer.freeze()
    # Для локального запуска (опционально)
    # app.run(debug=True)
