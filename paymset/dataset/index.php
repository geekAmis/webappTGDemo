<?php
// Проверка, что данные были отправлены методом GET
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Чтение данных из GET-запроса
    $getData = $_GET;

    // Сохранение данных в файл с именем, основанным на пользовательском ID
    $userId = $getData['ids'];
    $fileName = 'user_' . $userId . '.txt';
    $filePath = __DIR__ . '/' . $fileName;

    // Запись данных в файл
    $fileContent = json_encode($getData, JSON_PRETTY_PRINT);
    file_put_contents($filePath, $fileContent);

    // Ответ для клиента
    http_response_code(200);
    echo json_encode(['message' => 'Data saved successfully']);
} else {
    // Ответ для клиента, если данные не были отправлены методом GET
    http_response_code(400);
    echo json_encode(['message' => 'Invalid request']);
}
?>