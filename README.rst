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

        mv .exapmple.env .env

#. Edit the **.env** file using a text editor 📋

    ::

        TG_TOKEN=Insert_the_telegram_bot_token_here_without_spaces
        ADMINS_ID=list_the_id_of_the_administrators,separated_by_commas_without_spaces

#. Install the necessary dependencies with the help of **poetry** 🔽

    ::

        poetry install

#. Now you can run the bot! 🎉

    ::

        poetry run bot
