import constants as cons


def spaceUnit():
    print("// Drawing spaceUnit")
    print("FileAppend, spaceUnit, log.txt")
    print("_SPACE_ += _SPACE_APPEND_ / _ZOOM_PERCENT_")

def lineUnit():
    print("// Drawing lineUnit")
    print("FileAppend, lineUnit, log.txt")
    print("_SPACE_ = 0")
    print("_LINE_ += _LINE_APPEND_ / _ZOOM_PERCENT_")

def endOfPage():
    print("// Drawing endOfPage")
    print("FileAppend, endOfPage, log.txt")
    print("EraseAll(5000)")
    print("_SPACE_ = 0")
    print("_LINE_ = 0")

def resetSpace():
    print("FileAppend, resetSpace, log.txt")
    print("_SPACE_ = 0")

def drawUpperA(free_drag_x=0, free_drag_y=0):
    print("// Drawing A")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperA, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperB(free_drag_x=0, free_drag_y=0):
    print("// Drawing B")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperB, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperC(free_drag_x=0, free_drag_y=0):
    print("// Drawing C")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperC, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawUpperD(free_drag_x=0, free_drag_y=0):
    print("// Drawing D")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperD, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperE(free_drag_x=0, free_drag_y=0):
    print("// Drawing E")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperE, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperF(free_drag_x=0, free_drag_y=0):
    print("// Drawing F")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperF, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperG(free_drag_x=0, free_drag_y=0):
    print("// Drawing G")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperG, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawUpperH(free_drag_x=0, free_drag_y=0):
    print("// Drawing H")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperH, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperI(free_drag_x=0, free_drag_y=0):
    print("// Drawing I")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperI, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperJ(free_drag_x=0, free_drag_y=0):
    print("// Drawing J")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperJ, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperK(free_drag_x=0, free_drag_y=0):
    print("// Drawing K")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperK, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawUpperL(free_drag_x=0, free_drag_y=0):
    print("// Drawing L")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperL, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperM(free_drag_x=0, free_drag_y=0):
    print("// Drawing M")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperM, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawUpperN(free_drag_x=0, free_drag_y=0):
    print("// Drawing N")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperN, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawUpperO(free_drag_x=0, free_drag_y=0):
    print("// Drawing O")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperO, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperP(free_drag_x=0, free_drag_y=0):
    print("// Drawing P")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperP, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperQ(free_drag_x=0, free_drag_y=0):
    print("// Drawing Q")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperQ, log.txt")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawUpperR(free_drag_x=0, free_drag_y=0):
    print("// Drawing R")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperR, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperS(free_drag_x=0, free_drag_y=0):
    print("// Drawing S")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperS, log.txt")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawUpperT(free_drag_x=0, free_drag_y=0):
    print("// Drawing T")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperT, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperU(free_drag_x=0, free_drag_y=0):
    print("// Drawing U")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperU, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperV(free_drag_x=0, free_drag_y=0):
    print("// Drawing V")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperV, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperW(free_drag_x=0, free_drag_y=0):
    print("// Drawing W")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperW, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperX(free_drag_x=0, free_drag_y=0):
    print("// Drawing X")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperX, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawUpperY(free_drag_x=0, free_drag_y=0):
    print("// Drawing Y")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperY, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUpperZ(free_drag_x=0, free_drag_y=0):
    print("// Drawing Z")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUpperZ, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerA(free_drag_x=0, free_drag_y=0):
    print("// Drawing a")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerA, log.txt")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerB(free_drag_x=0, free_drag_y=0):
    print("// Drawing b")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerB, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerC(free_drag_x=0, free_drag_y=0):
    print("// Drawing c")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerC, log.txt")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerD(free_drag_x=0, free_drag_y=0):
    print("// Drawing d")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerD, log.txt")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerE(free_drag_x=0, free_drag_y=0):
    print("// Drawing e")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerE, log.txt")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerF(free_drag_x=0, free_drag_y=0):
    print("// Drawing f")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerF, log.txt")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerG(free_drag_x=0, free_drag_y=0):
    print("// Drawing g")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerG, log.txt")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerH(free_drag_x=0, free_drag_y=0):
    print("// Drawing h")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerH, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerI(free_drag_x=0, free_drag_y=0):
    print("// Drawing i")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerI, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerJ(free_drag_x=0, free_drag_y=0):
    print("// Drawing j")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerJ, log.txt")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerK(free_drag_x=0, free_drag_y=0):
    print("// Drawing k")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerK, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerL(free_drag_x=0, free_drag_y=0):
    print("// Drawing l")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerL, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerM(free_drag_x=0, free_drag_y=0):
    print("// Drawing m")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerM, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35  * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerN(free_drag_x=0, free_drag_y=0):
    print("// Drawing n")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerN, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerO(free_drag_x=0, free_drag_y=0):
    print("// Drawing o")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerO, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerP(free_drag_x=0, free_drag_y=0):
    print("// Drawing p")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerP, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerQ(free_drag_x=0, free_drag_y=0):
    print("// Drawing q")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerQ, log.txt")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerR(free_drag_x=0, free_drag_y=0):
    print("// Drawing r")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerR, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerS(free_drag_x=0, free_drag_y=0):
    print("// Drawing s")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerT, log.txt")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerT(free_drag_x=0, free_drag_y=0):
    print("// Drawing t")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerT, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerU(free_drag_x=0, free_drag_y=0):
    print("// Drawing u")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerU, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerV(free_drag_x=0, free_drag_y=0):
    print("// Drawing v")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerV, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerW(free_drag_x=0, free_drag_y=0):
    print("// Drawing w")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerW, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerX(free_drag_x=0, free_drag_y=0):
    print("// Drawing x")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerX, log.txt")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLowerY(free_drag_x=0, free_drag_y=0):
    print("// Drawing y")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerY, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLowerZ(free_drag_x=0, free_drag_y=0):
    print("// Drawing z")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLowerZ, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawDot(free_drag_x=0, free_drag_y=0):
    print("// Drawing Dot")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawDot, log.txt")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawQuestion(free_drag_x=0, free_drag_y=0):
    print("// Drawing Question")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawExclamation, log.txt")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawExclamation(free_drag_x=0, free_drag_y=0):
    print("// Drawing Exclamation")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawExclamation, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawSlash(free_drag_x=0, free_drag_y=0):
    print("// Drawing Slash")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawSlash, log.txt")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawMinus(free_drag_x=0, free_drag_y=0):
    print("// Drawing Minus")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawMinus, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawApostrophe(free_drag_x=0, free_drag_y=0):
    print("// Drawing Apostrophe")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawApostrophe, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawComma(free_drag_x=0, free_drag_y=0):
    print("// Drawing Comma")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawComma, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawNum1(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum1")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum1, log.txt")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawNum2(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum2")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum2, log.txt")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawNum3(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum3")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum3, log.txt")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawNum4(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum4")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum4, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawNum5(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum5")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum5, log.txt")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawNum6(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum6")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum6, log.txt")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawNum7(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum7")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum7, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawNum8(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum8")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum8, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawNum9(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum9")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum9, log.txt")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawNum0(free_drag_x=0, free_drag_y=0):
    print("// Drawing drawNum0")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawNum0, log.txt")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")


def drawAt(free_drag_x=0, free_drag_y=0):
    print("// Drawing @")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawAt, log.txt")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawHashtag(free_drag_x=0, free_drag_y=0):
    print("// Drawing #")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawHashtag, log.txt")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawDollar(free_drag_x=0, free_drag_y=0):
    print("// Drawing $")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawDollar, log.txt")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawPercent(free_drag_x=0, free_drag_y=0):
    print("// Drawing percent")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawPercent, log.txt")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawHat(free_drag_x=0, free_drag_y=0):
    print("// Drawing ^")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawHat, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawAmpersand(free_drag_x=0, free_drag_y=0):
    print("// Drawing &")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawAmpersand, log.txt")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawAsterisk(free_drag_x=0, free_drag_y=0):
    print("// Drawing *")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawAsterisk, log.txt")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLeftParenthesis(free_drag_x=0, free_drag_y=0):
    print("// Drawing (")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLeftParenthesis, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawRightParenthesis(free_drag_x=0, free_drag_y=0):
    print("// Drawing )")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawRightParenthesis, log.txt")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawUnderscore(free_drag_x=0, free_drag_y=0):
    print("// Drawing _")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawUnderscore, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLesserThan(free_drag_x=0, free_drag_y=0):
    print("// Drawing <")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLesserThan, log.txt")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawGreaterThan(free_drag_x=0, free_drag_y=0):
    print("// Drawing >")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawGreaterThan, log.txt")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawPlus(free_drag_x=0, free_drag_y=0):
    print("// Drawing +")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawPlus, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawEqual(free_drag_x=0, free_drag_y=0):
    print("// Drawing =")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawEqual, log.txt")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")

def drawLeftCurlyBracket(free_drag_x=0, free_drag_y=0):
    print("// Drawing {")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, CASCA, log.txt")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawRightCurlyBracket(free_drag_x=0, free_drag_y=0):
    print("// Drawing }")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawRightCurlyBracket, log.txt")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (65 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (35 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawLeftSquareBracket(free_drag_x=0, free_drag_y=0):
    print("// Drawing [")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawLeftSquareBracket, log.txt")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (25 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")

def drawRightSquareBracket(free_drag_x=0, free_drag_y=0):
    print("// Drawing ]")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, drawRightSquareBracket, log.txt")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")
    print("MouseClickDrag, L, (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (15 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (55 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (45 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (75 * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")


def CASCA(free_drag_x=0, free_drag_y=0):
    print("// Drawing XXXXX")
    print("ToolTip, %_SPACE_% %_LINE_%, 0, 30")
    print("FileAppend, CASCA, log.txt")
    print("MouseClickDrag, L, (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseClickDrag, L, (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+"), (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("MouseMove, (XX * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_X + _SPACE_ + "+str(free_drag_x)+"), (YY * _FONT_FACTOR_/_ZOOM_PERCENT_ + WRITE_DRAG_Y + _LINE_ + "+str(free_drag_y)+")")
    print("Click")


def select_char(input_char, free_drag_x=0, free_drag_y=0):
    # UPPER CASE
    if (input_char == "A"):
        drawUpperA(free_drag_x, free_drag_y)
    elif (input_char == "B"):
        drawUpperB(free_drag_x, free_drag_y)
    elif (input_char == "C"):
        drawUpperC(free_drag_x, free_drag_y)
    elif (input_char == "D"):
        drawUpperD(free_drag_x, free_drag_y)
    elif (input_char == "E"):
        drawUpperE(free_drag_x, free_drag_y)
    elif (input_char == "F"):
        drawUpperF(free_drag_x, free_drag_y)
    elif (input_char == "G"):
        drawUpperG(free_drag_x, free_drag_y)
    elif (input_char == "H"):
        drawUpperH(free_drag_x, free_drag_y)
    elif (input_char == "I"):
        drawUpperI(free_drag_x, free_drag_y)
    elif (input_char == "J"):
        drawUpperJ(free_drag_x, free_drag_y)
    elif (input_char == "K"):
        drawUpperK(free_drag_x, free_drag_y)
    elif (input_char == "L"):
        drawUpperL(free_drag_x, free_drag_y)
    elif (input_char == "M"):
        drawUpperM(free_drag_x, free_drag_y)
    elif (input_char == "N"):
        drawUpperN(free_drag_x, free_drag_y)
    elif (input_char == "O"):
        drawUpperO(free_drag_x, free_drag_y)
    elif (input_char == "P"):
        drawUpperP(free_drag_x, free_drag_y)
    elif (input_char == "Q"):
        drawUpperQ(free_drag_x, free_drag_y)
    elif (input_char == "R"):
        drawUpperR(free_drag_x, free_drag_y)
    elif (input_char == "S"):
        drawUpperS(free_drag_x, free_drag_y)
    elif (input_char == "T"):
        drawUpperT(free_drag_x, free_drag_y)
    elif (input_char == "U"):
        drawUpperU(free_drag_x, free_drag_y)
    elif (input_char == "V"):
        drawUpperV(free_drag_x, free_drag_y)
    elif (input_char == "W"):
        drawUpperW(free_drag_x, free_drag_y)
    elif (input_char == "X"):
        drawUpperX(free_drag_x, free_drag_y)
    elif (input_char == "Y"):
        drawUpperY(free_drag_x, free_drag_y)
    elif (input_char == "Z"):
        drawUpperZ(free_drag_x, free_drag_y)
    #LOWER CASE
    elif (input_char == "a"):
        drawLowerA(free_drag_x, free_drag_y)
    elif (input_char == "b"):
        drawLowerB(free_drag_x, free_drag_y)
    elif (input_char == "c"):
        drawLowerC(free_drag_x, free_drag_y)
    elif (input_char == "d"):
        drawLowerD(free_drag_x, free_drag_y)
    elif (input_char == "e"):
        drawLowerE(free_drag_x, free_drag_y)
    elif (input_char == "f"):
        drawLowerF(free_drag_x, free_drag_y)
    elif (input_char == "g"):
        drawLowerG(free_drag_x, free_drag_y)
    elif (input_char == "h"):
        drawLowerH(free_drag_x, free_drag_y)
    elif (input_char == "i"):
        drawLowerI(free_drag_x, free_drag_y)
    elif (input_char == "j"):
        drawLowerJ(free_drag_x, free_drag_y)
    elif (input_char == "k"):
        drawLowerK(free_drag_x, free_drag_y)
    elif (input_char == "l"):
        drawLowerL(free_drag_x, free_drag_y)
    elif (input_char == "m"):
        drawLowerM(free_drag_x, free_drag_y)
    elif (input_char == "n"):
        drawLowerN(free_drag_x, free_drag_y)
    elif (input_char == "o"):
        drawLowerO(free_drag_x, free_drag_y)
    elif (input_char == "p"):
        drawLowerP(free_drag_x, free_drag_y)
    elif (input_char == "q"):
        drawLowerQ(free_drag_x, free_drag_y)
    elif (input_char == "r"):
        drawLowerR(free_drag_x, free_drag_y)
    elif (input_char == "s"):
        drawLowerS(free_drag_x, free_drag_y)
    elif (input_char == "t"):
        drawLowerT(free_drag_x, free_drag_y)
    elif (input_char == "u"):
        drawLowerU(free_drag_x, free_drag_y)
    elif (input_char == "v"):
        drawLowerV(free_drag_x, free_drag_y)
    elif (input_char == "w"):
        drawLowerW(free_drag_x, free_drag_y)
    elif (input_char == "x"):
        drawLowerX(free_drag_x, free_drag_y)
    elif (input_char == "y"):
        drawLowerY(free_drag_x, free_drag_y)
    elif (input_char == "z"):
        drawLowerZ(free_drag_x, free_drag_y)
    # SPECIAL CHARACTERS
    elif (input_char == " "):
        spaceUnit()
    elif (input_char == "."):
        drawDot(free_drag_x, free_drag_y)
    elif (input_char == "?"):
        drawQuestion(free_drag_x, free_drag_y)
    elif (input_char == "!"):
        drawExclamation(free_drag_x, free_drag_y)
    elif (input_char == "-"):
        drawSlash(free_drag_x, free_drag_y)
    elif(input_char == "'"):
        drawApostrophe(free_drag_x, free_drag_y)
    elif(input_char == ","):
        drawComma(free_drag_x, free_drag_y)
    elif(input_char == "#"):
        drawHashtag(free_drag_x, free_drag_y)
    elif (input_char == "@"):
        drawAt(free_drag_x, free_drag_y)
    elif (input_char == "$"):
        drawDollar(free_drag_x, free_drag_y)
    elif (input_char == "%"):
        drawPercent(free_drag_x, free_drag_y)
    elif (input_char == "^"):
        drawHat(free_drag_x, free_drag_y)
    elif (input_char == "&"):
        drawAmpersand(free_drag_x, free_drag_y)
    elif (input_char == "*"):
        drawAsterisk(free_drag_x, free_drag_y)
    elif (input_char == "("):
        drawLeftParenthesis(free_drag_x, free_drag_y)
    elif (input_char == ")"):
        drawRightParenthesis(free_drag_x, free_drag_y)
    elif (input_char == "_"):
        drawUnderscore(free_drag_x, free_drag_y)
    elif (input_char == "<"):
        drawLesserThan(free_drag_x, free_drag_y)
    elif (input_char == ">"):
        drawGreaterThan(free_drag_x, free_drag_y)
    elif (input_char == "+"):
        drawPlus(free_drag_x, free_drag_y)
    elif (input_char == "="):
        drawEqual(free_drag_x, free_drag_y)
    elif (input_char == "{"):
        drawLeftCurlyBracket(free_drag_x, free_drag_y)
    elif (input_char == "}"):
        drawRightCurlyBracket(free_drag_x, free_drag_y)
    elif (input_char == "["):
        drawLeftSquareBracket(free_drag_x, free_drag_y)
    elif (input_char == "]"):
        drawRightSquareBracket(free_drag_x, free_drag_y)
    # Numbers
    elif (input_char == "0"):
        drawNum0(free_drag_x, free_drag_y)
    elif (input_char == "1"):
        drawNum1(free_drag_x, free_drag_y)
    elif (input_char == "2"):
        drawNum2(free_drag_x, free_drag_y)
    elif (input_char == "3"):
        drawNum3(free_drag_x, free_drag_y)
    elif (input_char == "4"):
        drawNum4(free_drag_x, free_drag_y)
    elif (input_char == "5"):
        drawNum5(free_drag_x, free_drag_y)
    elif (input_char == "6"):
        drawNum6(free_drag_x, free_drag_y)
    elif (input_char == "7"):
        drawNum7(free_drag_x, free_drag_y)
    elif (input_char == "8"):
        drawNum8(free_drag_x, free_drag_y)
    elif (input_char == "9"):
        drawNum9(free_drag_x, free_drag_y)
    else:
        print("ERROR " + input_char)


def main_text_printer(text, free_drag_x=0, free_drag_y=0):
    my_text = str(text)

    for idx in range(len(my_text)):
        select_char(my_text[idx], free_drag_x, free_drag_y)
        if ((idx + 1) % cons._CHAR_LIMIT_ == 0):
            lineUnit()
            #print("ChangeColor(" + str(random.randint(0, 255)) + ", " + str(random.randint(0, 255)) + ", " + str(random.randint(0, 255)) + ")")
        else:
            spaceUnit()

        if (((idx + 1) % (cons._CHAR_LIMIT_ * cons._LINE_LIMIT_)) == 0):
            endOfPage()
            #print("ChangeColor(" + str(random.randint(0, 255)) + ", " + str(random.randint(0, 255)) + ", " + str(random.randint(0, 255)) + ")")

def writeLine(text, size_limit,free_drag_x=0, free_drag_y=0):
    my_text = str(text)

    resetSpace()
    for idx in range(size_limit):
        select_char(my_text[idx], free_drag_x, free_drag_y)
        if(my_text[idx] != " "):
            spaceUnit()

def CropStringToFit(input_str, width):
    if cons._FONT_SIZE_ == 0:
        return ""

    crop_value = int(width/(cons._FONT_SIZE_ * cons._FONT_MULTIPLIER_))
    ret_str = input_str[0:crop_value]

    # Careful when printing $ and special characters when running ahk
    #print("ToolTip, String Crop "+str(input_str)+" to "+str(ret_str)+" crop value "+str(crop_value)+", 0, 30")
    #print("FileAppend, String Crop "+str(input_str)+" to "+str(ret_str)+" crop value "+str(crop_value)+", log.txt")

    if len(ret_str) == 0:
        return ""
    return input_str[0:crop_value]