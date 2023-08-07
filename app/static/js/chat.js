const sendBtn = document.getElementById("send-btn");
const inputMessage = document.getElementById("input-message");
const chatsContainer = document.getElementById("chats-container");
const roomsContainer = document.getElementById("rooms");
const sidebarToggler = document.getElementById("sidebar-toggler");
const sidebar = document.getElementById("sidebar");
// styling
sidebarToggler.addEventListener("click", () => {
  sidebar.classList.toggle("show-sidebar");
  if(sidebarToggler.name == "chevron-forward-outline"){
    sidebarToggler.name = "chevron-back-outline"
  }else{
    sidebarToggler.name = "chevron-forward-outline"
  }
})
chatsContainer.addEventListener("click", (e) => {
  sidebar.classList.remove("show-sidebar");
})

// 
const socket = io("http://192.168.228.157:5000/");

const joinRoom = (room) => {
  socket.emit("join_room", { room: room });
};
socket.on("join_room_message", (data) => {
  sendBtn.classList.remove("disabled");
});

const rooms = () => {
  roomsContainer.querySelectorAll(".room").forEach((room) => {
    room.classList.remove("bg-primary")
    room.classList.remove("text-white")
    room.classList.add("w3-pale-green")
    room.addEventListener("click", () => {
      rooms();
      joinRoom(room.dataset.room);
      localStorage.setItem('room', room.dataset.room);
      room.classList.remove("w3-pale-green")
      room.classList.add('bg-primary')
      room.classList.add("text-white")
    });
  });
};

const Rooms = (data) => {
  roomsContainer.innerHTML = "";
  for (let x in data) {
        let room = document.createElement("div");
        room.class = `room d-flex justify-content-start align-items-center w3-pale-green w3-hover-shadow px-2 mb-2`;
        room.setAttribute("class", room.class);
        room.profile = `<div class="img-fluid profile-text rounded-circle me-2 p-1 bg-success d-flex justify-content-center align-items-center">
      <h5 class="text-uppercase">${x[0]}</h5></div>`;
        room.bio = `<div class=""><b class="d-block">${x}</b><small>Lorem ipsum dolor sit </small>
    </div>`;
        room.dataset.room = data[x].room;
        room.innerHTML = room.profile + room.bio;
        roomsContainer.append(room);
  }
  rooms();
};

// Load Room
let username = localStorage.getItem("username");
socket.emit("load_room", { username: username });
socket.on("load_room_message", (data) => {
  localStorage.setItem("room", data.room);
  Rooms(data.rooms);
});

// Send Message
sendBtn.addEventListener("click", () => {
  if (inputMessage !== "") {
    socket.emit("send_message", {
      message: inputMessage.value,
      room: localStorage.getItem("room"),
    });
    inputMessage.value = "";
  }
});

// Sender
const chatProfileClass = `img-fluid rounded-circle profile-image p-1 border border-dark`;
const chatMessageClass = `shadow chats-message rounded-4 p-2 border  text-white`;
const senderChats = (data) => {
  const chat = document.createElement("div");
  chat.class = `sender d-flex mb-3 mt-2`;
  chat.setAttribute("class", chat.class);
  chat.profile = `<div title="${data.username}" class="img-fluid profile-text rounded-circle me-2 p-1 w3-green d-flex justify-content-center align-items-center">
  <h5 class="text-uppercase">${data.username[0]}</h5></div>`;
  chat.message = `<div class="${chatMessageClass} w3-green"><small class="d-block text-end bold">${data.time}</small><small class="message"></small></div></div>`;
  chat.innerHTML = chat.profile + chat.message;
  chat.querySelector(".message").innerText = data.message;
  chatsContainer.append(chat);
};

// Receiver
const receiveChats = (data) => {
  const chat = document.createElement("div");
  chat.class = `receiver d-flex mb-3 mt-2`;
  chat.setAttribute("class", chat.class);
  chat.profile = `<div title="${data.username}" class="img-fluid profile-text rounded-circle me-2 p-1 w3-blue d-flex justify-content-center align-items-center">
  <h5 class="text-uppercase">${data.username[0]}</h5></div>`;
  chat.message = `<div class="${chatMessageClass} w3-blue me-2"><small class="d-block text-end bold">${data.time}</small><small class="message"></small></div></div>`;
  chat.innerHTML = chat.message+chat.profile;
  chat.querySelector(".message").innerText = data.message;
  chatsContainer.append(chat);
};

// Receive Message
socket.on("receive_message", (data) => {
  let username = localStorage.getItem("username");
  console.log(data)
  if (username === data.username) {
    senderChats(data);
  } else {
    receiveChats(data);
  }
});
