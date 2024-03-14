import requests
import urllib3
from bs4 import BeautifulSoup
import os
import re
import PyPDF2
import json
import shutil

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
PATH = os.path.join(os.path.dirname(__file__), 'bulletins')


def get_cve_list():
    name_list = os.listdir(PATH)
    cve_list = []
    cve_list_repeat = []
    for name in name_list:
        pdf_file = open(f'{PATH}/{name}', 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()

        data = ''
        for i in range(number_of_pages):
            page = read_pdf.getPage(i)
            page_content = page.extractText()
            data1 = json.dumps(page_content)
            data += data1
        pdf_file.close()

        rez = ''
        for n, item in enumerate(data, start=0):
            if item != '\\':
                rez += data[n]

        result = ''
        for n, item in enumerate(rez, start=0):
            if item != 'n':
                result += rez[n]
        rez1 = result.replace(" ", "")

        regex = re.findall(r'CVE-\d{4}-\d{4,8}', rez1)
        for cve in regex:
            cve_list_repeat.append(cve)
    for item in cve_list_repeat:
        if item not in cve_list:
            cve_list.append(item)

    shutil.rmtree(PATH)
    os.mkdir(PATH)
    return cve_list


def get_links_for_bulletine():
    links = []
    for page_number in range(2):
        r = requests.get(f"https://safe-surf.ru/specialists/bulletins-nkcki/?PAGEN_1={page_number+1}")
        soup = BeautifulSoup(r.text, "html.parser")
        for vuln in soup.find_all("h3"):
            vuln_name = re.findall(r"VULN-\d*.\d*", vuln.text)
            if vuln_name:
                full_name_vuln = vuln_name[0] + ".pdf"
                bulletin_pdf_url = "https://safe-surf.ru/upload/VULN/{}".format(full_name_vuln)
                links.append(bulletin_pdf_url)
    return links


def create_pdf_file(links):
    for item in links:
        get = requests.get(item)
        name = item.replace("https://safe-surf.ru/upload/VULN/", "")
        with open(f'{PATH}/{name}', 'wb') as f:
            f.write(get.content)
        f.close()


links = get_links_for_bulletine()
create_pdf_file(links)
cve_line = get_cve_list()  # Получение списка cve из бюллетеня НКЦКИ
print(cve_line)

