# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import pyperclip
import time

class Main(Wox):

    def query(self, keyword):
        output = keyword
        if keyword.isnumeric():
            timeArray = time.localtime(int(keyword) / 1000)
            output = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        else:
            if len(keyword) > 10:
                timeArray = time.strptime(keyword, "%Y-%m-%d %H:%M:%S")
            else:
                timeArray = time.strptime(keyword, "%Y-%m-%d")
            timeStamp = int(time.mktime(timeArray) * 1000)
            output = timeStamp
        results = list()
        results.append({
            "Title": output,
            "SubTitle": "enter copy",
            "IcoPath": "Images/ico.ico",
            "JsonRPCAction": {
                "method": "test_func",
                "parameters": [output],
                "dontHideAfterAction": False      # 运行后是否隐藏Wox窗口
            }
        })
        return results

    def test_func(self, output):
        pyperclip.copy(output)

if __name__ == "__main__":
    Main()