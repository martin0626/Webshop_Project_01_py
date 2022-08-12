export async function accessMessage(msg) {
    let messageBox = document.getElementById('message')
    messageBox.textContent = msg;
    messageBox.style.display = 'block';
    setTimeout(() => messageBox.style.display = 'none', 3000);
    console.log('asd')
}
