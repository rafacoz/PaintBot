_ZOOM_PERCENT_ = 1 # 1 means 100% zoom
_FONT_SIZE_ = 3 # Font size - set to 0 zero you want to not use. Default should be 3 or 4
_FONT_MULTIPLIER_ = 7

_SPACE_X_ = _FONT_SIZE_/2
_SPACE_Y_ = _FONT_SIZE_/2

_CHAR_LIMIT_ = 25 * _ZOOM_PERCENT_
_LINE_LIMIT_ = 10 * _ZOOM_PERCENT_


_FRAME_H_ = (_FONT_SIZE_ * 9)
_FRAME_H_2_ = (_FONT_SIZE_ * 9) * 2
#  _FRAME_W_ = _CANVAS_W_  # Not yet defined nor used

_UPPER_FRAME_DRAG_X_ = 13
_UPPER_FRAME_DRAG_Y_ = 151

_LOWER_FRAME_DRAG_X_ = 13
_LOWER_FRAME_DRAG_Y_ = 151

_DRAW_DRAG_X_ = 13  # This is the distance between the leftmost part of the screen and the canvas
_DRAW_DRAG_Y_ = 151 + _FRAME_H_  # This is the distance between the upper part of the screen and the canvas +upper frame

_WRITE_DRAG_X_ = 13   # This is the distance between the leftmost part of the screen and the canvas
_WRITE_DRAG_Y_ = 151  # This is the distance between the upper part of the screen and the canvas

_FILE_APPEND_NAME_ = "_resized"
_FILE_APPEND_FORMAT_ = ".png"


# Lambda functions
lower = lambda a: int((abs(a) + a) / 2)
upper = lambda a: 255 if (a > 255) else a

_R_ = 0  # Tuple R position
_G_ = 1  # Tuple G position
_B_ = 2  # Tuple B position

_X_ = 0  # X Axis code
_Y_ = 1  # X Axis code

# Colors RGB
_MAGENTA_ = (255, 0, 255)
_CYAN_ = (0, 255, 255)
# Log
_IS_DEBUG_ = False
_IS_INFO_ = True