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