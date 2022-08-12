import {getCookie} from "../get_cookie.js";

async function addRequest(slug) {
    let res = await fetch("http://127.0.0.1:8000/api/add_to_favourites/", {
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

async function addToFavourites() {
    let buttons = document.querySelectorAll('.favourites')
    buttons.forEach(addEvent)
    function addEvent(item){
        item.addEventListener('click', ()=>{
            let productSlug = item.getAttribute("data-product-slug");
            addRequest(productSlug)

        })
    }
}

addToFavourites()
