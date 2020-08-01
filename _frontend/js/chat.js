let chat = document.querySelector(".chat");

document.querySelector(".chat-text").addEventListener('click', function (e) {
    chat.style.height = "500px";
    e.target.style.display = "flex"
})