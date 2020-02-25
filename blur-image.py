from PIL import Image, ImageFilter

howto = Image.open("big-sale.png")
blur_howto = howto.filter(ImageFilter.GaussianBlur)
blur_howto.save("how-to-blur.png")
blur_howto.show()