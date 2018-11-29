import os
import PIL
from PIL import Image

f_names = os.listdir("PPC")
files = [os.path.join("PPC",f) for f in os.listdir("PPC") if os.path.isfile(os.path.join("PPC", f))]
HSIZE = 32
WSIZE = 32

for idx, f in enumerate(files):
    print(os.path.join("PPC2",f_names[idx]))
    img = Image.open(f)
    img = img.resize((WSIZE, HSIZE))
    img.save(os.path.join("PPC2",f_names[idx]))
