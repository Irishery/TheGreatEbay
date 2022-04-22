import {add_to_cart} from '../js/api_methods.js'


document.getElementById('add_to_cart').onclick = async (event) => {
    let count = document.getElementById('product_count').value;
    await add_to_cart(event.target.value, count);
    alert('Товар добавлен')
}