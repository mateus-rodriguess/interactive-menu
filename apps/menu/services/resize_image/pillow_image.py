from PIL import Image


def resize_image(path):

    try:
        img = Image.open(path)
        img = img.resize((330, 280), Image.ANTIALIAS)
        img.save(path)
    except Exception as e:
        print(f"Erro no pillow: {e}")
  
