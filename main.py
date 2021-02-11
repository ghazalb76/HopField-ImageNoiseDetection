from hopfield import hopfield
from PIL import Image, ImageFont
import numpy as np
import random


font = ImageFont.truetype("Tahoma.ttf", font_siza)
def make_perfect_data(font_size)
    for char in "ABCDEFGHIJ":
        im = Image.Image()._new(font.getmask(char))
        im.save("train/"+str(font_size)+"/"+char+".bmp")


def make_noisy_data(font_size, v):

    for char in "ABCDEFGHIJ":
        im = Image.Image()._new(font.getmask(char))
        data = np.array(im)
        for i in data:
            for j in range(len(i)):
                r = random.randint(1, 10)
                if r <= v:
                    i[j] = 0
                    rescaled = (255.0 / data.max() *
                                (data - data.min())).astype(np.uint8)
                    print(rescaled)
                    im = Image.fromarray(rescaled)
                    im.save("test/"+str(font_size)+"/"+char+".bmp")

''' uncomment any of them to make image or noisy image '''
# make_perfect_data(16)
# make_perfect_data(32)
# make_perfect_data(64)

# make_noisy_data(16, 1)
# make_noisy_data(32, 3)
# make_noisy_data(64, 6)



train_paths = []
path = "train/64/"
for i in "A":
    print(i)
    train_paths.append(path+i+".bmp")


test_paths = []
path = "test/64/"
for i in "A":
    print(i)
    test_paths.append(path+i+".bmp")


hopfield(train_files=train_paths, test_files=test_paths, theta=0.5,
         time=20000, size=(100, 100), threshold=60)


'''
10% for all of them 100
30% is different and between 10 to 50
60% for all of them 0