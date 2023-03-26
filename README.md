# STicketBot
Простой бот для тикетов в дискорде использующий модальное окно для создания тикета

![Сообщение созздания тикета](https://turbovadim.ru/github/message.png)
![Модальное окно](https://turbovadim.ru/github/modal.png)
![Закрыть тикет](https://turbovadim.ru/github/close.png)

## Использование бота

### 1. Скачивание бота

Скачайте бота по ссылке https://github.com/Turbovadim/STicketBot/releases/latest/
или при помощи команды 
```
git clone https://github.com/Turbovadim/STicketBot
```
```
# Windows
python -m pip install -r requirements.txt

# Linux
pip install -r requirements.txt
```

### 2. Установка зависимостей
```
# Windows
python -m pip install -r requirements.txt

# Linux
pip install -r requirements.txt
```
### 3. Настройка конфига

Заполните **config.ini** используя ваши данные.

token - Токен бота для авторизации бота
guild_id - ID вашей дискорд группа 

support - Роль поддержки
sub_support - Вторая роль поддержки

```
# Данные вставлять без кавычек
[Auth]
token=
guild_id=
[Roles]
support=
sub_support=
```
