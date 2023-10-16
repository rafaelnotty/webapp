const chatForm = document.getElementById("chat-form");
const chatMessages = document.getElementById("chat-messages");
const messageInput = document.getElementById("message");

// Función para mostrar mensajes en el chat
function showMessage(sender, message) {
    const messageElement = document.createElement("p");
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatMessages.appendChild(messageElement);
}

// Función para limpiar el cuadro de texto
function clearMessageInput() {
    messageInput.value = "";
}

// Agregar un listener para el envío del formulario
chatForm.addEventListener("submit", async function(event) {
    event.preventDefault();
    const message = messageInput.value;
    if (message) {
        showMessage("User", message);
        clearMessageInput();

        // Enviar el mensaje al servidor
        const response = await fetch('/enviar-mensaje/', {
            method: 'POST',
            body: JSON.stringify({mensaje: message}),
            headers: {'Content-Type': 'application/json'}
        });
        const data = await response.json();
        showMessage("Data-Scientist IA", data.respuesta);
    }
});
