import random
import time
import 模块识别器1
import 自定义函数解释器
import ast
userlist = []
user = ['','','普通用户']
adduser = ''
keylist = []
addkey = ''
addbuy = '0'
AddGit = ''
AddTxtToGit = ''
GitList = []
RTxt = []
print('普通用户激活码gnQ6')
with open('C:\\解释器\\环境变量\\账户列表.txt','r',encoding='utf-8') as u:
    u1 = u.readlines()
    for u2 in u1:
        u3 = u2.split()
        userlist.append(u3[0:4])
with open('C:\\解释器\\环境变量\\激活码列表.txt','r',encoding='utf-8') as d:
    d1 = d.readlines()
    for d2 in d1:
        keylist.append(d2)
with open('C:\\解释器\\环境变量\\Git仓库列表.txt','r',encoding='utf-8') as g:
    g3 = g.readlines()
    for g4 in g3:
        GitList.append(g4.split()[0:2])
while True:
    num1 = input('>>>')
    num4 = '1'
    num5 = 0
    nun1 = None
    nun2 = 0
    num7 = '0'
    d2 = {}
    num8 = '0'
    x9 = '0'
    x114514 = 0
    if num1=='退出（）':
        break
    elif num1=='注册（）':
        us1 = input('用户名：')
        us2 = input('密码：')
        us3 = input('激活码：')
        if us3=='gnQ6':
            us4 = '普通用户'
            us5 = '未订阅'
        elif us3=='jVn5':
            us4 = '开发者'
            us5 = '已订阅'
        else:
            print('注册失败，请重试')
            us4 = ''
            continue
        usn = []
        for u4 in userlist:
            usn.append(u4[0])
        if us1 in usn:
            print('已有此用户名，请重试。')
            continue
        adduser = us1+' '+us2+' '+us4+' '+us5+' '+'\n'
        print('注册完成，重启解释器。')
        break
    elif num1=='登录（）':
        usn5 = input('用户名：')
        usn6 = input('密码：')
        for u5 in userlist:
            if usn5 == u5[0] and usn6 == u5[1]:
                user = u5
                print('登录成功')
                break
        if user==['','','普通用户']:
            print('登录失败请重试。')
        continue
    elif num1=='查看账户信息（）':
        if user!=['','','普通用户']:
            print('用户名：'+user[0])
            print('密码：' + user[1])
            print('账户权限：'+user[2])
            print('编码 pro 订阅状态：'+user[3])
        else:
            print('您还未登录。')
        continue
    elif num1=='查看账户列表（）':
        if user[2]=='开发者':
            for u6 in userlist:
                print(f'用户名：{u6[0]}密码：{u6[1]}账户权限：{u6[2]}编码 pro 订阅状态：{u6[3]}')
        else:
            print('权限不足。')
        continue
    elif num1=='退出账户（）':
        user = ['','','普通用户']
        print('退出成功。')
        continue
    elif num1=='获取订阅编码 pro（）' and user!=['','','普通用户']:
        addpath = input('发送路径：')
        addkey = [str(random.randint(100000,999999))+'\n',addpath+'激活码.txt']
        print('发送完毕，重启解释器。')
        break
    elif num1=='激活订阅编码 pro（）' and user!=['','','普通用户']:
        ab = input('激活码：')
        if ab+'\n' in keylist:
            userlist[userlist.index(user)][3] = '已订阅'
            keylist.remove(ab+'\n')
            addbuy = '1'
            print('激活成功，重启解释器。')
            break
        else:
            print('激活码错误。')
            continue
    elif num1=='创建 Git 仓库（）' and user!=['','','普通用户']:
        g1 = input('Git 名称：')
        g2 = input('邀请码：')
        TORF = False
        for GB in GitList:
            if g1 == GB[0]:
                TORF = True
                break
        if TORF:
            print('已有此Git 仓库，请重试。')
            continue
        AddGit = [g1,g2]
        print('创建成功，重启解释器。')
        break
    elif num1=='将文件添加到 Git 仓库（）' and user!=['','','普通用户']:
        ug1 = input('Git 名称：')
        ug2 = input('邀请码：')
        ug3 = input('文件路经：')
        name = input('储存文件名：')
        Git = ''
        for ug4 in GitList:
            if ug1==ug4[0] and ug2==ug4[1]:
                Git = ug4
        if Git=='':
            print('添加失败，请重试。')
            continue
        else:
            n1 = False
            with open('C:\\解释器\\环境变量\\Git仓库储存\\'+Git[0]+'.txt','r',encoding='utf-8') as Names:
                for Name in Names.readlines():
                    if Name.split('%start%')[0]==name:
                        n1 = True
                        break
            if n1:
                print('此 Git 内已有相同文件名的文件，请重试。')
                continue
            AddTxtToGit = [Git[0],ug3,name]
            print('添加成功，重启解释器。')
            break
    elif num1=='从 Git 仓库中提取文件（）' and user!=['','','<UNK>']:
        rg1 = input('Git 名称：')
        rg2 = input('邀请码：')
        rg3 = input('文件名：')
        rg5 = input('提取目标路经：')
        RGit = ''
        for rg4 in GitList:
            if rg1==rg4[0] and rg2==rg4[1]:
                RGit = rg4
        if RGit=='':
            print('提取失败，请重试。')
            continue
        else:
            with open('C:\\解释器\\环境变量\\Git仓库储存\\'+RGit[0]+'.txt','r',encoding='utf-8') as r:
                RLines = r.readlines()
                TxtS = {}
                for rLine in RLines:
                    TxtS[rLine.split('%start%')[0]] = rLine.split('%start%')[1]
                if rg3 in TxtS:
                    RTxtLines = []
                    for RLine in TxtS[rg3].split('%endl%')[0:-1]:
                        RTxtLines.append(RLine)
                    RTxt.append(rg5)
                    RTxt.append(RTxtLines)
                    print('提取成功，重启解释器。')
                    break
                else:
                    print('提取失败，请重试。')
                    continue
    if user==['','','普通用户']:
        continue
    with open(num1,'r',encoding='utf-8') as n1:
        list1 = ['<空值>','<真>','<假>']
        l1 = n1.readlines()
        if len(l1)!=1:
            n2 = ''
            for i in l1:
                n2+=i
            l1 = n2.split('\n')
        d1 = {}
        num2 = 0
        t = time.time()
        for j in l1:
            num2 += 1
            if nun1==None and x9=='0':
                if '打印（' in j and '）' in j and '随机抽取变量并' not in j:
                    n3 = j.replace('打印（','_')
                    n4 = n3.replace('）','_')
                    l2 = n4.split('_')
                    if '‘' in l2[1] and '’' in l2[1]:
                        n5 = l2[1].replace('‘','_')
                        n6 = n5.replace('’','_')
                        l3 = n6.split('_')
                        print(l3[1])
                    else:
                        try:
                            int(l2[1])
                        except:
                            if l2[1] not in list(d1.keys()) and l2[1] not in list1:
                                print(f'''文件名：{num1} 名字错误 第{num2}行
{l2[1]}未定义''')
                                break
                            else:
                                if l2[1] in list(d1.keys()):
                                    if '‘' in d1[l2[1]] and '’' in d1[l2[1]]:
                                        n5 = d1[l2[1]].replace('‘','_')
                                        n6 = n5.replace('’','_')
                                        l3 = n6.split('_')
                                        print(l3[1])
                                    else:
                                        print(d1[l2[1]])
                                else:
                                    print(l2[1])
                        else:
                            print(l2[1])
                elif j=='':
                    pass
                elif len(j)>=4 and '<注释>' in j:
                    if j[0]+j[1]+j[2]+j[3]=='<注释>':
                        pass
                elif '赋值' in j:
                    l4 = j.split('赋值',1)
                    if '‘' in l4[1] and '’' in l4[1] and '（' not in l4[1] and '）' not in l4[1] and '==' not in l4[1] and '+' not in l4[1] and '-' not in l4[1] and '*' not in l4[1] and '/' not in l4[1] and '列表：' not in l4[1]:
                        if '，' not in l4[0]:
                            n3 = ''
                            for n in l4[1]:
                                if n!='\r':
                                    n3+=n
                            d1[l4[0]] = n3
                        else:
                            l5 = []
                            for m in l4[1]:
                                l5.append(m)
                            l5.remove('‘')
                            l5.remove('’')
                            if '\r' in l5:
                                l5.remove('\r')
                            l6 = l4[0].split('，')
                            if len(l5)!=len(l6):
                                if len(l5)<len(l6):
                                    print(f'''文件名：{num1} 语法错误 第{num2}行
对象少{len(l6) - len(l5)}''')
                                    break
                                else:
                                    print(f'''文件名：{num1} 语法错误 第{num2}行
对象多{len(l5) - len(l6)}''')
                                    break
                            else:
                                for l in range(len(l6)):
                                    d1[l6[l]] = '‘'+l5[l]+'’'
                    elif ('（' not in l4[1] or '）' not in l4[1]) and ('+' not in l4[1] and '-' not in l4[1] and '*' not in l4[1] and '/' not in l4[1] and '==' not in l4[1]) and ('<' not in l4[1] or '>' not in l4[1]) and l4[1] not in d2 and '列表：' not in l4[1]:
                        n3 = ''
                        for n in l4[1]:
                            if n!='\r':
                                n3+=n
                        l4[1] = n3
                        try:
                            int(l4[1])
                        except:
                            if l4[1] not in list(d1.keys()) and l4[1] not in list1:
                                print(f'''文件名：{num1} 名字错误 第{num2}行
{l4[1]}未定义''')
                                break
                            else:
                                if l4[1] in list(d1.keys()):
                                    if '‘' not in d1[l4[1]] and '’' not in d1[l4[1]] and '，' not in l4[0]:
                                        d1[l4[0]] = d1[l4[1]]
                                    else:
                                        l5 = []
                                        for m in d1[l4[1]]:
                                            l5.append(m)
                                        l5.remove('‘')
                                        l5.remove('’')
                                        l6 = l4[0].split('，')
                                        if len(l5)!=len(l6):
                                            if len(l5)<len(l6):
                                                print(f'''文件名：{num1} 语法错误 第{num2}行
对象少{len(l6) - len(l5)}''')
                                                break
                                            else:
                                                print(f'''文件名：{num1}语法错误 第{num2}行
对象多{len(l5) - len(l6)}''')
                                                break
                                        else:
                                            for l in range(len(l6)):
                                                d1[l6[l]] = '‘'+l5[l]+'’'
                                else:
                                    d1[l4[0]] = l4[1]
                        else:
                            d1[l4[0]] = l4[1]
                    else:
                        if '输入' == l4[1][:2] and user[3]=='已订阅':
                            n8 = l4[1].replace('输入（','_')
                            n9 = n8.replace('）','_')
                            l7 = n9.split('_')
                            if '‘' not in l7[1] or '‘' not in l7[1]:
                                if l7[1] not in list(d1.keys()):
                                    print(f'''文件名：{num1} 类型错误 第{num2}行
参数类型应为字符串''')
                                    break
                                else:
                                    if '‘' not in d1[l7[1]] or '‘' not in d1[l7[1]]:
                                        print(f'''文件名：{num1} 类型错误 第{num2}行
参数类型应为字符串''')
                                        break
                                    else:
                                        n13 = d1[l7[1]].replace('’','_')
                                        n14 = n13.replace('‘','_')
                                        l9 = n14.split('_')
                                        n15 = input(l9[1])
                                        d1[l4[0]] = '‘' + n15 + '’'
                            else:
                                n10 = l7[1].replace('’','_')
                                n11 = n10.replace('‘','_')
                                l8 = n11.split('_')
                                n12 = input(l8[1])
                                d1[l4[0]] = '‘' + n12 + '’'
                        elif '变量类型' == l4[1][:4]:
                            n16 = l4[1].replace('变量类型（','_')
                            n17 = n16.replace('）','_')
                            l16 = n17.split('_')
                            if l16[1] not in list(d1.keys()):
                                print(f'''文件名：{num1} 参数错误 第{num2}行
{l16}不是变量''')
                                break
                            else:
                                if '’' in d1[l16[1]] and '‘' in d1[l16[1]]:
                                    d1[l4[0]] = '‘字符串’'
                                else:
                                    try:
                                        int(d1[l16[1]])
                                    except:
                                        if d1[l16[1]]=='<真>' or d1[l16[1]]=='<假>':
                                            d1[l4[0]] = '‘布尔’'
                                        else:
                                            d1[l4[0]] = '‘空型’'
                                    else:
                                        d1[l4[0]] = '‘数字’'
                        elif l4[1]=='计时——结束（）':
                            if num4=='2':
                                n20 = time.time() - num5
                                d1[l4[0]] = str(n20)
                                num4 = '1'
                                num5 = 0
                            else:
                                print(f'''文件名：{num1} 语法错误 第{num2}行
计时没有开始''')
                                break
                        elif '整除' in l4[1][:2]:
                            n21 = l4[1].replace('整除（','_')
                            n22 = n21.replace('）','_')
                            l17 = n22.split('_')
                            l18 = l17[1].split('，')
                            num6 = '1'
                            l19 = []
                            for o in l18:
                                try:
                                    int(o)
                                except:
                                    if o not in list(d1.keys()):
                                        print(f'''文件名：{num1} 参数错误 等{num2}行
‘整除（）’函数每个参数类型都应是整数''')
                                        num6 = '2'
                                        break
                                    else:
                                        try:
                                            int(d1[o])
                                        except:
                                            print(f'''文件名：{num1} 参数错误 等{num2}行
‘整除（）’函数每个参数类型都应是整数''')
                                            num6 = '2'
                                            break
                                        else:
                                            n23 = int(d1[o])
                                else:
                                    n23 = int(o)
                                if num6=='2':
                                    pass
                                else:
                                    try:
                                        int(l18[0])
                                    except:
                                        if n23 % int(d1[l18[0]]) == 0:
                                            l19.append(n23)
                                    else:
                                        if n23%int(l18[0])==0:
                                            l19.append(n23)
                            if num6 == '2':
                                break
                            try:
                                int(l18[0])
                            except:
                                l19.remove(int(d1[l18[0]]))
                            else:
                                l19.remove(int(l18[0]))
                            l20 = []
                            for p in l19:
                                l20.append('，')
                                l20.append(str(p))
                            l20.remove('，')
                            n24 = ''
                            for q in l20:
                                n24+=q
                            d1[l4[0]] = '‘'+n24+'’'
                        elif '+' in l4[1] or '-' in l4[1] or '*' in l4[1] or '/' in l4[1]:
                            try:
                                d1[l4[0]] = str(eval(l4[1]))
                            except:
                                n29 = l4[1]
                                LV1 = []
                                LV2 = []
                                for k1 in list(d1.keys()):
                                    if k1 in n29:
                                        LV1.append(k1)
                                        LV2.append(len(k1))
                                LV2.sort(reverse=True)
                                LV3 = []
                                for v1 in LV2:
                                    v = ''
                                    for v2 in LV1:
                                        if len(v2) == v1:
                                            LV3.append(v2)
                                            v = v2
                                            break
                                for v3 in LV3:
                                    if v3 in n29:
                                        n29 = n29.replace(v3,d1[v3])
                                try:
                                    d1[l4[0]] = str(eval(n29))
                                except:
                                    print(f'''文件名：{num1} 语法错误 第{num2}行
只支持数字计算''')
                                    break
                        elif l4[1] in list(d2.keys()):
                            d3 = d1.copy()
                            for i1 in range(d2[l4[1]][1]):
                                if '传参 ' not in l1[num2 + i1]:
                                    print(f'''文件名：{num1} 传参错误 第{num2}行
参数漏写''')
                                    num7 = '1'
                                    break
                                else:
                                    for j1 in list(d1.keys()):
                                        if '%%' in j1 and d1[j1] == None and d2[l4[1]][2][i1]==j1:
                                            n28 = l1[num2 + i1].split('传参 ')
                                            d1[j1] = n28[1]
                                            try:
                                                int(n28[1])
                                            except:
                                                if '‘' in n28[1] and '’' in n28[1]:
                                                    d1[j1] = n28[1]
                                                elif n28[1] in list(d1.keys()):
                                                    d1[j1] = d1[n28[1]]
                                                else:
                                                    num8 = '1'
                                                    print(f'''文件名：{num1} 名字错误 第{num2}行
{n28[1]}未定义''')
                                                    break
                                            else:
                                                d1[j1] = n28[1]
                                if num8 == '1':
                                    break
                            if num7 == '1' or num8 == '1':
                                num7 = '0'
                                num8 = '0'
                                break
                            l24 = 自定义函数解释器.job3(d2[l4[1]], num1, num2, d1)
                            d1 = d3.copy()
                            d1[l4[0]] = l24[1]
                            if l24[2]=='1':
                                break
                        elif '整数' == l4[1][:2]:
                            n30 = l4[1].replace('整数（','_')
                            n31 = n30.replace('）','_')
                            l25 = n31.split('_')
                            if '‘' not in l25[1] or '’' not in l25[1]:
                                if l25[1] not in list(d1.keys()):
                                    print(f'''文件名：{num1} 类型错误 第{num2}行
‘整数（）’的参数应是含数字的字符串类型''')
                                    break
                                else:
                                    if '‘' not in d1[l25[1]] or '’' not in d1[l25[1]]:
                                        print(f'''文件名：{num1} 类型错误 第{num2}行
‘整数（）’的参数应是含数字的字符串类型''')
                                        break
                                    n32 = d1[l25[1]]
                            else:
                                n32 = l25[1]
                            n33 = n32.replace('‘','_')
                            n34 = n33.replace('’','_')
                            l26 = n34.split('_')
                            try:
                                int(l26[1])
                            except:
                                print(f'''文件名：{num1} 类型错误 第{num2}行
‘整数（）’的参数应是含数字的字符串类型''')
                                break
                            else:
                                d1[l4[0]] = l26[1]
                        elif '字符串' == l4[1][:3]:
                            n35 = l4[1].replace('字符串（', '_')
                            n36 = n35.replace('）', '_')
                            l27 = n36.split('_')
                            try:
                                int(l27[1])
                            except:
                                if l27[1] in list(d1.keys()):
                                    try:
                                        int(d1[l27[1]])
                                    except:
                                        print(f'''文件名：{num1} 类型错误 第{num2}行
‘字符串（）’的参数应是整数类型''')
                                        break
                                    else:
                                        n37 = d1[l27[1]]
                                else:
                                    print(f'''文件名：{num1} 类型错误 第{num2}行
‘字符串（）’的参数应是整数类型''')
                                    break
                            else:
                                n37 = l27[1]
                            d1[l4[0]] = '‘'+n37+'’'
                        elif '==' in l4[1]:
                            l28 = l4[1].split('==')
                            try:
                                int(l28[1])
                                int(l28[0])
                            except:
                                if (('‘' in l28[0] and '’' in l28[0]) and ('‘' in l28[1] and '’' in l28[1])) or (l28[0] in list1 and l28[1] in list1):
                                    if l28[0]==l28[1]:
                                        d1[l4[0]] = '<真>'
                                    else:
                                        d1[l4[0]] = '<假>'
                                elif l28[0] in list(d1.keys()) or l28[1] in list(d1.keys()):
                                    if l28[0] in list(d1.keys()) and l28[1] not in list(d1.keys()):
                                        if d1[l28[0]] == l28[1]:
                                            d1[l4[0]] = '<真>'
                                        else:
                                            d1[l4[0]] = '<假>'
                                    elif l28[1] in list(d1.keys()) and l28[0] not in list(d1.keys()):
                                        if l28[0] == d1[l28[1]]:
                                            d1[l4[0]] = '<真>'
                                        else:
                                            d1[l4[0]] = '<假>'
                                    else:
                                        if d1[l28[0]] == d1[l28[1]]:
                                            d1[l4[0]] = '<真>'
                                        else:
                                            d1[l4[0]] = '<假>'
                                else:
                                    print(f'''文件名：{num1} 参数错误 第{num2}行
{l28[0]}或{l28[1]}未定义''')
                                    break
                            else:
                                if l28[0] == l28[1]:
                                    d1[l4[0]] = '<真>'
                                else:
                                    d1[l4[0]] = '<假>'
                        elif '<随机数> ' == l4[1][:6]:
                            l32 = l4[1].split(' ')
                            try:
                                int(l32[2])
                            except:
                                if l32[2] in d1:
                                    try:
                                        int(d1[l32[2]])
                                    except:
                                        print(f'''文件名：{num1} 参数错误 第{num2}行
参数必须是整数''')
                                        break
                                    else:
                                        r1 = int(d1[l32[2]])
                                else:
                                    print(f'''文件名：{num1} 参数错误 第{num2}行
参数必须是整数''')
                                    break
                            else:
                                r1 = int(l32[2])
                            try:
                                int(l32[1])
                            except:
                                if l32[1] in d1:
                                    try:
                                        int(d1[l32[1]])
                                    except:
                                        print(f'''文件名：{num1} 参数错误 第{num2}行
参数必须是整数''')
                                        break
                                    else:
                                        r2 = int(d1[l32[1]])
                                else:
                                    print(f'''文件名：{num1} 参数错误 第{num2}行
参数必须是整数''')
                                    break
                            else:
                                r2 = int(l32[1])
                            d1[l4[0]] = str(random.randint(r2,r1))
                        elif '列表：' == l4[1][:3]:
                            s1 = l4[1].split('列表：')
                            sl1 = s1[1].split('，')
                            sl2 = ''
                            st = False
                            for s2 in sl1:
                                if '‘' in s2 and '’' in s2:
                                    sl2+=s2
                                else:
                                    try:
                                        int(s2)
                                    except:
                                        if s2 in list1:
                                            sl2+=s2
                                        elif s2 in d1:
                                            sl2+=d1[s2]
                                        else:
                                            print(f'''文件名：{num1} 名字错误 第{num2}行
{s2}未定义''')
                                            st = True
                                            break
                                    else:
                                        sl2+=s2
                                sl2+='，'
                            if st:
                                break
                            d1[l4[0]] = '‘'+sl2[:-1]+'’'
                        elif '<列表索引> ' == l4[1][:7]:
                            s6 = l4[1].split()[1:]
                            try:
                                int(s6[1])
                            except:
                                if s6[1] in d1:
                                    try:
                                        int(d1[s6[1]])
                                    except:
                                        print(f'''文件名：{num1} 名字错误 第{num2}行
{s6[1]}未定义''')
                                        break
                                    else:
                                        sn = d1[s6[1]]
                                else:
                                    print(f'''文件名：{num1} 名字错误 第{num2}行
{s6[1]}未定义''')
                                    break
                            else:
                                sn = s6[1]
                            if s6[0] in d1:
                                if '‘' in d1[s6[0]] and '’' in d1[s6[0]]:
                                    s7 = d1[s6[0]][1:-1].split('，')
                                    if int(sn)>=len(s7):
                                        print(f'''文件名：{num1} 索引错误 第{num2}行
索引超出范围''')
                                        break
                                    else:
                                        d1[l4[0]] = s7[int(sn)]
                                else:
                                    print(f'''文件名：{num1} 名字错误 第{num2}行
参数应是字符串列表''')
                                    break
                            else:
                                print(f'''文件名：{num1} 名字错误 第{num2}行
参数应是字符串列表''')
                                break
                        else:
                            print(f'''文件名：{num1} 名字错误 第{num2}行
{l4[1]}未定义''')
                            break
                elif '<列表输出> ' in j:
                    s3 = j.split()
                    if s3[1] in d1:
                        if '‘' in d1[s3[1]] and '’' in d1[s3[1]]:
                            s4 = d1[s3[1]][1:-1].split('，')
                            sl3 = ''
                            for s5 in s4:
                                sl3 += s5 + '，'
                            print(sl3[:-1])
                        else:
                            print(f'''文件名：{num1} 名字错误 第{num2}行
参数应是字符串列表''')
                            break
                    else:
                        print(f'''文件名：{num1} 名字错误 第{num2}行
参数应是字符串列表''')
                        break
                elif j=='退出（）':
                    break
                elif '<删除>' in j and len(j)>=4:
                    if j[0]+j[1]+j[2]+j[3]=='<删除>':
                        l1 = j.split('<删除>',1)
                        l2 = l1[1].split('，')
                        num3 = '1'
                        for k in l2:
                            if k not in list(d1.keys()):
                                print(f'''文件名：{num1} 名字错误 第{num2}行
{k}未定义''')
                                num3 = '2'
                                break
                            else:
                                d1.pop(k)
                        if num3=='2':
                            break
                elif j=='随机抽取变量并打印（）':
                    n7 = random.choice(list(d1.keys()))
                    print(d1[n7])
                elif 'python 3.9.0' in j:
                    n1 = None
                    n2 = j.split('python 3.9.0',1)
                    if '.py' not in n2[1]:
                        print(f'''文件名：{num1} 语法错误 第{num2}行
请检查文件扩展名''')
                        break
                    with open(n2[1],'r+',encoding='utf-8') as n3:
                        while n1!='<退出>' and n1!='<查看>':
                            n1 = input('py>')
                            if n1=='<退出>':
                                pass
                            elif n1=='<查看>':
                                n4 = n3.read()
                                print(n4)
                            else:
                                n3.write(n1)
                elif '等待（' in j and '）' in j:
                    n18 = j.replace('等待（','_')
                    n19 = n18.replace('）','_')
                    l10 = n19.split('_')
                    try:
                        int(l10[1])
                    except:
                        print(f'''文件名：{num1} 类型错误 第{num2}行
参数应为数字''')
                        break
                    else:
                        time.sleep(int(l10[1]))
                elif j =='计时——开始（）':
                    num4 = '2'
                    num5 = time.time()
                elif '导入 ' in j and user[3]=='已订阅':
                    n25 = j.split('导入 ')
                    try:
                        n26 = open(n25[1],'r',encoding='utf-8')
                        n26.close()
                    except:
                        print(f'''文件名：{num1} 文件名错误 第{num2}行
未找到指定文件''')
                        break
                    else:
                        nun3 = 模块识别器1.job1(n25[1],d1,d2)
                        d1 = nun3[0]
                        d2 = nun3[1]
                        if nun3[2] == '1':
                            break
                elif '定义 ' in j and user[3]=='已订阅':
                    nun2+=4
                    l21 = j.split('定义 ')
                    d2[l21[1]] = [[],0,[]]
                    nun1 = l21[1]
                elif j in list(d2.keys()):
                    d3 = d1.copy()
                    for i1 in range(d2[j][1]):
                        if '传参 ' not in l1[num2+i1]:
                            print(f'''文件名：{num1} 传参错误 第{num2}行
参数漏写''')
                            num7 = '1'
                            break
                        else:
                            for j1 in list(d1.keys()):
                                if '%%' in j1 and d1[j1]==None and d2[j][2][i1]==j1:
                                    n28 = l1[num2+i1].split('传参 ')
                                    try:
                                        int(n28[1])
                                    except:
                                        if '‘' in n28[1] and '’' in n28[1]:
                                            d1[j1] = n28[1]
                                        elif n28[1] in list(d1.keys()):
                                            d1[j1] = d1[n28[1]]
                                        else:
                                            num8 = '1'
                                            print(f'''文件名：{num1} 名字错误 第{num2}行
{n28[1]}未定义''')
                                            break
                                    else:
                                        d1[j1] = n28[1]
                        if num8=='1':
                            break
                    if num7=='1' or num8=='1':
                        num7 = '0'
                        num8 = '0'
                        break
                    else:
                        l23 = 自定义函数解释器.job3(d2[j],num1,num2,d1)
                        d1 = d3.copy()
                        if l23[2] == '1':
                            break
                elif '传参 ' in j:
                    pass
                elif j=='<主程序>':
                    pass
                elif j=='<主程序/>':
                    pass
                elif '<如果>' in j and user[3]=='已订阅':
                    l29 = j.split('<如果>')
                    if l29[1]=='<真>':
                        pass
                    elif l29[1]=='<假>':
                        x9 = '1'
                    elif l29[1] in list(d1.keys()):
                        if d1[l29[1]]=='<真>':
                            pass
                        elif d1[l29[1]]=='<假>':
                            x9 = '1'
                        else:
                            print(f'''文件名：{num1} 类型错误 第{num2}行
参数应是布尔类型''')
                            break
                    else:
                        print(f'''文件名：{num1} 类型错误 第{num2}行
参数应是布尔类型''')
                        break
                elif j=='<如果/>':
                    pass
                elif '<循环导入>' in j:
                    l30 = j.split(' ')
                    try:
                        MFile = open(l30[1],'r',encoding='utf-8')
                        MFile.close()
                    except:
                        print(f'''文件名：{num1} 文件名错误 第{num2}行
未找到指定文件''')
                        break
                    else:
                        try:
                            int(l30[2])
                        except:
                            if l30[2] in d1:
                                try:
                                    int(d1[l30[2]])
                                except:
                                    print(f'''文件名：{num1} 参数错误 第{num2}行
导入次数必须是整数''')
                                    break
                                else:
                                    Break = False
                                    for _ in range(int(d1[l30[2]])):
                                        l31 = 模块识别器1.job1(l30[1],d1,d2)
                                        d1 = l31[0]
                                        d2 = l31[1]
                                        if l31[2] == '1':
                                            Break = True
                                            break
                                    if Break:
                                        break
                            else:
                                print(f'''文件名：{num1} 参数错误 第{num2}行
导入次数必须是整数''')
                                break
                        else:
                            Break = False
                            for _ in range(int(l30[2])):
                                l32 = 模块识别器1.job1(l30[1], d1, d2)
                                d1 = l32[0]
                                d2 = l32[1]
                                if l32[2] == '1':
                                    Break = True
                                    break
                            if Break:
                                break
                else:
                    print(f'''文件名：{num1} 名字错误 第{num2}行
{j}未定义''')
                    break
            elif x9=='1':
                if '<如果>' in j:
                    x114514+=1
                elif j=='<如果/>':
                    if x114514==0:
                        x9 = '0'
                    else:
                        x114514-=1
            else:
                if '    ' not in j:
                    print(f'''文件名：{num1} 缩进错误 第{num2}行
缩进漏写''')
                    break
                else:
                    if j!='    结束' and '    参数 ' not in j:
                        l22 = j.split('    ')
                        d2[nun1][0].append(l22[1])
                        if '赋值' in j:
                            l114514 = j.split('赋值')
                            if '%%' not in l114514[0]:
                                print(f'''文件名：{num1} 语法错误 第{num2}行
局部变量名需有“%%”''')
                                break
                    elif '   参数 ' in j:
                        n27 = j.split('   参数 ')
                        d1[n27[1]] = None
                        d2[nun1][1]+=1
                        d2[nun1][2].append(n27[1])
                        if '%%' not in n27[1]:
                            print(f'''文件名：{num1} 语法错误 第{num2}行
参数名需有“%%”''')
                            break
                    else:
                        nun1 = None
                        nun2-=4
        t1 = time.time() - t
        print(f'\n\n程序运行结束 用时：{t1}秒')
if adduser!='':
    with open('C:\\解释器\\环境变量\\账户列表.txt','a',encoding='utf-8') as a:
        a.write(adduser)
if addkey!='':
    with open('C:\\解释器\\环境变量\\激活码列表.txt','a',encoding='utf-8') as ak:
        ak.write(addkey[0])
    with open(addkey[1],'w',encoding='utf-8') as path:
        path.write(addkey[0])
if addbuy=='1':
    with open('C:\\解释器\\环境变量\\账户列表.txt','w',encoding='utf-8') as buy:
        for ab2 in userlist:
            buy.write(ab2[0]+' '+ab2[1]+' '+ab2[2]+' '+ab2[3]+' '+'\n')
    with open('C:\\解释器\\环境变量\\激活码列表.txt','w',encoding='utf-8') as keybuy:
        for ab3 in keylist:
            keybuy.write(ab3)
if AddGit!='':
    with open('C:\\解释器\\环境变量\\Git仓库列表.txt','a',encoding='utf-8') as git:
        git.write(AddGit[0]+' '+AddGit[1]+' '+'\n')
    with open('C:\\解释器\\环境变量\\Git仓库储存\\'+AddGit[0]+'.txt','w',encoding='utf-8') as git2:
        pass
if AddTxtToGit!='':
    test = []
    with open(AddTxtToGit[1],'r',encoding='utf-8') as txt:
        tests = txt.readlines()
        for line in tests:
            test.append(line.split('\n')[0]+'%endl%')
    with open('C:\\解释器\\环境变量\\Git仓库储存\\'+AddTxtToGit[0]+'.txt','a',encoding='utf-8') as WriteTxt:
        WriteTxt.write(AddTxtToGit[2]+'%start%')
        for lines in test:
            WriteTxt.write(lines)
        WriteTxt.write('%start% \n')
if RTxt!=[]:
    with open(RTxt[0],'w',encoding='utf-8') as rtxt:
        for RL in RTxt[1]:
            rtxt.write(RL+'\n')