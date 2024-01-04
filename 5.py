import cv2
import numpy as np

def hist_match(source, template):
    # Calcule o histograma cumulativo da imagem de origem e do modelo
    src_cdf, bins = np.histogram(source.flatten(), 256, [0,256], density=True)
    src_cdf = src_cdf.cumsum() # histograma cumulativo
    tmpl_cdf, bins = np.histogram(template.flatten(), 256, [0,256], density=True)
    tmpl_cdf = tmpl_cdf.cumsum() # histograma cumulativo

    # Crie uma tabela de pesquisa para mapear os valores de pixel da imagem de origem para a imagem do modelo
    lut = np.zeros(256, dtype='uint8')
    j = 0
    for i in range(256):
        while tmpl_cdf[j] < src_cdf[i] and j < 255:
            j += 1
        lut[i] = j

    # Aplique a tabela de pesquisa à imagem de origem
    return lut[source]

# Carregue as imagens
source = cv2.imread('einstein.jpg', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('polen.png', cv2.IMREAD_GRAYSCALE)

# Aplique a correspondência de histograma
matched = hist_match(source, template)

# Salve a imagem resultante
cv2.imwrite('matched.png', matched)
