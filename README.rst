Aiogram template
================

Template for creating Python telegram bots using the Aiogram library. 🐍

🏃 How do I run it?
----------------
#. Clone this repository 🚀

    ::

        git clone https://github.com/t3m8ch/aiogram-template.git
        cd aiogram-template

#. Rename **.example.env** to **.env** 🔄

    ::

        mv .example.env .env

#. Edit the **.env** file using a text editor 📋

    ::

        TG_TOKEN=Insert_the_telegram_bot_token_here_without_spaces
        ADMINS_ID=List_the_id_of_the_administrators,separated_by_commas_without_spaces
        WEBHOOK_HOST=Insert/the/host/that/will/be/accessed/by/Telegram
        WEBHOOK_PATH=Insert/the/path/to/bot/that/will/be/accessed/by/Telegram
        WEBAPP_HOST=Insert.web.application.host
        WEBAPP_PORT=Insert_web_application_port

    To use webhook, you only need to specify the environment variable **WEBHOOK_HOST**.
    If this parameter is not specified, long polling is used. If you specify only
    this parameter, it is the default:

    ::

        WEBHOOK_PATH=/bot
        WEBAPP_HOST=localhost
        WEBAPP_PORT=3000

#. Install the necessary dependencies with the help of **poetry** 🔽

    ::

        poetry install

#. Now you can run the bot! 🎉

    ::

        poetry run bot
