const tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = "var(--tg-theme-text-color)";
tg.MainButton.color = "var(--tg-theme-bg-color)";
//tg.MainButton.setText(`Корзина`);


function changeCount(id,per=true){
  let MaxItem = 9
  try{
    console.log(document.getElementById(`counter_${id}`));
    if (per && per < MaxItem-1){
      document.getElementById(`counter_${id}`).innerHTML = parseInt(document.getElementById(`counter_${id}`).innerHTML)+1
    }else if (!per && parseInt(document.getElementById(`counter_${id}`).innerHTML)>0){
      document.getElementById(`counter_${id}`).innerHTML = parseInt(document.getElementById(`counter_${id}`).innerHTML)-1
    }
  }catch{}
  
}

function createItemElement(item) {
  let itemImage = item.image;
  let itemName = item.name;
  let itemPrice = item.price;
  let itemId = item.product_id.replace(/[^a-z0-9_-]/gi, '').substring(0, 20);
  let itemMax = item.count_on_place;

  const itemDiv = document.createElement('div');
  itemDiv.classList.add('item');
  itemDiv.id = itemMax;

  const itemImg = document.createElement('img');
  itemImg.setAttribute('src', itemImage);
  itemImg.setAttribute('alt', '');
  itemImg.classList.add('img');

  const itemNameDiv = document.createElement('div');
  itemNameDiv.classList.add('item-name');
  itemNameDiv.textContent = itemName;

  const itemPriceDiv = document.createElement('div');
  itemPriceDiv.classList.add('item-price');
  itemPriceDiv.textContent = `${itemPrice} ₽`;

  const counterDiv = document.createElement('div');
  counterDiv.classList.add('counter');
  counterDiv.setAttribute('id', `counter_${itemId}`);
  counterDiv.innerHTML = '0';

  itemDiv.appendChild(counterDiv);
  itemDiv.appendChild(itemImg);
  itemDiv.appendChild(itemNameDiv);
  itemDiv.appendChild(itemPriceDiv);

  const btnMinus = document.createElement('button');
  btnMinus.classList.add('btn-rem');
  btnMinus.textContent = '-';
  btnMinus.setAttribute('product-id', `${itemId}`);
  btnMinus.addEventListener("click",changeCount(itemId,false));

  const btnPlus = document.createElement('button');
  btnPlus.classList.add('btn-add');
  btnPlus.textContent = '+';
  btnPlus.setAttribute('product-id', `${itemId}`);
  btnPlus.addEventListener("click",changeCount(itemId));

  itemDiv.appendChild(btnMinus);
  itemDiv.appendChild(btnPlus);
  

  return itemDiv;
}

function addPage(page=0){
  fetch('data/product_list.json')
    .then((response) => response.json())
    .then((data) => {
        // Обработать полученные данные
        data.items.forEach(item => {
            console.log(item);
            document.querySelector('.inner').appendChild((createItemElement(item)));
        });

    })
    .catch((error) => {
        console.log('Ошибка чтения файла:', error);
    });
}


function ShowMainButton(text) {
  tg.MainButton.setText(`${text}`);
}
function UpdateMainButton(text){
  g.MainButton.hide();
  ShowMainButton(text);
}



Telegram.WebApp.onEvent("mainButtonClicked", function () {

});