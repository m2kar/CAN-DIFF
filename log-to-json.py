"""

"""
#   @Time:  2018/5/15 0:15
#   @File:  log-to-json.py
#   @Author:
import json

if __name__ == '__main__':
    with open("流量样本.txt",encoding="utf-8") as fp:
        ll=fp.readlines()
    ld=[]
    for line in ll:
        ld.append(eval(line))
    with open("sample1.json","w",encoding="utf8") as fp:
        json.dump({"ld":ld},fp,ensure_ascii=False,indent=2)

