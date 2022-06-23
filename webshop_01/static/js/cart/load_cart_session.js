async function load_cart_session() {
    try {
        let res = await fetch("http://127.0.0.1:8000/api/get_cart_items/", {
            method: 'GET',
        });

        let data = await res.json();
        for (let index in data) {
            let item = data[index];
            if (!Object.keys(sessionStorage).includes(item)) {
                sessionStorage.setItem(item, item);

            }
        }
    } catch {
        console.log('asd')
    }

}

load_cart_session();
