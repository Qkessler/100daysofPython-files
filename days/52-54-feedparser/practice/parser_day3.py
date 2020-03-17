import feedparser
from collections import namedtuple
from datetime import datetime

Entrada = namedtuple('Entrada', 'title published creador')


def printear_entradas(entradas):
    for entrada in entradas:
        print(f'{entrada.published} - {entrada.title}:{entrada.creador}')


keys = ['id', 'guidislink', 'link', 'title', 'title_detail', 'published',
        'published_parsed', 'links', 'authors', 'author', 'author_detail',
        'dcterms_alternative', 'summary', 'summary_detail', 'tags',
        'media_keywords', 'media_content', 'media_thumbnail', 'href',
        'content']


def parsing_pais(fichero):
    feed = feedparser.parse(fichero)
    if 'title' in feed.entries[0]:
        entradas = []
        # print(feed.entries[1].author)
        for entry in feed.entries:
            dobj = datetime.strptime(entry.published, '%a, %d %b %Y %X %Z')
            entradas.append(Entrada(entry.title, dobj, entry.author))
        entradas.sort(key=lambda entrada: entrada.published)
        printear_entradas(entradas)


if __name__ == '__main__':
    parsing_pais('elpais.xml')
