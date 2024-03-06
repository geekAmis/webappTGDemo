<?



class DatabaseManager
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    // Функция для получения значений из таблицы
    public function getValuesFromTable($tableName, $columns = '*', $conditions = [])
    {
        $placeholders = implode(',', array_fill(0, count($conditions), '?'));
        $query = "SELECT $columns FROM $tableName WHERE 1=1" . ($conditions ? ' AND ' . implode(' AND ', $conditions) : '');

        $stmt = $this->pdo->prepare($query);
        $stmt->execute($conditions + array_values($conditions));

        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    // Функция для добавления значения в таблицу
    public function addValueToTable($tableName, $values)
    {
        $placeholders = implode(',', array_fill(0, count($values), '?'));
        $query = "INSERT INTO $tableName (${implode(", ", array_keys($values))}) VALUES ($placeholders)";

        return $this->pdo->exec($query, array_values($values));
    }

    // Функция для обновления значения в таблице
    public function updateValueInTable($tableName, $valuesToUpdate, $condition)
    {
        $setClause = implode(', ', array_map(function ($value) {
            return $value['col'] . '=' . $value['value'];
        }, array_columns($valuesToUpdate)));

        $query = "UPDATE $tableName SET $setClause WHERE $condition";

        return $this->pdo->exec($query, array_values(array_column($valuesToUpdate, 'value')));
    }

    // Функция для удаления значения из таблицы
    public function deleteValueFromTable($tableName, $condition)
    {
        $query = "DELETE FROM $tableName WHERE $condition";

        return $this->pdo->exec($query, array_values(array_column($conditions, 'value')));
    }
}

?>