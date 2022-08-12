import {getCookie} from "../get_cookie.js";

async function delRequest(slug) {
    let res = await fetch("http://127.0.0.1:8000/api/delete_from_favourites/", {
        method: 'POST',
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({slug: slug})
    });

    let data = await res.json()
    document.getElementById('favourites-count').textContent = data['favourites_count'];

}

async function delFromFavourites() {
    let buttons = document.querySelectorAll('.favourites')
    buttons.forEach(addEvent)
    function addEvent(item){
        item.addEventListener('click', ()=>{
            let productSlug = item.getAttribute("data-product-slug");
            delRequest(productSlug)
            document.getElementById(productSlug).remove()
        })
    }
}

delFromFavourites()