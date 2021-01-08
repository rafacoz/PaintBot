import constants as cons

def printHeaderAHK(width, height):
    # prints header file
    print("#SingleInstance force")
    print("#CommentFlag //")
    print("// OPTIMIZATIONS START")
    print("SetMouseDelay, 0")
    print("SetDefaultMouseSpeed, 0")

    print("FileDelete, log.txt")
    print("Run, mspaint.exe")
    print("WinWaitActive, ahk_class MSPaintApp,, 2")
    print("Sleep 1000")

    print("SPACE_RATIO = 60")
    print("LINE_RATIO = 300")
    print("DRAW_DRAG_X = " + str(cons._DRAW_DRAG_X_))
    print("DRAW_DRAG_Y = " + str(cons._DRAW_DRAG_Y_))
    print("WRITE_DRAG_X = " + str(cons._WRITE_DRAG_X_))
    print("WRITE_DRAG_Y = " + str(cons._WRITE_DRAG_Y_))
    print("_ZOOM_PERCENT_ = " + str(cons._ZOOM_PERCENT_))
    print("_FONT_SIZE_ = " + str(cons._FONT_SIZE_))
    print("_FONT_FACTOR_ := " + str(cons._FONT_SIZE_ / 10))
    print("_SPACE_ = 0")
    print("_LINE_ = 0")
    print("_SPACE_APPEND_ = " + str(7 * cons._FONT_SIZE_))
    print("_LINE_APPEND_ = " + str(9 * cons._FONT_SIZE_ ))

    print("\n")

    print("ChangeColor(R, G, B){")
    print("    Click, 1000, 75 // Color Editor")
    print("    Sleep 100")
    print("    MouseClickDrag, L, 10, 10, 500, 10")
    print("    Send {Tab 7}")
    print("    Send %R%")
    print("    Send {Tab}")
    print("    Send %G%")
    print("    Send {Tab}")
    print("    Send %B%")
    print("    Send {Enter}")
    print("}")

    print("ResizeCanvas(width, height){")
    print("    Sleep 100")
    print("    Send, ^{e}")
    print("    Send %width%")
    print("    Send {Tab}")
    print("    Send %height%")
    print("    Send {Enter}")
    print("    Sleep 100")
    print("}")

    print("SelectPencil(){")
    print("    Click, 250, 70 // Pencil")
    print("}")

    print("SelectBrush(){")
    print("    Click, 350, 70 // Brush")
    print("}")

    print("SelectEraser(){")
    print("    Click, 250, 105 // Rubber")
    print("}")

    print("SelectColor1(){")
    print("    Click, 690, 70 // Color 2")
    print("}")

    print("SelectColor2(){")
    print("    Click, 750, 70 // Color 2")
    print("}")

    print("IncreaseSize(){")
    print("    Send, ^{NumpadAdd}")
    print("}")

    print("DecreaseSize(){")
    print("    Send, ^{NumpadSub}")
    print("}")

    print("DecreaseMinimum(){")
    print("    Loop, 12 {")
    print("        DecreaseSize()")
    print("    }")
    print("}")

    print("IncreaseToFontSize(font_size){")
    print("    local_font_size := (font_size - 1)")
    print("    Loop, %local_font_size% {")
    print("        IncreaseSize()")
    print("    }")
    print("}")

    print("ZoomOut(){")
    print("    Send, ^{PgDn}")
    print("}")

    print("ZoomIn(){")
    print("    Send, ^{PgUp}")
    print("}")

    print("EraseAll(wait_time){")
    print("    Sleep, wait_time")
    print("    ChangeColor(255, 255, 255)")
    print("    Send, ^{a}")
    print("    Send, {Del}")
    print("    ChangeColor(0, 0, 0)")
    print("}")

    print("ResizeCanvas(" + str(width) + ", " + str(height) + ")")
    print("// Add script")

def printEraseAllAHK(time_in_ms):
    print("EraseAll("+ str(time_in_ms) +")")

def printResizeAHK(width, height):
    print("ResizeCanvas(" + str(width) + ", " + str(height) + ")")
    print("// Add script")

def printSelectPencilAHK():
    print("SelectPencil()")

def printSelectBrushAHK():
    print("SelectBrush()")

def changeToWriteMode(red_value=0, green_value=0, blue_value=0):
    print("\n\n\n")
    print("// WRITE MODE")
    print("SetMouseDelay, 1")
    print("SelectEraser()")
    print("SelectColor2()")
    print("DecreaseMinimum()")
    print("IncreaseToFontSize(" + str(cons._FONT_SIZE_) + ")")

    print("ChangeColor(" + str(red_value)
          + ", " + str(green_value)
          + ", " + str(blue_value) + ")")

def changeToDrawingMode(red_value=0, green_value=0, blue_value=0):
    print("\n\n\n")
    print("// DRAWING MODE")
    print("SetMouseDelay, 0")
    print("DecreaseMinimum()")
    print("SelectColor1()")
    print("SelectPencil()")
    print("ChangeColor(" + str(red_value)
          + ", " + str(green_value)
          + ", " + str(blue_value) + ")")

def printFooterAHK():
    print("\n")
    print("ToolTip, Finished, 0, 30")
    print("FileAppend, Finished, log.txt")
    print("ESC::ExitApp")
    print("#p::Pause")

def changeColor(red_value=0, green_value=0, blue_value=0):
    print("ChangeColor(" + str(red_value)
          + ", " + str(green_value)
          + ", " + str(blue_value) + ")")

def printUpperFrame(width, height, red_value=0, green_value=0, blue_value=0):
    upper_local_drag_x = cons._UPPER_FRAME_DRAG_X_
    upper_local_drag_y = cons._UPPER_FRAME_DRAG_Y_

    print("// Drawing Upper Frame")
    print("ChangeColor(" + str(red_value)
          + ", " + str(green_value)
          + ", " + str(blue_value) + ")")
    print("ToolTip, "+str(width)+" "+str(height)+", 0, 30")
    print("FileAppend, printUpperFrame, log.txt")

    for idx in range(cons._FRAME_H_):
        print("MouseClickDrag, L, " + str(upper_local_drag_x) + ", " + str(upper_local_drag_y + idx) + ", " + str(upper_local_drag_x + width - 1) + ", " + str(upper_local_drag_y + idx) + "")


def printLowerFrame(width, height, red_value=0, green_value=0, blue_value=0):
    lower_local_drag_x = cons._UPPER_FRAME_DRAG_X_
    lower_local_drag_y = cons._UPPER_FRAME_DRAG_Y_ + height + cons._FRAME_H_

    print("// Drawing Lower Frame")
    print("ChangeColor(" + str(red_value)
          + ", " + str(green_value)
          + ", " + str(blue_value) + ")")
    print("ToolTip, "+str(width)+" "+str(height)+", 0, 30")
    print("FileAppend, printLowerFrame, log.txt")

    for idx in range(cons._FRAME_H_):
        print("MouseClickDrag, L, " + str(lower_local_drag_x) + ", " + str(lower_local_drag_y + +idx) + ", " + str(lower_local_drag_x + width - 1) + ", " + str(lower_local_drag_y + idx) + "")

def resetMousePosition(pos_x=0, pos_y=0):
    print("MouseMove, "+str(pos_x)+", "+str(pos_y)+"")