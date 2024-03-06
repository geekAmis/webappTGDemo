<?php




$config_db = array(
    "host" => "",
    "user" => "",
    "password" => "",
    "database" => ""
);

// Создаем PDO объект для подключения к базе данных
$dsn = 'mysql:host=' . $config_db['host'] . ';dbname=' . $config_db['database'];
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_EMULATE_PREPARES => false,
];
try {
    $pdo = new PDO($dsn, $config_db['user'], $config_db['password'], $options);
} catch (PDOException $e) {
    die("Ошибка подключения к базе данных: " . $e->getMessage());
    exit;
}

include "./db_class.php";

$dbManager = new DatabaseManager($pdo);

function getUSERS_DATA()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('USERS_DATA', ' Tid, balance');
    return $users;
}



function getUser_DATA()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('User_DATA', ' Tid, first_name, last_name, username, balance, owner_status, registration_date');
    return $users;
}

function getUserFastCart()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('UserFastCart', ' Tid, total_tickets, total_wins');
    return $users;
}

function getTickets()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('Tickets', ' ticketid, hashCode, ownerTid, Lid');
    return $users;
}

function getLotery_DATA()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('LoteryDATA', 'Lid, prize, win_hash, winnersTid, maxTicketsForOnePerson, amount, Datem');
    return $users;
}

function getLotery_Descript()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('LoteryDescript', ' Lid, About, how_to_play, prizes, terms_conditions, prize_pool');
    return $users;
}

function getLastLoteryData()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('LastLoteryData', ' Lid, Type, prize, Datem, winTid');
    return $users;
}

function getCartTickets()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('CartTickets', ' Tid, ticketid, amount');
    return $users;
}

function getAdminstructure()
{
    global $dbManager;

    $users = $dbManager->getValuesFromTable('Adminstructure', ' Botname, Balance, WebURL, Owners_Tids');
    return $users;
}

function updateLotery_DATA($Lid, $valuesToUpdate)
{
    global $dbManager;

    //$valuesToUpdate = [
    //    ['col' => 'name', 'value' => $name],
    //    ['col' => 'email', 'value' => $email]
    //];
    $condition = 'Lid = ?';
    $affectedRows = $dbManager->updateValueInTable('users', $valuesToUpdate, $condition, [$Lid]);
    return $affectedRows;
}


// Функция для добавления пользователя в таблицу users
function addLotery_DATA($values)
{
    global $dbManager;
    //$values = [
    //    ['col' => 'name', 'value' => $name],
    //    ['col' => 'email', 'value' => $email]
    //];
    $affectedRows = $dbManager->addValueToTable('Lotery_DATA', $values);
    return $affectedRows;
}


?>