const base_request = (path, method, data) => {
    const request = new Request(`http://127.0.0.1:5000/api/${path}/?` + new URLSearchParams(data),
    {method: method});

    return fetch(request)
    .then(response => {
        if (response.status === 200) {
        return response.json();
        } else {
        throw new Error('Something went wrong on api server!');
        }
    })
    .then(response => {
        return response
    }).catch(error => {
        console.error(error);
    });
};

const get_products = (last_id, category) => {
    return base_request('products/lazy_load', 'GET', {id: last_id,
                                                      category: category});
};

const set_cookie = (name, value) => {
    return base_request('cookie', 'POST', {name: name,
                                           value: value})
};

const add_to_cart = (product_id, count) => {
    return base_request('user/cart', 'POST', {product_id: product_id,
                                              count: count})
}

const checkout_cart = () => {
    return base_request('user/cart', 'DELETE', {})
}

export {get_products, set_cookie, add_to_cart, checkout_cart};
