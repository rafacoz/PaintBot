import sys
from enum import Enum
#from instalooter.looters import PostLooter
import os


class CommandEnums(Enum):
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class SourceMedia(CommandEnums):
    eInstagram = "instagram"


class SourceMediaUrl(CommandEnums):
    eInstagram = "instagram"


class DrawingTool(CommandEnums):
    ePencil = "pencil"
    eBrush = "brush"


class ImageQuality(CommandEnums):
    eHighQuality = "high"
    eMediumQuality = "medium"
    eLowQuality = "low"
    eLowestQuality = "lowest"


class ArgvParamPosition(CommandEnums):
    eImgSourceMediaPos = 1
    eImgUrlIdPos = 2
    eImgQualityPos = 3
    eImgDrawingToolPos = 4
    eImgRequestUserPos = 5
    eImgTargetUserPos = 6


class CommandInterpreter:
    # !draw instagram CGnddBuBcXq high brush request_user target_user
    # argv => ['main.py', 'instagram', 'CGnddBuBcXq', 'high', 'brush', 'request_user', 'target_user'] => len  7

    _INSTAGRAM_URL_ID_SIZE_ = 11  # ex CGnddBuBcXq
    _ARGV_MAX_SIZE_ = 7

    _INSTAGRAM_URL_LEFT_SIDE = "https://www.instagram.com/p/"

    def __init__(self, img_source_media="", img_url_id="", img_quality="",
                 drawing_tool="", request_user="", target_user=""):

        self.img_source_media = img_source_media
        self.img_url_id = img_url_id
        self.img_quality = img_quality
        self.drawing_tool = drawing_tool
        self.request_user = request_user
        self.target_user = target_user

    def initialize(self, input_sys_argv):
        if len(input_sys_argv) != self._ARGV_MAX_SIZE_:
            return False
        self.img_source_media = input_sys_argv[ArgvParamPosition.eImgSourceMediaPos.value]
        self.img_url_id = input_sys_argv[ArgvParamPosition.eImgUrlIdPos.value]
        self.img_quality = input_sys_argv[ArgvParamPosition.eImgQualityPos.value]
        self.drawing_tool = input_sys_argv[ArgvParamPosition.eImgDrawingToolPos.value]
        self.request_user = input_sys_argv[ArgvParamPosition.eImgRequestUserPos.value]
        self.target_user = input_sys_argv[ArgvParamPosition.eImgTargetUserPos.value]
        return True

    def is_img_source_media_valid(self):
        if not SourceMedia.has_value(self.img_source_media):
            return False
        return True

    def is_img_url_id_valid(self):
        if self.img_source_media == SourceMedia.eInstagram.value \
                and (len(self.img_url_id) != self._INSTAGRAM_URL_ID_SIZE_):
            return False
        return True

    def is_img_quality_valid(self):
        if not ImageQuality.has_value(self.img_quality):
            return False
        return True

    def is_drawing_tool_valid(self):
        if not DrawingTool.has_value(self.drawing_tool):
            return False
        return True

    def is_request_user_valid(self):
        if not isinstance(self.request_user, str):
            return False
        return True

    def is_target_user_valid(self):
        if not isinstance(self.target_user, str):
            return False
        return True

    def is_valid(self):
        if self.is_target_user_valid() \
                and self.is_img_url_id_valid() \
                and self.is_img_quality_valid() \
                and self.is_drawing_tool_valid() \
                and self.is_request_user_valid()\
                and self.is_target_user_valid():
            return True
        return False


# input argv: >python CommandInterpreter.py instagram CGnddBuBcXq lowest pencil @bot @target => True
command_interpreter = CommandInterpreter()
command_interpreter.initialize(sys.argv)
print(command_interpreter.is_valid())


looter_cmd_str = "instalooter post "
download_url_str = "\"" + command_interpreter._INSTAGRAM_URL_LEFT_SIDE + command_interpreter.img_url_id + "\""
file_name_opt = " -T {username}_{code}_{id}_{datetime}"
download_file_name = " ~/TwitchPaintBot/" + command_interpreter.request_user

full_command = looter_cmd_str + download_url_str + file_name_opt + download_file_name

os.system(full_command)
print(full_command)