<?php

error_reporting(E_ALL);

// Функция для обработки ошибок
function handleErrors($errorNumber, $errorMessage, $errorFile, $errorLine)
{
    $error = "[$errorNumber] $errorMessage in $errorFile:$errorLine";
    // Добавьте здесь логирование ошибки в файл
    error_log($error);
}

// Регистрируем функцию handleErrors для обработки ошибок
set_error_handler('handleErrors');

include "./dba.php";

try {
    $table = $_GET['table'] ?? '';
    $query = $_GET['query'] ?? '';

    switch ($table) {
        case 'users':
            if ($query === 'get') {
                $usersData = getUSERS_DATA();
                http_response_code(200);
                echo json_encode(['count' => count($usersData)]);
            } else {
                http_response_code(400);
                echo json_encode(['error' => 'Invalid query parameter.']);
            }
            break;
        case 'adminstructure':
            if ($query === 'get') {
                $adminStructure = getAdminstructure()[0];
                http_response_code(200);
                echo json_encode($adminStructure);
            } else {
                http_response_code(400);
                echo json_encode(['error' => 'Invalid query parameter.']);
            }
            break;
        case 'Lotery_data':
            if ($query === 'get') {
                http_response_code(200);
                echo json_encode(getLotery_DATA());
            } else {
                http_response_code(400);
                echo json_encode(['error' => 'Invalid query parameter.']);
            }
            break;
        case 'Last_lotery':
        	if ($query == 'get'){
        		http_response_code(200);
        		echo json_encode(getLastLoteryData());
        	} elseif ($query == 'put'){
        		http_response_code(200);
        		$valuesToUpdate = json_decode($_POST["values"], true);
        		updateLotery_DATA($_POST["Lid"], $valuesToUpdate);
        	} elseif ($query == 'add'){
        		http_response_code(200);
        		$values = json_decode($_POST["values"], true);
        		addLotery_DATA($values);
        	} else{
        		http_response_code(400);
        		echo json_encode(['error' => 'Invalid query parameter.']);
        	}
        	break;

        default:
            http_response_code(400);
            echo json_encode(['error' => 'Invalid table parameter.']);
    }
} catch (\Throwable $throwable) {
    http_response_code(500);
    error_log($throwable->getMessage());
    echo json_encode(['error' => 'Internal Server Error. '.$throwable->getMessage()]);
}