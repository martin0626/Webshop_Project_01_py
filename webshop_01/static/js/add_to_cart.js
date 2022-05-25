async function Add_to_cart(){
    let button = document.querySelectorAll('#cart');
    button.forEach(addEventOnClick)

    function addEventOnClick(item){
        item.addEventListener('click', async ()=>{
        let productSlug = item.getAttribute("data-product-slug");
        // sessionStorage.setItem(productSlug, productSlug);
        await addToCart(productSlug)
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
