import requests
import os


def download_file(url, size=2000, file_name="report.pdf"):
    """
    Passa a url do pdf e vai criar um pdf no diretorio com mesmo metadata.
   
    :param url: url do arquivo para download.
    :param size: tamanho maximo do arquivo.
    :param file_name: nome do arquivo
    :return: cria o pdf e retorna True.
    """

    url_download = url
    request = requests.get(url_download, stream=True)

    # tamanho em bytes.
    size_pdf = size
    directory = "c:\\tmp"

    # verifica se o diretorio existe senao cria.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    return write_pdf(os.path.join(directory, file_name), request, size_pdf)


def write_pdf(path, request, size):

    with open(path, 'wb') as fd:
        for chunk in request.iter_content(size):
            fd.write(chunk)

    return True

download_file('http://www.dcc.ufrj.br/~fabiom/mab225/pythonbasico.pdf')
