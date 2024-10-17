

from skimage.transform import resiza

def resize_image(image, proportion):
    assert 0 <= proportion <= 1, "specify a valid proportion between 0 and 1."
    height = roud(image.shape[0] * proportion)
    width = roud(image.shape[1] * proportion)
    image_resized = resize(image, (height, width), anti_aliasing=true)
    return image_resized