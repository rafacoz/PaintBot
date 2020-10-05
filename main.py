from PIL import Image
import random


# Lambda functions
lower = lambda a: int((abs(a) + a) / 2)
upper = lambda a: 255 if (a > 255) else a

_R_ = 0  # Tuple R position
_G_ = 1  # Tuple G position
_B_ = 2  # Tuple B position

_X_ = 0  # X Axis code
_Y_ = 1  # X Axis code

# Colors RGB
_BLACK_ = (0, 0, 0)
_RED_ = (255, 0, 0)
_GREEN_ = (0, 255, 0)
_BLUE_ = (0, 0, 255)
_YELLOW_ = (255, 255, 0)
_MAGENTA_ = (255, 0, 255)
_CYAN_ = (0, 255, 255)
_GREY_ = (127, 127, 127)
_WHITE_ = (255, 255, 255)

# Gameboy Green Shades
_GB_GREEN0_ = (202, 220, 159)  # Lightest
_GB_GREEN1_ = (155, 188, 15)
_GB_GREEN2_ = (139, 172, 15)
_GB_GREEN3_ = (48, 98, 48)
_GB_GREEN4_ = (15, 56, 15)  # Darkest

# Shades of Grey
_GB_GREY1_ = (255, 255, 255)  # Lightest
_GB_GREY2_ = (169, 169, 169)
_GB_GREY3_ = (84, 84, 84)
_GB_GREY4_ = (0, 0, 0)  # Darkest

_GB_SINGLE_GREY1_ = 255  # Lightest
_GB_SINGLE_GREY2_ = 169
_GB_SINGLE_GREY3_ = 84
_GB_SINGLE_GREY4_ = 0  # Darkest

# Log
_IS_DEBUG_ = False
_IS_INFO_ = True


def LOG_DEB(logString):
    if (_IS_DEBUG_):
        print("[DEB]\t" + logString)


def LOG_INFO(logString):
    if (_IS_INFO_):
        print("[INFO]\t" + logString)


def comparePixel(rgbTuple1, rgbTuple2, tol=0):
    if (rgbTuple1[_R_] >= (lower(rgbTuple2[_R_] - tol))
            and rgbTuple1[_R_] <= (upper(rgbTuple2[_R_] + tol))
            and rgbTuple1[_G_] >= (lower(rgbTuple2[_G_] - tol))
            and rgbTuple1[_G_] <= (upper(rgbTuple2[_G_] + tol))
            and rgbTuple1[_B_] >= (lower(rgbTuple2[_B_] - tol))
            and rgbTuple1[_B_] <= (upper(rgbTuple2[_B_] + tol))):
        return True
    return False


class PaintBot:
    def __init__(paintbot, imagePath, tolerance):
        LOG_DEB("Entered PaintBot Constructor")

        paintbot.imagePath = imagePath
        paintbot.tolerance = tolerance

        im = Image.open(paintbot.imagePath)
        paintbot.rgbImg = im.convert('RGB')

        LOG_DEB("Exit getImageTupleListBlackFilter")

    def getImageMatrix(self):
        LOG_DEB("Entered getImageMatrix")

        imageMatrix = [[0 for x in range(self.rgbImg.height)] for y in range(self.rgbImg.width)]
        LOG_DEB("Matrix X len: " + str(len(imageMatrix)) + "\tMatrix Y len: " + str(len(imageMatrix[0])))

        for x in range(self.rgbImg.width):
            for y in range(self.rgbImg.height):
                imageMatrix[x][y] = self.rgbImg.getpixel((x, y))
                LOG_DEB(str(imageMatrix[x][y]))

        LOG_DEB("Exit getImageMatrix")
        return imageMatrix

    def getGameboyImageMatrix(self):
        LOG_DEB("Entered getGameboyImageMatrix")

        imageMatrix = [[0 for x in range(self.rgbImg.height)] for y in range(self.rgbImg.width)]
        LOG_DEB("Matrix X len: " + str(len(imageMatrix)) + "\tMatrix Y len: " + str(len(imageMatrix[0])))

        for x in range(self.rgbImg.width):
            for y in range(self.rgbImg.height):
                r, g, b = self.rgbImg.getpixel((x, y))

                if ((r + g + b) / 3 <= _GB_SINGLE_GREY1_ and (r + g + b) / 3 > _GB_SINGLE_GREY2_):  # 255
                    imageMatrix[x][y] = _GB_GREEN1_

                elif ((r + g + b) / 3 <= _GB_SINGLE_GREY2_ and (r + g + b) / 3 > _GB_SINGLE_GREY3_):  # 169
                    imageMatrix[x][y] = _GB_GREEN2_

                elif ((r + g + b) / 3 <= _GB_SINGLE_GREY3_ and (r + g + b) / 3 > _GB_SINGLE_GREY4_):  # 84
                    imageMatrix[x][y] = _GB_GREEN3_

                elif ((r + g + b) / 3 == _GB_SINGLE_GREY4_):  # 0
                    imageMatrix[x][y] = _GB_GREEN4_

                else:
                    LOG_DEB("ERROR")
                    imageMatrix[x][y] = _YELLOW_

                LOG_DEB(str(imageMatrix[x][y]))

        LOG_DEB("Exit getGameboyImageMatrix")
        return imageMatrix

    @staticmethod
    def getNeighborPixel(imgMatrix, rgbPixel, tol=0):
        LOG_DEB("Entered getNeighborPixel")

        max_X = len(imgMatrix)
        max_Y = len(imgMatrix[0])
        matchList = []
        auxList = []

        # Check matches running over X axis
        for y in range(max_Y):
            for x in range(max_X):
                if (comparePixel(imgMatrix[x][y], rgbPixel, tol) and x < (max_X - 1)):
                    # Position is not end of line and pixel matches
                    auxList.append((x, y, imgMatrix[x][y][_R_], imgMatrix[x][y][_G_], imgMatrix[x][y][_B_]))

                elif (comparePixel(imgMatrix[x][y], rgbPixel, tol) and x == (max_X - 1)):
                    # Add last end of line matching pixel
                    auxList.append((x, y, imgMatrix[x][y][_R_], imgMatrix[x][y][_G_], imgMatrix[x][y][_B_]))
                    # Append to final list
                    if (len(auxList) > 1):
                        matchList.append((auxList[0], auxList[-1]))
                    else:
                        matchList.append(auxList[0])
                    # Reset aux list
                    auxList = []

                else:
                    # Pixel does not match rgbPixel
                    # Append current aux to final if not empty
                    if (len(auxList) > 0):
                        if (len(auxList) > 1):
                            matchList.append((auxList[0], auxList[-1]))
                        else:
                            matchList.append(auxList[0])
                        auxList = []

        LOG_DEB("Exit getNeighborPixel")
        return matchList

    @staticmethod
    def printChangeColor(rgbPixel):
        # If wish to runs faster
        # print("SetMouseDelay, 5")
        print("ChangeColor(" + str(rgbPixel[_R_])
              + ", " + str(rgbPixel[_G_])
              + ", " + str(rgbPixel[_B_]) + ")")

    def printAHKScript(self, rgbPixel):
        speedBosterFlag = True
        pixelList = self.getNeighborPixel(self.getImageMatrix(), rgbPixel, self.tolerance)

        if (len(pixelList) == 0):
            return -1

        pb.printChangeColor(rgbPixel)
        for idx in range(len(pixelList)):
            if (_IS_INFO_):
                print("FileAppend, Step " + str(idx)
                      + " Color " + str(rgbPixel[_R_]) + " " + str(rgbPixel[_G_]) + " " + str(rgbPixel[_B_])
                      + " `n, log.txt")
                print("ToolTip, Step " + str(idx)
                      + " Color " + str(rgbPixel[_R_]) + " " + str(rgbPixel[_G_]) + " " + str(rgbPixel[_B_])
                      + ", 0, 30")
            if (len(pixelList[idx]) == 5):
                # Single pixel
                print("MouseMove, " + str(pixelList[idx][0]) + "+DRAG_X," + str(pixelList[idx][1]) + "+DRAG_Y")
                print("Click")
            else:
                # Lined pixel
                print("MouseClickDrag, L, "
                      + str(pixelList[idx][0][0]) + "+DRAG_X,"
                      + str(pixelList[idx][0][1]) + "+DRAG_Y,"
                      + str(pixelList[idx][1][0]) + "+DRAG_X,"
                      + str(pixelList[idx][1][1]) + "+DRAG_Y")
            if (speedBosterFlag):
                # If wish to runs faster, runs once
                # print("SetMouseDelay, 5")
                speedBosterFlag = False


    @staticmethod
    def printHeaderAHK():
        # prints header file
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
        print("DRAG_X = 13")
        print("DRAG_Y = 152")
        print("_SPACE_ = 0")
        print("_LINE_ = 0")

        print("\n")

        print("ChangeColor(R, G, B){")
        print("    Click, 1125, 75 // Color Editor")
        print("    Send {Tab 7}")
        print("    Send %R%")
        print("    Send {Tab}")
        print("    Send %G%")
        print("    Send {Tab}")
        print("    Send %B%")
        print("    Send {Enter}")
        print("}")

        print("SelectPencil(){")
        print("    Click, 320, 70 // Pencil")
        print("}")

        print("IncreaseSize(){")
        print("    Send, ^{NumpadAdd}")
        print("}")

        print("DecreaseSize(){")
        print("    Send, ^{NumpadSub}")
        print("}")

        print("SelectPencil()")
        print("\n")
        print("// Add script")


    @staticmethod
    def printFooterAHK():
        print("\n")
        print("ESC::ExitApp")
        print("#p::Pause")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    color_pallete_div = 128
    pb = PaintBot("fruits.png", int(color_pallete_div/2))
    currentColor = []

    pb.printHeaderAHK()

    for r in range(int(256 / color_pallete_div) + 1):
        for g in range(int(256 / color_pallete_div) + 1):
            for b in range(int(256 / color_pallete_div) + 1):
                currentColor.append(((lower(r * color_pallete_div - 1)), (lower(g * color_pallete_div - 1)),
                                     (lower(b * color_pallete_div - 1))))
                # print(currentColor)

    currentColor = sorted(currentColor, key=lambda x: random.random())
    # currentColor.reverse()
    for elem in range(len(currentColor)):
        pb.printAHKScript(currentColor[elem])

    pb.printFooterAHK()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
