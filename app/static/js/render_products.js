import {get_products, set_cookie} from './api_methods.js';
import {setCookie, getCookie} from './cookie_utils.js';

let last_product_id = 0;
let category = '';


const set_products_loader = async () => {
    document.body.onscroll = function() {
      let scroll = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0
      if (scroll == 0) {
        console.log('aboba')
      }

      let scrollHeight = $(document).height();
      let scrollPosition = $(window).height() + $(window).scrollTop();
      if ((scrollHeight - scrollPosition) / scrollHeight === 0) {
            render_products();
      }
    }
}


const render_products = async () => {
    let products_div = document.getElementById('products-div')
    let category = getCookie('category')
    if (!category) {
        category = '';
    }
    let products = await get_products(last_product_id, category);
    
    if (products.length) {
        console.log(products)
        last_product_id = products[products.length - 1].id;
    };

    products.reverse()

    for (const product of products) {
        products_div.insertAdjacentHTML(
            'afterbegin',
            `
            <div class="col-6 col-md-6 col-lg-4 col-sm-6">
                <div class="card h-100 mb-4">
                    <img src="${product.photo}" class="card-img-top w-auto" alt="...">
                    <div class="card-body">
                        <p class="card-text">${product.name}</p>
                        <a href="/product?id=${product.id}" class="btn btn-primary" style="height: 2rem;"><p style="font-size: small;">${product.cost}$</p></a>
                    </div>
                </div>
            </div>
            `
        )
    };

    
}

let $category_togglers = jQuery('.category_li')
$category_togglers.click(async function(event) {
    category = event.target.attributes[2].value;
    setCookie('category', category)
    location.reload()
})
 

document.onreadystatechange = async () => {
    if (document.readyState == "complete") {
        render_products();
        set_products_loader();
    }
}
