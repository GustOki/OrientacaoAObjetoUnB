const socket = io('http://localhost:8080'); // Endereço do servidor Socket.IO

// Seleciona o botão pelo ID
const button = document.getElementById('sendButton');

socket.on('connect', () => {
   console.log('Conexão estabelecida com o servidor Socket.IO');
});

// recebimentos das mensagens
socket.on('message', (data) => {
    displayMessage(data.content, data.username);
});

// recebimento de uma nova lista de usuários conectados
socket.on('update_users_event', (data) => {
    updateUserList(data.users)
});

// envio de solicitação para o servidor para que o mesmo possa devolver
// a lista de mensagens atualizada
function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value;
    socket.emit('message', message);
    messageInput.value = '';
}

function displayMessage(message, user) {
    const messageDisplay = document.getElementById('messageDisplay');
    if (messageDisplay) {
        messageDisplay.innerHTML += `<li>${message} | escrita por: ${user}</li>`;
    } else {
        console.error('Elemento messageDisplay não encontrado');
    }
}

function updateUserList(users) {
    const usersDisplay = document.getElementById('usersDisplay');
    if (usersDisplay) {
        usersDisplay.innerHTML = '';
        users.forEach(user => {
            const listItem = document.createElement('li');
            listItem.textContent = user.username;
            usersDisplay.appendChild(listItem);
        });
    } else {
        console.error('Elemento usersDisplay não encontrado');
    }
}

button.addEventListener('click', sendMessage);
