from PIL import Image


class ImageEditor:
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []


    def open(self):
        try:
            self.oraginal = Image.open(self.filename)
            self.original.show()
        except:
            print('Файл не знайдено')


    def do_left(self):
        rotate = self.original.transpone(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotate)


        temp_filename = self.filename.split('.')
        new_filename = temp_filenname

