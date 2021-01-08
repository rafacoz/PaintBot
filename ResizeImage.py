from PIL import Image

_MAX_WIDTH_ = 1080
_MAX_HEIGHT_ = 800

# VERIFICAR SE EH MTO GRANDE -> RESIZE PRA CABER

def resize_image(image_path, output_file="default.png"):
    img = Image.open(image_path) # image extension *.png,*.jpg
    width, height = img.size
    ratio = calculateRatio(width, height)

    new_width = int(width * ratio)
    new_height = int(height * ratio)
    if new_width < 1:
        new_width = 1
    if new_height < 1:
        new_height = 1

    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    file_name = output_file
    img.save(file_name) # format may what you want *.png, *jpg, *.gif

def calculateRatio(width, height):
    if width <= _MAX_WIDTH_ and height <= _MAX_HEIGHT_:
        return 1
    if width > height:
        return _MAX_WIDTH_ / width
    return _MAX_HEIGHT_ / height
