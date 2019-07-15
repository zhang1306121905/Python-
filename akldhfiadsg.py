import urllib.request
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from tkinter import *

#翻页函数
def getContent(page):
    url = ''
    url = 'https://search.51job.com/list/050000,000000,0000,00,9,99,%25E6%259C%25BA%25E6%25A2%25B0,2,'+str(page)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    fjob = urllib.request.urlopen(url)  # 打开网址
    html = fjob.read().decode('gbk')  # 读取源代码并转为unicode
    return html

#获得一个项目列表
def get(html):
    reg = re.compile( r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>', re.S)  # 匹配换行符
    items = re.findall(reg, html)
    return items

'''
#**************************************************************    测 试 系 统    *************************************************************
html = getContent(1)
items = get(html)
print(items)
print(items[0][0])
#**************************************************************    测 试 完 毕    *************************************************************
'''
#初始化列表
a = ['职业']
b = ['公司']
c = ['工作地点']
d = ['工资']
e = ['发布日期']

for j in range(1, 50):
    print("正在爬取第"+str(j)+"页数据")

    #调用函数将内容返回
    html = getContent(j)#html
    items = get(html)#d

    #把数据放入列表 a,b,c,d,e中
    for i in range(len(items)+1):
        try:
            a.append(items[i][0])
            b.append(items[i][1])
            c.append(items[i][2])
            d.append(items[i][3])
            e.append(items[i][4])
        except IndexError:
            pass
#字典的key值就是CSV表格的列名
dataframe = pd.DataFrame({'职业': a, '公司': b, '工作地点': c, '工资': d, '发布日期': e}, columns=['职业', '公司', '工作地点', '工资', '发布日期'])
#将DataFrame储存为csv
dataframe.to_csv("jobs.csv", index=False, encoding='gbk', header=False)

#配置中文显示
font_1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\SIMLI.ttf')
font_2 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
# 读入文件
file = open("jobs.csv", 'r', encoding='gbk')
#初始化变量
hx= jn = bh = xq = hd = dl = wq = jh = bc = nk = nh = hp = jz = bd = hq = tj = yd = 0
data_list = []
while True:
    # 依次读入文件的每一行
    line = file.readline()
    # 如果读到文件末尾，则退出
    if not line:
        break
    # 先去除每行的前后的空格和回车换行符（\n），然后使用,拆分每行字符串
    words = line.strip().split(',')
    #测试
    print(words[2])

    #按地区对结果分类
    if '河西' in words[2]:
        hx = hx+1
    elif '津南' in words[2]:
        jn = jn+1
    elif '滨海新区' in words[2]:
        bh = bh+1
    elif '西青' in words[2]:
        xq = xq+1
    elif '河东' in words[2]:
        hd = hd+1
    elif '东丽' in words[2]:
        dl = dl+1
    elif '武清' in words[2]:
        wq = wq+1
    elif '静海' in words[2]:
        jh = jh+1
    elif '北辰' in words[2]:
        bc = bc+1
    elif '南开' in words[2]:
        nk = nk+1
    elif '宁河' in words[2]:
        nh = nh+1
    elif '和平' in words[2]:
        hp = hp+1
    elif '蓟州' in words[2]:
        jz = jz+1
    elif '宝坻' in words[2]:
        bd = bd+1
    elif '红桥' in words[2]:
        hq = hq+1
    elif '天津' in words[2]:
        tj = tj+1
    else:
        yd = yd+1
#画图表达 并且生成image.png文件
data = [hx, jn, bh, xq, hd, dl, wq, jh, bc, nk, nh, hp, jz, bd, hq, tj, yd]
labels = ['河西', '津南', '滨海', '西青', '河东', '东丽', '武清', '静海', '北辰', '南开', '宁河', '和平', '蓟州', '宝坻', '红桥', '天津', '异地']
#画图
plt.bar(np.arange(len(data)), data , color='blue', width=0.5)
plt.xticks(np.arange(len(data)), ('河西', '津南', '滨海', '西青', '河东', '东丽', '武清', '静海', '北辰', '南开', '宁河', '和平', '蓟州', '宝坻', '红桥', '天津', '异地'), fontproperties=font_2)
plt.title('机械专业工作地点分布图', FontProperties=font_1, size='30')
plt.xlabel('工作地点', FontProperties=font_1, color='black', size='20')
plt.ylabel('工作数量', FontProperties=font_1, color='black', size='20')
plt.savefig("E:\爬虫练习\大数据爬虫\image.png")
plt.show()

'''
##创建窗口
root = Tk()
#窗口标题
root.title("网易云音乐")
#窗口大小
root.geometry("550x400")
#窗口位置
root.geometry("+700+230")
#创建标签控件
lable = Label(root,text = "机械专业在天津就业地点分析图",font = ('隶书',20))
#定位  pack：包 grid：网格式布局 place： 空间
lable.grid()

#列表框控件
text = Listbox(root,font = ('微软雅黑',15),width =45 ,height =10 )
#columnspan 组件跨越的列数
text.grid(row = 1,columnspan = 2)

#显示窗口 消息循环
root.mainloop()

'''