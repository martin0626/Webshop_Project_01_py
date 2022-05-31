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


function delete_from_cart() {
    let buttons = document.getElementsByClassName('delete_cart_element');
    Array.from(buttons).forEach(addDeleteFunc)

    function addDeleteFunc(item) {
        item.addEventListener("click", () => {
                let slug = item.getAttribute("data-product-slug");
                let res = fetch('http://127.0.0.1:8000/api/cart_delete_product/', {
                    method: 'POST',
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                        "Content-Type": 'application/json'
                    },
                    body: JSON.stringify({slug: slug})
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