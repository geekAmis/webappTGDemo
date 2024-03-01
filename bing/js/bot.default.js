let bot = window.Telegram.WebApp;
bot.expand();
const { id,first_name, last_name, username, language_code } = bot.initDataUnsafe.user;
console.log(`BOT DEFAULT : Connect SUCCESS V | DefDataUser: ${id}, ${first_name}, ${last_name}, ${username}, ${language_code}`);