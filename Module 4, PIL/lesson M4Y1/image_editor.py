from PIL import Image
class ImageEditor():
   def __init__(self, filename):
       self.filename = filename
       self.original = None
       self.changed = list()

   def open(self):
       try:
           self.original = Image.open(self.filename)
       except:
           print('Файл не найден!')
       self.original.show()

MyImage = ImageEditor('rocket.png')
MyImage.open()
