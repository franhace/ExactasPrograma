import docx
from V2.Clase5 import *

def readDocx(doc):
    try:
        doc = docx.Document('{}'.format(doc))  # Creating word reader object.
        data = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            data = '\n'.join(fullText)

        return(data)

    except IOError:
        print('There was an error opening the file!')
        return

archivo = '/media/nn/1CC6A8D9C6A8B484/NN/Python/ExactasPrograma/V2/Plenario 12 de agosto sensaciones.docx'
texto_mt = readDocx(archivo)

mt_limpio = limpio_texto(texto_mt)
mt_separadas = (mt_limpio.split())

censuradas_mt = ('que', 'y', 'a', 'en', 'el', 'con',
                 'me', 'de', 'pero', 'las', 'la', 'un',
                 'una', 'muy', 'lo', 'no', 'es', 'por',
                 'desde', 'ya', 'trajo', 'del', 'al',
                 'los', 'como',"estos","estaba","incluso")
z = generar_dict_filt(palabras_separadas=mt_separadas,
                      palabras_filtro=censuradas_mt,
                      n=80, r=0)
print(z)

wordcloud = WordCloud(width=480, height=480, margin=0)
wordcloud.generate_from_frequencies(z)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()