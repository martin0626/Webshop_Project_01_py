async function getFavouritesCount(){
    try{
        let res = await fetch("http://127.0.0.1:8000/api/add_to_favourites/", {
            method: 'GET',
        });

        let data = await res.json()
        document.getElementById('favourites-count').textContent = data['favourites_count'];
    }
    catch{}
}

getFavouritesCount()
