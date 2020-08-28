import re
import requests
import html2text
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

## Word cloud

texto_sherlock = "Sherlock            Holmes            is            a            fictional            private            detective            created            by            British            author            Sir            Arthur            Conan            Doyle.            Referring            to            himself            as            a            consulting            detective            in            the            stories,            Holmes            is            known            for            his            proficiency            with            observation,            deduction,                       forensic            science,            and            logical            reasoning            that            borders            on            the            fantastic,            which            he                      employs            when            investigating            cases            for            a            wide            variety            of            clients,            including         Scotland            Yard."


def limpio_texto(texto):
    rx = re.compile('\W+')
    res = rx.sub(' ', texto).strip().lower()
    return res


def elimino_key_values(dict, censuradas):
    new_dict = {i:dict[i] for i in dict if i not in censuradas}
    return new_dict


def generar_dict_filt(palabras_separadas, palabras_filtro,n,r):
    # Creamos un dict con la frecuencia de cada palabra
    frec_pals = dict(Counter(palabras_separadas))
    if n <= 0:
        return frec_pals
    else:
        # lo censuramos
        dict_1 = elimino_key_values(frec_pals, palabras_filtro)

        # lo ordenamos
        dict_2 = {k: v for k, v in sorted(dict_1.items(), key=lambda item: item[1])}
        print(dict_2)

        # eligimos las que tengan una frec >= r
        if r > 0:
            dict_2 = {key: val for key, val in dict_2.items() if val >= r}

        # elegimos el top
        dict_3 =  dict(sorted(dict_2.items(), key=lambda xx: xx[1], reverse=True)[:n])
        return dict_3


sherlock_limpio = limpio_texto(texto_sherlock)
x = (sherlock_limpio.split())
censuradas = ('is', 'in', 'a', 'the')
w = generar_dict_filt(palabras_separadas=x, palabras_filtro=censuradas,
                      n=5, r=0)
# print(w)

# wordcloud = WordCloud(width=480, height=480, margin=0)
# wordcloud.generate_from_frequencies(w)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.margins(x=0, y=0)
# plt.show()

# 9
# vamos a hacer lo mismo con 4 obras literarias

from bs4 import BeautifulSoup
from urllib.request import urlopen

def titulo_limpio(link):
    # buscamos el titulo
    r = urlopen(link)
    soup = BeautifulSoup(r, "html.parser")
    title = soup.title.string

    # limpiamos limpiamos
    rx = re.compile('\W+')
    res = rx.sub(' ', title).strip()
    titulo = "_".join(res.split())
    return titulo


def limpio_html(link):
    # obtenemos el titulo
    titulo = titulo_limpio(link)

    # nos bajamos el archivo y lo guardamos con el titulo
    r = requests.get(link)
    with open('./archivos/{}.htm'.format(titulo), 'wb') as f_html:
        f_html.write(r.content)

    # lo leemos
    with open('./archivos/{}.htm'.format(titulo), 'r') as f_h:
        f_down = f_h.read()

    # eliminamos los tags html
    h = html2text.HTML2Text()
    h.ignore_links = True
    semi_limpio = (h.handle(f_down))

    # hacemos regex para quedarnos solo con las letras
    # dependiendo el caso deberiamos tener numeros tmb
    # entre otros caracteres
    semi_limpio2 = limpio_texto(semi_limpio)

    return semi_limpio2

def limpito_separo_palabras(link,):
    limpiado = limpio_html(link, )
    apalabrado = (limpiado.split())
    return apalabrado

# Funcion que nos muestra el cloud de un link
# nombre_elegido: nombre elegido para el archivo
# palabras_filtro: palabras que no nos interesa trackear
# n : num max de palabras
# r : umbral minimo de repeticiones para tomar palabra
def muestro_wordcloud_link(link,
                           palabras_filtro,
                           n, r):
    titulo = titulo_limpio(link)
    en_palabras = limpito_separo_palabras(link)
    final = generar_dict_filt(en_palabras,palabras_filtro, n, r)
    wordcloud = WordCloud(width=480, height=480, margin=0)
    wordcloud.generate_from_frequencies(final)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.savefig('./img/{}.png'.format(titulo))
    # return plt.show()

link_estudio_escarlata ='https://www.gutenberg.org/files/244/244-h/244-h.htm'
link_agatha = 'http://www.gutenberg.org/files/58866/58866-h/58866-h.htm'
link_chesterton = 'http://www.gutenberg.org/files/1695/1695-h/1695-h.htm'
link_sayers = 'http://www.gutenberg.org/files/58820/58820-h/58820-h.htm'
censored = ('gutenberg', 'Gutenberg-tm', 'the', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once')

# estudio_escarlata = muestro_wordcloud_link(link=link_estudio_escarlata,
#                              palabras_filtro=censored,
#                              n=5, r=0)

# print(estudio_escarlata)


# Lo hacemos para una lista de links
def word_clouds(lista_links, palabras_filtro,n, r):
    for i in lista_links:
        print(muestro_wordcloud_link(i, palabras_filtro, n, r))

links = []
links.extend((link_agatha, link_sayers, link_chesterton, link_estudio_escarlata))

# print(word_clouds(lista_links=links, palabras_filtro=censored,n=50, r=20))


# 10

link_articulos = []
link1 = 'https://doi.org/10.1371/journal.pone.0005738'
link2 = 'https://doi.org/10.1109/LRA.2020.2966414'
link3 = 'https://doi.org/10.1371/journal.pone.0108895'
link_articulos.extend((link1,link2,link3))

print(word_clouds(lista_links=link_articulos, palabras_filtro=censored,n=20, r=0))