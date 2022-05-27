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
        console.log(Object.keys(sessionStorage).includes(productSlug))
        sessionStorage.setItem(productSlug, productSlug);
        // sessionStorage.setItem(productSlug, productSlug);
        await addToCart(productSlug);
    })
    }
}

async function addToCart(slug) {
    let res = await fetch("http://127.0.0.1:8000/api/cart_add/", {
        method: 'POST',
        headers: {"Content-Type": 'application/json'},
        body: JSON.stringify({slug: slug})
    });
}

Add_to_cart();
