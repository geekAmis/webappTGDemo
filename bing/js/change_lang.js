// THIS CODE MUST BE BEFORE bot.default.js !!!! ALLWAYS !!!!!!!!!!!!!!

function changeLangCode() {
    langs = ["ru", "en"];
    thisLang = document.documentElement.getAttribute("lang");

    // Находим все элементы с атрибутом translate
    var elementsWithTranslate = document.querySelectorAll("[translate]");

    for (var i = 0; i < elementsWithTranslate.length; i++) {
        var element = elementsWithTranslate[i];
        var currentLang = element.getAttribute("translate");
        var currentText = element.textContent;

        // Меняем местами значение атрибута translate и текущего текста элемента
        element.setAttribute("translate", currentText);
        element.textContent = currentLang;
    }

    // Изменение языка для примера (в реальности это делается с помощью плагина или библиотеки)
    for (var i = 0; i < langs.length; i++) {
        if (langs[i] == thisLang) {
            if (i + 1 <= langs.length) {
                document.documentElement.setAttribute("lang", langs[i + 1]);
            } else {
                document.documentElement.setAttribute("lang", langs[i - 1]);
            }
        }
    }
}

function StandartizationLanguage() {
    if (document.documentElement.getAttribute("lang") !== language_code) {
        // Default document.documentElement.getAttribute("lang") == "ru" ALLWAYS
        changeLangCode();
    }
    console.log("Language STANDARTIZATE: SUCCESS V");
}
