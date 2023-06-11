import Parser, telebot, requests, os

bot = telebot.TeleBot("6191911390:AAFRVN4Yrms0lI1NXi48HFaKuLeAmZJCpGI")


@bot.message_handler(commands=["save_on_disk"])
def save_on_disk(mes):
    print(mes.text)
    if len(str(mes.text).split(" ")) >= 2:
        if str(mes.text).split(" ")[1].find("https://") != -1:
            url = str(mes.text).split(" ")[1]
            print(url)
            pages = Parser.PageList(url)
            pages.sheets = []
            pages.types = []
            pages.names = []
            pages.params["index"] = 1
            pages.data_handler()
            pages.first_sheet()
            pages.sheets_gen()
            pages.type_finder()
            pages.file_gener_pdf()

            bot.send_message(mes.chat.id, pages.title)

            names = pages.names
            print(names)
            print(pages.sheets)
            for name in names:
                with open(f"./Lists/{name}", "rb") as f:
                    bot.send_document(mes.chat.id, f)
        else:
            bot.send_message(mes.chat.id, "Invalid URL format")
    else:
        bot.send_message(mes.chat.id, "Invalid request")


@bot.message_handler(content_types=["text"])
def url_receiver(mes):
    if mes.text.find("https://") != -1 and mes.text.find("https://") == 0:
        url = mes.text
        print(url)
        pages = Parser.PageList(url)
        pages.sheets = []
        pages.types = []
        pages.names = []
        pages.params["index"] = 1
        pages.data_handler()
        pages.first_sheet()
        pages.sheets_gen()
        pages.type_finder()
        pages.file_gener_pdf()

        bot.send_message(mes.chat.id, pages.title)

        names = pages.names
        print(names)
        print(pages.sheets)
        for name in names:
            with open(f"./Lists/{name}", "rb") as f:
                bot.send_document(mes.chat.id, f)
            os.remove(f"./Lists/{name}")
    else:
        bot.send_message(mes.chat.id, "Invalid URL format")


bot.infinity_polling()
