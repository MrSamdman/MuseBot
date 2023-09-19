import requests, data, os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfMerger
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

class PageList:
    all_types = [".svg", ".png"]
    title = ''
    sheets = []
    id_code = ''
    fp_ext = ""
    types = []
    params = data.params
    headers = data.headers
    names = []
    names_not_pdf = []

    def __init__(self, url="https://musescore.com/user/89075/scores/4677401"):
        self.url = url
        self.title = ''
        self.sheets = []
        self.fp_ext = ""
        self.id_code = ''
        self.params = data.params
        self.headers = data.headers
        self.names = []
        self.names_not_pdf = []
        self.types = []
        self.id_code = self.url.split("/")[-1]
        self.params["id"] = self.id_code

    def first_sheet(self):
        raw = requests.get(self.url).text

        t_raw = raw[650:1000]
        t_st = t_raw.find('<meta property="og:title" content=') + 35
        t_end = t_raw.find('<meta property="og:url"') - 3
        self.title = t_raw[t_st:t_end]

        fp_st = raw.find('<link type="image/')
        fp_st = raw[fp_st:].find("href=")+fp_st+6
        fp_end = raw[fp_st:].find("/score_0") + fp_st

        self.fp_ext = raw[fp_end + 8:fp_end + 12]
        self.sheets.append(raw[fp_st:fp_end] + f'/score_0{self.fp_ext}')

    def sheets_gen(self):
        self.params["index"] = 1
        for i in range(100):
            sheet_garbage = requests.get('https://musescore.com/api/jmuse', params=self.params, headers=self.headers)
            self.params["index"] = str(int(self.params["index"]) + 1)
            list_link = sheet_garbage.text[int(sheet_garbage.text.find("https://")):-3]

            req = requests.get(list_link)

            if req.status_code != 200:
                break
            print(f"Pages status code: {req.status_code}")
            self.sheets.append(list_link)

    def type_finder(self):
        for num, sheet in enumerate(self.sheets):
            print(sheet)
            for t in self.all_types:
                if str(sheet).find(t) != -1:
                    self.types.append(t)

    def file_gener_pdf(self):
        for num, sheet in enumerate(self.sheets):
            ext = self.types[num]
            name = f'{self.title+str(num)}{ext}'
            name_pdf = f'{self.title+str(num)}.pdf'

            with open(name, 'wb') as f:
                print(name)
                f.write(requests.get(sheet).content)

            if ext == ".svg":
                self.names.append(name_pdf)
                renderPDF.drawToFile(svg2rlg(name), name_pdf)
                os.remove(name)
            else:
                self.names.append(name_pdf)
                image_1 = Image.open(name)
                im_1 = image_1.convert('RGB')
                im_1.save(f"{name_pdf}")
                os.remove(name)

            print("CONVERT. DONE!")

        if self.names:
            merger = PdfMerger()
            for pdf in self.names:
                merger.append(pdf)
            merger.write(f"1.pdf")
            merger.close()

            for name in self.names:
                os.remove(name)

            try:
                os.rename(f"./1.pdf", f"./Lists/1.pdf")
            except FileExistsError:
                os.remove(f"1.pdf")
                print("FILE EXISTS")

        if self.names_not_pdf:
            for name in self.names_not_pdf:
                try:
                    os.rename(f"./{name}", f"./Lists/{name}")
                except FileExistsError:
                    os.remove(f"{name}")
                    print("FILE EXISTS")


# page = PageList(input("URL: "))
# page.first_sheet()
# page.sheets_gen()
# page.type_finder()
# page.file_gener_pdf()
#
# print(page.sheets)