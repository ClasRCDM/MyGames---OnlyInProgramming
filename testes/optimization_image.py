from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), Image.ANTIALIAS)
save_path = asksaveasfilename()

img.save(save_path)
