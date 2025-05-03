from rembg import remove
from PIL import Image
from io import BytesIO
import requests
import os

url = "Link address of any 2d or vector image in jpg format"
image_name = url.split("/")[-1]

# img = Image.open(r"path of the image if it already in the original")
# image_name = url.split("/")[-1]  // comment out the next two line of code if image url is not required
img = Image.open(BytesIO(requests.get(url).content))
img.save("original/"+image_name, format='jpeg')

out_path = 'masked/'+image_name

with open(out_path, 'wb') as f:
    inp = open('original/'+image_name, 'rb').read()
    sub = remove(inp)
    f.write(sub)