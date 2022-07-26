async function accessMessage() {
    let messageBox = document.getElementById('message')
    addEventListener(onload, async () => {
        let res = await fetch("http://127.0.0.1:8000/api/alert/", {
            method: 'GET',
        });
        let data = await res.json();
        if (data['message']) {
            messageBox.textContent = data['message'];
            messageBox.style.display = 'block';
            setTimeout(() => messageBox.style.display = 'none', 3000);
        }
    })


}

accessMessage()