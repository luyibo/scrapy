__author__ = 'lyb'
#coding=utf-8
import json

c=[]
with open('zhihufenlei.json','w') as b:
    with open('zhihu.json','r') as f:
        for lines in f.readlines():
            js=json.loads(lines)
            print js['question']
            for i in range(len(js['question'])):
                a=[{}]*len(js['question'])
                a[i]['vote']=js['vote'][i]
                a[i]['question']=js['question'][i]
                print js['question']
                c.append(a)
    b.write(str(c))




