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