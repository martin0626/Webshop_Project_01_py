
function clear_on_logout() {
    let logoutBtn = document.getElementById('Logout')
    try {
        logoutBtn.addEventListener("click", () => {
            sessionStorage.clear()
        })
    } catch (TypeError) {
    }
}



clear_on_logout()