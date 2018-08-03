# -*- coding: utf-8 -*-# filename: receive.py

import xml.etree.ElementTree as ET 

def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    
    msg_type = xmlData.find('MsgType').text
   
    if msg_type == 'text':
        return TextMsg(xmlData)

class Msg(object):
    def __init__(self, xmlData):

        toUserName = xmlData.find('ToUserName')
        if not toUserName is None:
           self.ToUserName = toUserName.text
        
        FromUserName = xmlData.find('FromUserName')
        if not FromUserName is None:
           self.FromUserName = FromUserName.text

        CreateTime = xmlData.find('CreateTime')
        if not CreateTime is None:
           self.CreateTime = CreateTime.text
        
        MsgType = xmlData.find('MsgType')
        if not MsgType is None:
           self.MsgType = MsgType.text
        
        MsgId = xmlData.find('MsgId')
        if not MsgId is None:
           self.MsgId = MsgId.text
        
   

class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
