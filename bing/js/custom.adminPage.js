function addRowToTable(tableId, id, type, amount, date) {
  const table = document.getElementById(tableId);
  const tbody = table.getElementsByTagName('tbody')[0];

  // Создаем новую строку
  const newRow = document.createElement('tr');
  newRow.classList.add(
    "border-b",
    "transition-colors",
    "hover:bg-muted/50",
    "data-[state=selected]:bg-muted"
  );

  // Добавляем ячейки в строку и заполняем данными
  const cell1 = document.createElement('td');
  cell1.classList.add("p-4", "align-middle", "[&amp;:has([role=checkbox])]:pr-0");
  cell1.innerHTML = id;
  newRow.appendChild(cell1);

  const cell2 = document.createElement('td');
  cell2.classList.add("p-4", "align-middle", "[&amp;:has([role=checkbox])]:pr-0");
  cell2.innerHTML = type;
  newRow.appendChild(cell2);

  const cell3 = document.createElement('td');
  cell3.classList.add("p-4", "align-middle", "[&amp;:has([role=checkbox])]:pr-0");
  cell3.innerHTML = amount;
  newRow.appendChild(cell3);

  const cell4 = document.createElement('td');
  cell4.classList.add("p-4", "align-middle", "[&amp;:has([role=checkbox])]:pr-0");
  cell4.innerHTML = date;
  newRow.appendChild(cell4);

  // Добавляем строку в таблицу
  tbody.appendChild(newRow);
}

function changeBOTNAME(bot_name){
  changeElementTextById(bot_name,"bot_name")
}
function changeUSERS(count){
  changeElementTextById(count,"INT_users")
}
function changeLOTERRI(count){
  changeElementTextById(count,"INT_loterri")
}
function changeBALANCE(count){
  changeElementTextById(count,"INT_balance")
}