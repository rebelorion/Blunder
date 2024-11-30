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

document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.getElementById('submitBtn');
    const messageElement = document.getElementById('message');
  
    submitBtn.addEventListener('click', async () => {
      messageElement.textContent = ''; // Очищаем предыдущее сообщение
  
      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;
  
  
      try {
        const response = await fetch('/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
        });
  
        if (!response.ok) {
          const errorData = await response.json();
          messageElement.textContent = errorData.message || 'Ошибка регистрации';
          messageElement.style.color = 'red';
          return;
        }
  
        const data = await response.json();
        messageElement.textContent = data.message;
        // Optionally reset the form:
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
      } catch (error) {
        messageElement.textContent = 'Ошибка соединения с сервером';
        messageElement.style.color = 'red';
        console.error("Error:", error); // Log the error to the console for debugging.
      }
    });
  
    // Toggle Password Visibility (keep this part)
    const togglePassword = document.getElementById('toggle-password');
    const passwordInput = document.getElementById('password');
  
    togglePassword.addEventListener('click', function () {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        this.querySelector('i').classList.toggle('fa-eye');
        this.querySelector('i').classList.toggle('fa-eye-slash');
    });
  });