# -*- coding: utf-8 -*-

from error import Error
from mp.config import Config
from mpmessage_model import MPMessageModel
from wechat import WeChat


error = Error()
wechat = WeChat(
        token=Config.WECHAT.get('token'),
        appid=Config.WECHAT.get('appid'),
        EncodingAESKey=Config.WECHAT.get('EncodingAESKey'))