from PIL import Image


def resize_image(path):
    # A chances de não funcionar, caso aconteça isso
    # não faça nada
    try:
        img = Image.open(path)
        img = img.resize((310, 260), Image.ANTIALIAS)
    except Exception as e:
        print("Erro no pillow: {e}")
    # erro de diretorio de midia
    try:
        img.save(path)
    except IOError:
        print("cannot create thumbnail for", path)
  
