import {getCookie} from "../get_cookie.js";


function delete_from_cart() {
    let buttons = document.getElementsByClassName('delete_cart_element');
    Array.from(buttons).forEach(addDeleteFunc)

    function addDeleteFunc(item) {
        item.addEventListener("click", () => {
                let slug = item.getAttribute("data-product-slug");
                let price = parseInt(item.getAttribute("data-product-price"));
                let total_price_element = document.getElementById('total_price');
                let total_price = parseInt(total_price_element.getAttribute("data-total-price"));
                let end_price = total_price - price;
                let items_count_element = document.getElementById('products_count');

                items_count_element.textContent = `${parseInt(items_count_element.textContent.split(' ')[0]) - 1} items`;
                total_price_element.textContent = `BGN ${end_price}`;
                total_price_element.setAttribute('data-total-price', end_price);


                let res = fetch('http://127.0.0.1:8000/api/cart_delete_product/', {
                    method: 'POST',
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                        "Content-Type": 'application/json'
                    },
                    body: JSON.stringify({slug: slug, price: price})
                })
                item.parentNode.parentNode.parentNode.remove();
                sessionStorage.removeItem(slug)
                let cart_number = document.getElementById('cart_number');
                cart_number.textContent = parseInt(cart_number.textContent) - 1

                console.log(sessionStorage)
            }
        )
    }

}

delete_from_cart()