from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Расширенное меню "Дак Дональдс"
menu = {
    "Бургеры": [
        {"name": "ДакКриспи", "price": 120, "image": "https://github.com/AStrayker/DuckDonalds/blob/main/%D0%94%D0%B0%D0%BA%D0%9A%D1%80%D0%B8%D1%81%D0%BF%D0%B8.jfif"},
        {"name": "ДакКриспи Смоки Бекон", "price": 140, "image": "https://github.com/AStrayker/DuckDonalds/blob/main/%D0%94%D0%B0%D0%BA%D0%9A%D1%80%D0%B8%D1%81%D0%BF%D0%B8%20%D0%A1%D0%BC%D0%BE%D0%BA%D0%B8%20%D0%91%D0%B5%D0%BA%D0%BE%D0%BD.jfif"},
        {"name": "Чизбургер", "price": 60, "image": "https://github.com/AStrayker/DuckDonalds/blob/main/%D0%A7%D0%B8%D0%B7%D0%B1%D1%83%D1%80%D0%B3%D0%B5%D1%80.jfif"},
        {"name": "Гамбургер", "price": 50, "image": "https://github.com/AStrayker/DuckDonalds/blob/main/%D0%93%D0%B0%D0%BC%D0%B1%D1%83%D1%80%D0%B3%D0%B5%D1%80.jfif"},
        {"name": "Биг Дак", "price": 150, "image": "https://github.com/AStrayker/DuckDonalds/БигДак.png"},
        {"name": "ДакТейсти", "price": 160, "image": "https://github.com/AStrayker/DuckDonalds/blob/main/%D0%94%D0%B0%D0%BA%D0%A2%D0%B5%D0%B9%D1%81%D1%82%D0%B8.jfif"},
        {"name": "ДакЧикен", "price": 110, "image": "https://virus-corp.do.am/dakchiken.png"},
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

# Корзина: {item_name: {"price": price, "quantity": quantity}}
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

if __name__ == '__main__':
    app.run(debug=True)