from PIL import Image
import random
import sys
import constants as cons


def LOG_DEB(logString):
    if (cons._IS_DEBUG_):
        print("[DEB]\t" + logString)


def LOG_INFO(logString):
    if (cons._IS_INFO_):
        print("[INFO]\t" + logString)


def comparePixel(rgbTuple1, rgbTuple2, tol=0):
    if (rgbTuple1[cons._R_] >= (cons.lower(rgbTuple2[cons._R_] - tol))
            and rgbTuple1[cons._R_] <= (cons.upper(rgbTuple2[cons._R_] + tol))
            and rgbTuple1[cons._G_] >= (cons.lower(rgbTuple2[cons._G_] - tol))
            and rgbTuple1[cons._G_] <= (cons.upper(rgbTuple2[cons._G_] + tol))
            and rgbTuple1[cons._B_] >= (cons.lower(rgbTuple2[cons._B_] - tol))
            and rgbTuple1[cons._B_] <= (cons.upper(rgbTuple2[cons._B_] + tol))):
        return True
    return False

class PaintBot:
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

    def __init__(paintbot, imagePath, color_pallete_div, tolerance):
        LOG_DEB("Entered PaintBot Constructor")

        paintbot.imagePath = imagePath
        paintbot.tolerance = tolerance
        paintbot.colorPalleteDiv = color_pallete_div

        im = Image.open(paintbot.imagePath)
        paintbot.rgbImg = im.convert('RGB')

        paintbot.imageW = paintbot.rgbImg.width
        paintbot.imageH = paintbot.rgbImg.height

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

                if ((r + g + b) / 3 <= self._GB_SINGLE_GREY1_ and (r + g + b) / 3 > self._GB_SINGLE_GREY2_):  # 255
                    imageMatrix[x][y] = self._GB_GREEN1_

                elif ((r + g + b) / 3 <= self._GB_SINGLE_GREY2_ and (r + g + b) / 3 > self._GB_SINGLE_GREY3_):  # 169
                    imageMatrix[x][y] = self._GB_GREEN2_

                elif ((r + g + b) / 3 <= self._GB_SINGLE_GREY3_ and (r + g + b) / 3 > self._GB_SINGLE_GREY4_):  # 84
                    imageMatrix[x][y] = self._GB_GREEN3_

                elif ((r + g + b) / 3 == self._GB_SINGLE_GREY4_):  # 0
                    imageMatrix[x][y] = self._GB_GREEN4_

                else:
                    LOG_DEB("ERROR")
                    imageMatrix[x][y] = cons._CYAN_

                LOG_DEB(str(imageMatrix[x][y]))

        LOG_DEB("Exit getGameboyImageMatrix")
        return imageMatrix

    @staticmethod
    def getNeighborPixel(self, imgMatrix, rgbPixel, tol=0):
        LOG_DEB("Entered getNeighborPixel")

        max_X = len(imgMatrix)
        max_Y = len(imgMatrix[0])
        self.imageW = max_X
        self.imageH = max_Y

        matchList = []
        auxList = []

        # Check matches running over X axis
        for y in range(max_Y):
            for x in range(max_X):
                if (comparePixel(imgMatrix[x][y], rgbPixel, tol) and x < (max_X - 1)):
                    # Position is not end of line and pixel matches
                    auxList.append((x, y, imgMatrix[x][y][cons._R_], imgMatrix[x][y][cons._G_], imgMatrix[x][y][cons._B_]))

                elif (comparePixel(imgMatrix[x][y], rgbPixel, tol) and x == (max_X - 1)):
                    # Add last end of line matching pixel
                    auxList.append((x, y, imgMatrix[x][y][cons._R_], imgMatrix[x][y][cons._G_], imgMatrix[x][y][cons._B_]))
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
        print("ChangeColor(" + str(rgbPixel[cons._R_])
              + ", " + str(rgbPixel[cons._G_])
              + ", " + str(rgbPixel[cons._B_]) + ")")

        # Color randomizer
        #print("ChangeColor(" + str(random.randint(0, 255))
        #      + ", " + str(random.randint(0, 255))
        #      + ", " + str(random.randint(0, 255)) + ")")

    def printAHKScript(self, rgbPixel):
        speedBosterFlag = True
        pixelList = self.getNeighborPixel(self, self.getImageMatrix(), rgbPixel, self.tolerance)

        if (len(pixelList) == 0):
            return -1

        self.printChangeColor(rgbPixel)
        for idx in range(len(pixelList)):
            if (cons._IS_INFO_):
                print("FileAppend, Step " + str(idx)
                      + " Color " + str(rgbPixel[cons._R_]) + " " + str(rgbPixel[cons._G_]) + " " + str(rgbPixel[cons._B_])
                      + " `n, log.txt")
                print("ToolTip, Step " + str(idx)
                      + " Color " + str(rgbPixel[cons._R_]) + " " + str(rgbPixel[cons._G_]) + " " + str(rgbPixel[cons._B_])
                      + ", 0, 30")
            if (len(pixelList[idx]) == 5):
                # Single pixel
                print("MouseMove, " + str(pixelList[idx][0]) + "+DRAW_DRAG_X," + str(pixelList[idx][1]) + "+DRAW_DRAG_Y")
                print("Click")
            else:
                # Lined pixel
                print("MouseClickDrag, L, "
                      + str(pixelList[idx][0][0]) + "+DRAW_DRAG_X,"
                      + str(pixelList[idx][0][1]) + "+DRAW_DRAG_Y,"
                      + str(pixelList[idx][1][0]) + "+DRAW_DRAG_X,"
                      + str(pixelList[idx][1][1]) + "+DRAW_DRAG_Y")
            if (speedBosterFlag):
                # If wish to runs faster, runs once
                # print("SetMouseDelay, 5")
                speedBosterFlag = False



    def generateImageAHK(self):
        #  pb = df.PaintBot(image_file_path, int(color_pallete_div / 2))
        current_color = []

        for r in range(int(256 / self.colorPalleteDiv) + 1):
            for g in range(int(256 / self.colorPalleteDiv) + 1):
                for b in range(int(256 / self.colorPalleteDiv) + 1):
                    current_color.append(((cons.lower(r * self.colorPalleteDiv - 1)), (cons.lower(g * self.colorPalleteDiv - 1)),
                                         (cons.lower(b * self.colorPalleteDiv - 1))))
                    # print(currentColor)

        # Randomizer
        current_color = sorted(current_color, key=lambda x: random.random())

        # Reversers
        #current_color.reverse()
        for elem in range(len(current_color)):
            self.printAHKScript(current_color[elem])