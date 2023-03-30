const messageForm = document.getElementById('message-form');
const messages = document.getElementById('messages');
const userInput = document.getElementById('user-input');

messageForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const userText = userInput.value.trim();
    if (!userText) return;

    displayMessage(userText, 'user');
    userInput.value = '';

    const response = await fetchChatGPTResponse(userText);
    displayMessage(response, 'chatgpt');
});

async function fetchChatGPTResponse(message) {
    try {
        const apiKey = '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';
        const apiUrl = 'https://api.openai.com/v1/engines/davinci-codex/completions';

        const headers = {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        };

        const data = {
            prompt: `User: ${message}\nChatGPT:`,
            max_tokens: 100,
            n: 1,
            stop: null,
            temperature: 0.8,
            top_p: 1,
            frequency_penalty: 0,
            presence_penalty: 0
        };

        const response = await axios.post(apiUrl, data, { headers });
        const chatGPTResponse = response.data.choices[0].text.trim();

        return chatGPTResponse;
    } catch (error) {
        console.error('Error fetching ChatGPT response:', error);
        return 'Error: Unable to communicate with ChatGPT.';
    }
}
function displayMessage(message) {
  const messages = document.getElementById('messages');
  const newMessage = document.createElement('div');
  
  newMessage.textContent = message.content;
  newMessage.classList.add(message.role === 'user' ? 'message--user' : 'message--bot');
  
  messages.appendChild(newMessage);
}


