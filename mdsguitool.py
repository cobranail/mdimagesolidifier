# coding:utf-8
import wx
import sys
import os.path

import mdimagesolidifier
import mdsgui

import threading


class mtWorker(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, rqueue, solidifier ,threadID=1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.rqueue = rqueue
        self.solidifier = solidifier
    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        # print "Starting " + self.name
        # print_time(self.name, self.counter, 5)
        # print "Exiting " + self.name
        self.rqueue.append(self)
        assert isinstance(self.solidifier, mdimagesolidifier.ImageSolidifier)
        self.solidifier.solidify()
        self.rqueue.pop(self.rqueue.index(self))


class mdsguitool(mdsgui.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.queue = []
        self.solidifier = mdimagesolidifier.ImageSolidifier()
    def on_convert(self, event):
        srcfile = self.m_filePicker1.GetPath()
        destfile = self.m_filePicker2.GetPath()
        self.solidifier.setsrcfile(srcfile)
        self.solidifier.setdestfile(destfile)
        self.solidifier.ratiolimit = int(self.m_spin_ratiomin.GetValue())
        self.solidifier.qualitylimit = int(self.m_spin_qualitymin.GetValue())
        self.solidifier.qualitylimitmax = int(self.m_spin_qualitymax.GetValue())
        self.solidifier.datalenlimit = int(self.m_spin_datalengthlimit.GetValue())
        #self.solidifier.solidify()
        self.worker = mtWorker(rqueue=self.queue, solidifier=self.solidifier, threadID=1)
        self.worker.start()
        return super().on_convert(event)
    def on_timer(self, event):
        self.m_gauge1.SetValue(self.solidifier.progress)
        return super().on_timer(event)

if __name__=="__main__":
    app = wx.App()
    frame = mdsguitool(None)
    frame.Show()
    app.MainLoop()