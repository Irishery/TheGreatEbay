import {checkout_cart} from '../js/api_methods.js'

document.getElementById('checkout').onclick = async () => {
    await checkout_cart()
    location.reload()
}