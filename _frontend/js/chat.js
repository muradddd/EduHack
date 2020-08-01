window.innerWidth
window.innerHeight

let chat = document.querySelector(".chat");
const readMore = document.querySelector("#un");
const second = document.querySelector("#second");
let less = document.querySelector("#less");

readMore.addEventListener('click', function(e){
   second.innerHTML = `<input id="message" type="text" style="margin-top: 350px;">
    <button id="send" style="border: 1px solid #E6E6E6;
    background-color: white;
    border-radius: 5px;">Send</button>
   `;
   document.querySelector(".abel").style.display = "block";
   document.querySelector(".lesson-btn").style.display = "none";
   document.querySelector("#l").style.display = "none";
   document.querySelector("#ll").style.display = "none";
   document.querySelector("#lll").style.display = "none";
   document.querySelector("#c").style.display = "none";
   document.querySelector("#cc").style.display = "none";
   document.querySelector("#ccc").style.display = "none";
   e.target.innerHTML = "";
   less.innerHTML = "▲";
   chat.style.height = "535px";
})

// message = document.querySelector("#message").value;
// document.querySelector("#send").addEventListener('click', function(){
//     let chat_message = document.createElement("p", {'class': "chat-message"});
//     chat_message.innerHTML = "hey";
//     chat.appendChild(chat_message);
// })

less.addEventListener('click', function(e){
   second.innerHTML = "";
   document.querySelector(".abel").style.display = "none";
   document.querySelector(".lesson-btn").style.display = "initial";
   document.querySelector("#l").style.display = "initial";
   document.querySelector("#ll").style.display = "initial";
   document.querySelector("#lll").style.display = "initial";
   document.querySelector("#c").style.display = "initial";
   document.querySelector("#cc").style.display = "initial";
   document.querySelector("#ccc").style.display = "initial";
   e.target.innerHTML = "";
   readMore.innerHTML = "▼";
   chat.style.height = "100px";
})