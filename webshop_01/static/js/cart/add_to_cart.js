function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function Add_to_cart(){
    let button = document.querySelectorAll('#cart');
    button.forEach(addEventOnClick)

    function addEventOnClick(item){
        item.addEventListener('click', async ()=>{
        let cart_number = document.getElementById('cart_number');
        let productSlug = item.getAttribute("data-product-slug");
        if (!Object.keys(sessionStorage).includes(productSlug)){
            cart_number.textContent = parseInt(cart_number.textContent) + 1;
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
