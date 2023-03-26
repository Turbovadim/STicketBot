# STicketBot
Простой бот для тикетов в дискорде использующий модальное окно для создания тикета

![Сообщение созздания тикета](https://turbovadim.ru/github/message.png)
![Модальное окно](https://turbovadim.ru/github/modal.png)
![Закрыть тикет](https://turbovadim.ru/github/close.png)

## Использование бота

### 1. Скачивание бота

Скачайте бота по ссылке https://github.com/Turbovadim/STicketBot/releases/latest/

Или клонируйте репозиторий используя данную команду
```bash
git clone https://github.com/Turbovadim/STicketBot
```

### 2. Установка зависимостей
```bash
# Windows
python -m pip install -r requirements.txt

# Linux
pip install -r requirements.txt
```
### 3. Настройка конфига

Заполните **config.ini** используя ваши данные.

```ini
# Данные вставлять без кавычек
[Auth]
# Токен бота для авторизации
token=
# ID вашей дискорд группы
guild_id=
[Roles]
# Роль поддержки
support=
# Вторая роль поддержки
sub_support=
```

### 4. Запуск бота

Запустите бота при помощи команды
```bash
python bot.py
```
