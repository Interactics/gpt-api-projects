const chatForm = document.getElementById('chat-form');
const chatBox = document.getElementById('chat-box');

// Add these lines to the top of your app.js file
const hideChatBtn = document.getElementById('hide-chat-btn');
const chatContainer = document.querySelector('.chat-container');

hideChatBtn.addEventListener('click', () => {
    chatContainer.classList.toggle('hidden');
});

chatForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const message = chatForm.elements['chat-input'].value.trim();
    if (!message) return;

    addMessage('User', message);
    chatForm.elements['chat-input'].value = '';
    
    typingIndicator.style.display = 'block'; // Show the typing indicator

    try {
        const response = await fetch('/api/generate-response', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message }),
        });

        const data = await response.json();
        addMessage('GPT', data.response);
    } catch (error) {
        console.error('Error:', error);
    }

    typingIndicator.style.display = 'none'; // Hide the typing indicator
});

function addMessage(sender, text) {
    const messageElement = document.createElement('div');
    messageElement.classList.add(sender === 'User' ? 'user-message' : 'gpt-message');

    const iconClass = sender === 'User' ? 'user-icon' : 'gpt-icon';
    messageElement.innerHTML = `
      <div>
        <span class="${iconClass}"></span>
        <strong>${sender}:</strong>
      </div>
      <p>${text}</p>`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

