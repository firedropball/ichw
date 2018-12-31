#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Ge Feng"
__pkuid__  = "1800011827"
__email__  = "1800011827@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import urllib.error
import string

def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    for i in string.punctuation:
        lines.replace(i,' ')
    #除去标点
    for i in string.whitespace:
        lines.replace(i,' ')
    #除去其他符号
    lines=lines.lower()#转小写
    lines=lines.split()#分开字符
    i=1
    while(i<len(lines)-1):
        if lines[i]=='' or lines[i]==' ':
            lines[i].pop()
        i+=1
    #除去空格及无字符
    dic={}
    for x in lines:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    #统计个数
    dic=sorted(dic.items(),key=lambda x:x[1],reverse = True)
    #排序
    i=1
    for x in dic:
        print(x[0],''.join([' ' for i in range(20-len(x[0]))]),x[1])
        i+=1
        if i>topn:
            break
    #输出所需输出的
    pass

if __name__ == '__main__':
    top_num = 10
    if  len(sys.argv) == 1 or len(sys.argv) > 3:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    elif len(sys.argv) == 3:
        try:#判断输入数字是否合法
            top_num = int(sys.argv[2])
        except:
            print("please write a number here")
            sys.exit(1)
    try:#尝试请求打开网页
        doc = urlopen(sys.argv[1])
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode('UTF-8')
    except urllib.error.URLError:
        print(sys.exc_info()[1])
        sys.exit(1)
    except urllib.error.HTTPError:
        print(sys.exc_info()[1])
        sys.exit(1)
    except ValueError:
        print(sys.exc_info()[1])
        sys.exit(1)
    #对每种错误输出其错误并退出
    else:
        wcount(jstr,top_num)
    
