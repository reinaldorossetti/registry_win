import requests
from bs4 import BeautifulSoup
from json import loads
from os import getcwd
"""
Verificador de elementos nas páginas web.
Antes de realizar seus testes vamos validar se nao quebrou os links, elements.
"""

class ElementsValidated(object):

    def __init__(self,xml):
        self.data = []
        self.result = []
        self.url = ""
        root_path = getcwd()
        path =(root_path + "\\data\\" + str(xml))
        with open(path) as data_file:
                self.data = loads(data_file.read())

    def trade_spider(self, link):

        self.url = link
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for x in self.data["elements"]:
            find = soup.findAll(x["tag"], {x["attr"]: x["value"]})
            if find:
                self.result.append("Passed : {} {} {} ".format(x["tag"], x["attr"], x["value"]))
            else:
                self.result.append("Failed : {} {} {} ".format(x["tag"], x["attr"], x["value"]))

            # for result in find:
            #     if result.string:
            #         print(result.string)

        return self.result

if __name__=='__main__':
    json_name = "elements.json"
    obj = ElementsValidated(json_name)
    url = 'https://github.com/reinaldorossetti'
    for x in obj.trade_spider(url):
        print(x)
