import re
from collections import Counter

import html2text
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

        # eligimos las que tengan una frec >= r
        if r > 0:
            dict_2 = {key: val for key, val in dict_2.items() if val >= r}

        # elegimos el top
        dict_3 =  dict(sorted(dict_2.items(), key=lambda xx: xx[1], reverse=True)[:n])
        return dict_3


sherlock_limpio = limpio_texto(texto_sherlock)
x = (sherlock_limpio.split())
censuradas = ('is', 'in', 'a', 'the')
w = generar_dict_filt(palabras_separadas=x, palabras_filtro=censuradas,n=5,r=0)
# print(w)

# wordcloud = WordCloud(width=480, height=480, margin=0)
# wordcloud.generate_from_frequencies(w)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.margins(x=0, y=0)
# plt.show()

# 9
# vamos a hacer lo mismo con 4 obras literarias
import requests


def limpio_html(link,nombre_elegido):
    # nos bajamos el archivo
    r = requests.get(link)
    with open('{}.htm'.format(nombre_elegido), 'wb') as f_html:
        f_html.write(r.content)

    # lo leemos
    with open('{}.htm'.format(nombre_elegido), 'r') as f_h:
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

def limpito_separo_palabras(link,nombre_elegido):
    limpiado = limpio_html(link, nombre_elegido)
    apalabrado = (limpiado.split())
    return apalabrado

# nos muestra el cloud de un link
# nombre_elegido: nombre elegido para el archivo
# palabras_filtro: palabras que no nos interesa trackear
# n : num max de palabras
# r : umbral minimo de repeticiones para tomar palabra
def muestro_wordcloud_link(link,nombre_elegido,
                           palabras_filtro,
                           n, r):
    en_palabras = limpito_separo_palabras(link,nombre_elegido)
    final = generar_dict_filt(en_palabras,palabras_filtro, n, r)
    wordcloud = WordCloud(width=480, height=480, margin=0)
    wordcloud.generate_from_frequencies(final)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    return plt.show()

link_estudio_escarlata ='https://www.gutenberg.org/files/244/244-h/244-h.htm'
censored = ('gutenberg', 'Gutenberg-tm', 'the', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once')

asd = muestro_wordcloud_link(link=link_estudio_escarlata,
                             nombre_elegido='ElSherlo',
                             palabras_filtro=censored,
                             n=5, r=0)
print(asd)