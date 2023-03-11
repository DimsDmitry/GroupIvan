from PIL import Image
from PIL import ImageFilter

with Image.open('cyborg.png') as pic_original:
   pic_original.show()

   pic_gray = pic_original.convert('L')
   pic_gray.save('cyborg.jpg')
   pic_gray.show()

   pic_up = pic_gray.transpose(Image.ROTATE_180)
   pic_up.save('cyborg.jpg')
   pic_up.show()
