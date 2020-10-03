from bs4 import BeautifulSoup
import requests
import csv


def read():
    with open(file='content.html', encoding='utf-8', mode='r') as file:
        return file.read()


def down(url):
    res = requests.get(url=url).content
    file_name = url.split('/')[-1]
    with open(file=file_name, mode='wb') as file:
        file.write(res)


def write_csv(lines):
    with open(file='Hyundai_Sonata_Gallery.csv', encoding='utf-8', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(lines)


def main():
    content = read()
    soup = BeautifulSoup(content, 'html5lib')
    cards = soup.select('.media-preview__image__wrapper')
    for card in cards:
        image = card.img['src']
        # title = card.find(attrs={'class': 'media-preview__title'}).text.strip()
        # year = title.split(' ')[0]
        # model = title.split(' ')[1]
        line = ['2016', 'Hyundai', 'Sonata', 'Front', image]
        print(line)
        write_csv([line])


if __name__ == '__main__':
    main()
