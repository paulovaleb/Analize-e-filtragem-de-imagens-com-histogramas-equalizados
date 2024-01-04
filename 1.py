import numpy as np
from PIL import Image

def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32")
    return data

def save_image(npdata, outfilename):
    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"), "L")
    img.save(outfilename)

def detect_edges(image, adjacency):
    edges = np.zeros_like(image)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            if adjacency == '8':
                neighborhood = image[i-1:i+2, j-1:j+2]
            elif adjacency == 'm':
                neighborhood = image[i-1:i+2, j-1:j+2]
                neighborhood = np.delete(neighborhood, [0, 2, 6, 8])
            if np.max(neighborhood) != image[i,j] or np.min(neighborhood) != image[i,j]:
                edges[i,j] = 255
    return edges

image = load_image("aviao.png")
edges_8 = detect_edges(image, '8')
edges_m = detect_edges(image, 'm')

save_image(edges_8, "edges_8.png")
save_image(edges_m, "edges_m.png")

print("Imagens salvas como 'edges_8.png' e 'edges_m.png'")
