from PIL import Image, ImageDraw, ImageFont
class Operation_image:
  """
    Classe permettant de creer, d'une operation son objet image.
  """
  def __init__(self, width, height, operation, font_size):
    self.width = width
    self.height = height
    self.operation = operation
    self.font_size = font_size
    self.result = eval(self.operation)
    self.image = self.Image_constructor(self.font_size)
  def Image_constructor(self, size):
    font = ImageFont.truetype("arial.ttf", size=size)
    img = Image.new('RGB', (self.width, self.height), color='red')
    imgDraw = ImageDraw.Draw(img)
    textWidth, textHeight = imgDraw.textsize(self.operation, font=font)
    xText = (self.width - textWidth) / 2
    yText = (self.height - textHeight) / 2
    imgDraw.text((xText, yText), self.operation, font=font, fill=(255, 255, 0), align='justify')
    return img