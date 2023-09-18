import Parser, telebot, requests, os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_API"))


@bot.message_handler(commands=["save_on_disk"])
def save_on_disk(mes):
    print(mes.text)
    if len(str(mes.text).split(" ")) >= 2:
        if str(mes.text).split(" ")[1].find("https://musescore.com/") != -1:
            url = str(mes.text).split(" ")[1]
            print(url)

            pages = Parser.PageList(url)
            pages.first_sheet()
            pages.sheets_gen()
            pages.type_finder()
            pages.file_gener_pdf()

            bot.send_message(mes.chat.id, pages.title)

            print(pages.sheets)

            with open(f"./Lists/{pages.title}.pdf", "rb") as f:
                bot.send_document(mes.chat.id, f)

            if len(pages.names_not_pdf) > 0:
                names = pages.names_not_pdf
                for name in names:
                    with open(f"./Lists/{name}", "rb") as f:
                        bot.send_document(mes.chat.id, f)
        else:
            bot.send_message(mes.chat.id, "Invalid URL format")
    else:
        bot.send_message(mes.chat.id, "Invalid request")


@bot.message_handler(content_types=["text"])
def url_receiver(mes):
    if mes.text.find("https://musescore.com/") != -1:
        url = mes.text
        print(url)
        bot.send_message(mes.chat.id, "Получил ссылку на MuseScore. Начинаю обработку файлов!")

        try:
            pages = Parser.PageList(url)
            pages.first_sheet()
            pages.sheets_gen()
            pages.type_finder()
            pages.file_gener_pdf()

            bot.send_message(mes.chat.id, pages.title)

            print(pages.sheets)

            with open(f"./Lists/1.pdf", "rb") as f:
                bot.send_document(mes.chat.id, f)
            os.remove(f"./Lists/1"
                      f".pdf")

            if pages.names_not_pdf:
                names = pages.names_not_pdf
                for name in names:
                    with open(f"./Lists/{name}", "rb") as f:
                        bot.send_document(mes.chat.id, f)
                    os.remove(f"./Lists/{name}")

        except Exception:
            bot.send_message(mes.chat.id, "Во время работы произошла ошибка! Обратитесь к администратору.")
            raise


bot.infinity_polling()
