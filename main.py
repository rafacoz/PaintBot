from PIL import Image
import random
import sys
import ResizeImage
import PixelAlphabet as pixalf
import DrawingFunctions as df
import AHKFunctions as ahkf
import constants as cons
import ResizeImage as ri

# Lambda functions
lower = lambda a: int((abs(a) + a) / 2)
upper = lambda a: 255 if (a > 255) else a

_R_ = 0  # Tuple R position
_G_ = 1  # Tuple G position
_B_ = 2  # Tuple B position

_X_ = 0  # X Axis code
_Y_ = 1  # X Axis code

_ZOOM_PERCENT_ = 1 # Not being used at the moment
_FONT_SIZE_ = 4 # Font size

# Colors RGB
_MAGENTA_ = (255, 0, 255)
_CYAN_ = (0, 255, 255)


# Log
_IS_DEBUG_ = False
_IS_INFO_ = True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_file_path = "imgs\img_not_found.png"
    color_palette_div = 64
    upper_text = "HELLO! I AM A PAINT BOT"
    lower_text = "I GOING TO PAINT FLOWERS.PNG"

    # Verifies input data
    if (len(sys.argv) >= 2):
        image_file_path = sys.argv[1]
    if (len(sys.argv) >= 3):
        color_palette_div = int(sys.argv[2])

    currentColor = []

    # Sets output_file path and resize images
    output_file_path = image_file_path + cons._FILE_APPEND_NAME_ + cons._FILE_APPEND_FORMAT_
    ri.resize_image(image_file_path, output_file_path)

    pb = df.PaintBot(output_file_path, color_palette_div, int(color_palette_div / 2))
    img_width = pb.imageW
    img_height = pb.imageH

    ahkf.printHeaderAHK(img_width, (img_height + cons._FRAME_H_2_))

    # Draw Frames
    ahkf.printUpperFrame(img_width, img_height)
    ahkf.printLowerFrame(img_width, img_height, 0, 0, 0)

    # Write text
    ahkf.changeToWriteMode(0, 255, 0)
    filtered_upper_text = pixalf.CropStringToFit(upper_text, img_width)
    filtered_lower_text = pixalf.CropStringToFit(lower_text, img_width)
    pixalf.writeLine(filtered_upper_text, len(filtered_upper_text))
    pixalf.writeLine(filtered_lower_text, len(filtered_lower_text), 0, (pb.imageH + cons._FRAME_H_))

    # Draw Image
    ahkf.changeToDrawingMode()
    pb.generateImageAHK()

    # Add footer and reset mouse position
    ahkf.resetMousePosition()
    ahkf.printFooterAHK()

