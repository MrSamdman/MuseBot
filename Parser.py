import requests, data, os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


class PageList:
    title = 'Doctor Who Main Theme 2005 - 2007'
    sheets = []
    id_code = '4677401'
    embed_url = 'https://musescore.com/user/89075/scores/4677401/embed'
    params = data.params
    headers = data.headers
    ext = ''
    types = []
    names = []

    def __init__(self, url="https://musescore.com/user/89075/scores/4677401"):
        self.url = url

    def data_handler(self):
        self.embed_url = self.url + "/embed"
        self.id_code = self.url.split("/")[-1]
        if self.url.split("/")[-1] == "":
            self.id_code = self.url.split("/")[-2]
        self.params["id"] = self.id_code

    def first_sheet(self):
        raw = requests.get(self.url)

        title_raw = raw.text[650:1000]
        title_start = title_raw.find('<meta property="og:title" content=')+35

        title_end = title_raw.find('<meta property="og:url"') - 3
        self.title = title_raw[title_start:title_end]

        fp_raw = requests.get(self.embed_url).text
        fp_start = fp_raw.find('<img src="https://musescore.com/static/musescore/scoredata/g')+10
        fp_end = fp_raw[fp_start:].find("/score_0") + fp_start

        self.ext = fp_raw[fp_end + 8:fp_end + 12]
        print(f"First page ext.: {self.ext}")
        self.sheets.append(fp_raw[fp_start:fp_end] + f'/score_0{self.ext}')

    def sheets_gen(self, save_on_disk: bool = False):
        for i in range(100):

            list_garbage = requests.get('https://musescore.com/api/jmuse', params=self.params, headers=self.headers)
            self.params["index"] = str(int(self.params["index"]) + 1)
            list_link = list_garbage.text[int(list_garbage.text.find("https://")):-3]

            req = requests.get(list_link)
            print(req.status_code)
            if req.status_code != 200:
                break

            self.sheets.append(list_link)

    def type_finder(self):
        for num, sheet in enumerate(self.sheets):
            if num == 0:
                self.types.append(self.ext)
            else:
                ext_st = str(sheet).find("score_") + 7
                self.types.append(str(sheet)[ext_st:ext_st+4])
                print(str(sheet)[ext_st:ext_st+4])

    def file_gener_pdf(self):

        for num, file in enumerate(self.sheets):
            ext = self.types[num]
            name = f'{self.title+str(num)}{ext}'
            name_pdf = f'{self.title+str(num)}.pdf'

            if ext == ".svg":

                self.names.append(name_pdf)
                with open(name, 'wb') as f:
                    print(name)
                    f.write(requests.get(file).content)

                drawing = svg2rlg(name)
                renderPDF.drawToFile(drawing, name_pdf)

                print("CONVERT. DONE!")
                os.remove(name)
            else:
                with open(name, 'wb') as f:
                    print(name)
                    f.write(requests.get(file).content)
                    self.names.append(name)
# page = PageList(input("URL: "))
# page.data_handler()
# page.first_sheet()
# page.sheets_gen()
# page.type_finder()
#
# print(page.sheets)
# print(page.types)