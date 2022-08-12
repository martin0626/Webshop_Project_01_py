import {accessMessage} from "../alerts.js";
import {getCookie} from "../get_cookie.js";

async function Add_to_cart(){
    let button = document.querySelectorAll('#cart');
    button.forEach(addEventOnClick)

    function addEventOnClick(item){
        item.addEventListener('click', async (event)=>{
        event.preventDefault()
        let cart_number = document.getElementById('cart_number');
        let productSlug = item.getAttribute("data-product-slug");
        if (!Object.keys(sessionStorage).includes(productSlug)){
            cart_number.textContent = parseInt(cart_number.textContent) + 1;
            await accessMessage('Product Added To Cart')
        }
        console.log(Object.keys(sessionStorage).includes(productSlug), sessionStorage)
        sessionStorage.setItem(productSlug, productSlug)

        await addToCart(productSlug);
    })
    }
}

async function addToCart(slug) {
    let res = await fetch("http://127.0.0.1:8000/api/cart_add/", {
        method: 'POST',
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({slug: slug})
    });
}

Add_to_cart();
