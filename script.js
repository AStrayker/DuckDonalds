// Корзина
let cart = {};

// Инициализация индексов для анимации
document.querySelectorAll('.item').forEach((item, index) => {
    item.style.setProperty('--index', index);
    item.addEventListener('click', () => addToCart(item));
});

// Добавление товара в корзину
function addToCart(item) {
    const name = item.getAttribute('data-name');
    const price = parseFloat(item.getAttribute('data-price'));

    if (cart[name]) {
        cart[name].quantity += 1;
    } else {
        cart[name] = { price: price, quantity: 1 };
    }

    updateCart();
}

// Обновление корзины
function updateCart() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    cartItems.innerHTML = '';

    let total = 0;
    for (const [name, details] of Object.entries(cart)) {
        const itemTotal = details.price * details.quantity;
        total += itemTotal;
        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `<span>${details.quantity}x ${name}</span><span>${itemTotal.toFixed(2)} грн</span>`;
        cartItems.appendChild(cartItem);
    }

    cartTotal.textContent = `ВСЬОГО: ${total.toFixed(2)} грн`;
}

// Очистка корзины
function clearCart() {
    cart = {};
    updateCart();
}

// Подтверждение заказа
function confirmOrder() {
    if (Object.keys(cart).length === 0) {
        alert('Ваша корзина пуста!');
        return;
    }

    const total = Object.values(cart).reduce((sum, item) => sum + item.price * item.quantity, 0);
    alert(`Ваш заказ на сумму ${total.toFixed(2)} грн принят! Мы свяжемся с вами для подтверждения.`);
    clearCart();
}
