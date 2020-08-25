def separar_texto(pals):
    palabras = []
    for i in pals:
        pals.append(i)
    return palabras

texto = """Sherlock            Holmes            is            a            fictional            private            detective            created            by            British            author            Sir            Arthur            Conan            Doyle.            Referring            to            himself            as            a            consulting            detective            in            the            stories,            Holmes            is            known            for            his            proficiency            with            observation,            deduction,                       forensic            science,            and            logical            reasoning            that            borders            on            the            fantastic,            which            he                      employs            when            investigating            cases            for            a            wide            variety            of            clients,            including         Scotland            Yard."""
x = (texto.split())
from collections import Counter
freq_pals = dict(Counter(x))
print(freq_pals)

import matplotlib.pyplot as plt
import collections
from wordcloud import WordCloud
wordcloud = WordCloud(width=480, height=480, margin=0)
wordcloud.generate_from_frequencies(freq_pals)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
# plt.show()

def generar_dict_filt(palabras_separadas, palabras_filtro,n):
    if n < 0:
        return palabras_separadas
    else:
        for censurada in palabras_filtro:
            print(censurada)
            r = [palabras_separadas.pop(key) for key in palabras_filtro]
            print(r)
        palabras_3 = {k: v for k, v in sorted(palabras_2.items(), key=lambda item: item[1])}
        print(palabras_3)
        palabras_4 = collections.Counter(palabras_3).most_common(n)
        return palabras_4
censuradas = ('is', 'in')
w = generar_dict_filt(palabras_separadas=x, palabras_filtro=censuradas,n=2)
print(w)