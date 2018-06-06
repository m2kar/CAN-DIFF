"""

"""
#   @Time:  2018/5/15 0:15
#   @File:  log-to-json.py
#   @Author:
import json
import os
def traffic2json(filename):
    with open(filename,encoding="utf-8") as fp:
        ll=fp.readlines()
    ld=[]
    for line in ll:
        ld.append(eval(line))
    with open(os.path.splitext(filename)[0]+".json","w",encoding="utf8") as fp:
        json.dump({"ld":ld},fp,ensure_ascii=False,indent=2)


if __name__ == '__main__':
    for each in ["a1","a2","a3","base"]:
        traffic2json(each+".txt")
    traffic2json("流量样本.txt")
    traffic2json("base.txt")

    # with open("流量样本.txt",encoding="utf-8") as fp:
    #     ll=fp.readlines()
    # ld=[]
    # for line in ll:
    #     ld.append(eval(line))
    # with open("sample1.json","w",encoding="utf8") as fp:
    #     json.dump({"ld":ld},fp,ensure_ascii=False,indent=2)

