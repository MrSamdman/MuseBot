import Parser, telebot, requests, os

bot = telebot.TeleBot("6191911390:AAFRVN4Yrms0lI1NXi48HFaKuLeAmZJCpGI")


@bot.message_handler(content_types=["text"])
def url_receiver(mes):
    if mes.text.find("https://") != -1:
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
            with open(name, "rb") as f:
                bot.send_document(mes.chat.id, f)
            os.remove(name)

        print(pages.sheets, pages.title)
        sheets = []
        names = []
    else:
        bot.send_message(mes.chat.id, "Invalid URL format")


bot.infinity_polling()
