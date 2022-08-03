from PIL import Image

for i in range(3):
    img = Image.open('line{0}.jpg'.format(i))
    new_size_ratio = .14
    img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.Resampling.LANCZOS)
    img.save('compline{0}.jpg'.format(i))