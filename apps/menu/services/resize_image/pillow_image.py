from PIL import Image


def resize_image(path):
    
    img = Image.open(path)

    img = img.resize((310, 260), Image.ANTIALIAS)
    try:
        img.save(path)
    except IOError:
        print("cannot create thumbnail for", path)
  
