<?php
// Подключение к базе данных
$servername = "localhost"; // или ваш сервер базы данных
$username = "root"; // имя пользователя
$password = ""; // пароль
$dbname = "my_database"; // имя вашей базы данных

// Создаем соединение
$conn = new mysqli($servername, $username, $password, $dbname);

// Проверяем соединение
if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}

// Получаем данные из формы
$username = $_POST['username'];
$password = $_POST['password'];

// Хешируем пароль перед сохранением
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// SQL-запрос для вставки данных
$sql = "INSERT INTO users (username, pass) VALUES (?, ?)";

// Подготовка и выполнение запроса
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $username, $hashed_password);

if ($stmt->execute()) {
    echo "Регистрация успешна!";
} else {
    echo "Ошибка: " . $stmt->error;
}

// Закрываем соединение
$stmt->close();
$conn->close();
?>