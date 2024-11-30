const togglePassword = document.getElementById('toggle-password');
const passwordInput = document.getElementById('password');

togglePassword.addEventListener('click', function () {
    // Переключаем тип input между 'password' и 'text'
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    
    // Меняем иконку в зависимости от состояния
    this.querySelector('i').classList.toggle('fa-eye'); // Открытый глаз
    this.querySelector('i').classList.toggle('fa-eye-slash'); // Закрытый глаз
});

function handleSubmit(event) {
    event.preventDefault();
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const messageElement = document.getElementById('messageElement')

    try {
        const response = fetch('/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
        });
  
        if (!response.ok) {
          //const errorData = response.json();
          messageElement.textContent = /*errorData.message ||*/ 'Ошибка регистрации';
          messageElement.style.color = 'red';
          return;
        }
  
        const data = response.json();
        messageElement.textContent = data.message;
        // Optionally reset the form:
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
      } catch (error) {
        messageElement.textContent = 'Ошибка соединения с сервером';
        messageElement.style.color = 'red';
        console.error("Error:", error); // Log the error to the console for debugging.
      }
}