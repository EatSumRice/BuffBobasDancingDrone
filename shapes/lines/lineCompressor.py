from PIL import Image

for i in range(100):
    img = Image.open('line{0}.jpg'.format(i))
    new_size_ratio = .28
    img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.ANTIALIAS)
    img.save('compline{0}.jpg'.format(i))