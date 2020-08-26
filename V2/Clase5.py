import re
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

###### MT #####



