# Aiogram template

Template for creating Python telegram bots using the Aiogram library. 🐍

## 🏃 How do I run it?

### 1. Clone this repository 🚀
```bash
git clone https://github.com/t3m8ch/aiogram-template.git
cd aiogram-template
```

### 2. Copy **-example.env* to *.env* 🔄 
```bash
cp minimal-example.env .env
# OR
cp full-example.env .env
```

### 3. Edit the *.env* file using a text editor 📋
If you use webhooks and use the minimal example,
you need to add the **TG_WEBHOOK_HOST** parameter,
which specifies the host to which Telegram will send requests.

If you want to use **Redis** to store the states, specify the **REDIS_HOST** 
parameter. Otherwise **MemoryStorage** will be used.

Default values:
```dotenv
TG_SKIP_UPDATES=NO
TG_WEBHOOK_PATH=/bot

WEBAPP_HOST=localhost
WEBAPP_PORT=3000

LOG_LEVEL=INFO

REDIS_PORT=6379

DB_URL="postgresql+asyncpg://localhost/telegram_bot"
```

Valid values of **TG_SKIP_UPDATES**: `YES/Y/TRUE/1` or `NO/N/FALSE/0`

Webhooks can be used without setting SSL options if you use Certbot 
certificates or a certificate purchased from a Certificate Authority 
or if you use **Ngrok**.

### 4. Install the necessary dependencies with the help of **poetry** 🔽
```bash
poetry install
```

### 5. Now you can run the bot! 🎉
```bash
poetry run python3 bot
```
