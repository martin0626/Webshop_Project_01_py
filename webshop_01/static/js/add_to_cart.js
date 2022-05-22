function Add_to_cart(){
    let button = document.querySelectorAll('#cart');
    button.forEach(addEventOnClick)

    function addEventOnClick(item){
        item.addEventListener('click', ()=>{
        let productId = item.getAttribute("data-product-id");
        sessionStorage.setItem(productId, productId);
    })
    }
}

Add_to_cart()