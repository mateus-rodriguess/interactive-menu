from PIL import Image


def resize_image(path):
    # A chances de não funcionar, caso aconteça isso não faça nada
    try:
        img = Image.open(path)
        img = img.resize((330, 280), Image.ANTIALIAS)
        img.save(path)
    except Exception as e:
        print("Erro no pillow: {e}")
  
