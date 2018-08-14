# -*- coding: utf-8 -*-
# filename: main.py
import threading
import time

from blockmonitor import BlockMgr
from logger import Logger
from votemgr import VoteMgr
import sys

urls = (
    '/wx', 'Handle',
)


if __name__ == '__main__':

    Logger().Init()
    BlockMgr().Instance().Start()
    VoteMgr().Instance().regProducer("accountnum11",1)
    VoteMgr().Instance().regProducer("accountnum22",1)
    VoteMgr().Instance().bwAction("vote11111111","accountnum11",400000,0)
    VoteMgr().Instance().bwAction("vote11111122","accountnum22",600000,0) 
    VoteMgr().Instance().unbwAction("vote11111111","accountnum11",300000,0)
    VoteMgr().Instance().bwAction("vote11111122","accountnum22",500000,0)
    VoteMgr().Instance().bwAction("proxyproxy11",1)   
    try:
        while 1:
            pass
    except KeyboardInterrupt:
        pass


