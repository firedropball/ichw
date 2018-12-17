'''本程序用来解决在特定长宽砖上铺特定长宽砖种类，
并可通过turtle程序来画出来选中的种类。

__author__      = "Ge Feng"
__student ID__  = "180001827"
__institution__ = "Peking University"
'''
import turtle as t
sum=0
#使用全局变量以缓解栈溢出问题

solution1=[]
solution2=[]
solution3=[]
#这个时目前的解决方案

so1=[]
so2=[]
so3=[]
#这个时总的解决方案

map1 = [[0 for i in range(20)] for j in range(20)]
#这个是目前的墙面
def write(a,b,c,d,y):
    '''画一个(a,c)到(b,d)的矩形
    '''
    y.goto(a*30,b*30)
    y.pendown()
    y.goto(a*30,d*30)
    y.goto(c*30,d*30)
    y.goto(c*30,b*30)
    y.goto(a*30,b*30)
    y.penup()
    
def output(n,m,a0,a1):
    '''画图函数
    '''
    a=int(t.numinput('输入',"括号内为起始点、终止点坐标,请输入你的选择"))
    y=t.Turtle()
    y.speed(0)
    y.hideturtle()
    y.penup()
    y.goto(-40,0)
    y.write('纵坐标')
    y.goto(-30,-20)
    y.write('横坐标')
    for i in range(n+1):
        y.goto(i*30+15,-20)
        y.write(i+1,False,align='center',font=("Arial",10, "normal"))
    for i in range(m+1):
        y.goto(-20,i*30+15)
        y.write(i+1,False,align='center',font=("Arial",10, "normal"))
    #画坐标
    for i in range(n+1):
        for j in range(m+1):
            write(i,j,i+1,j+1,y)
    #画背景方块
    y.pensize(5)
    y.color('blue')
    for i in range(len(so1[a-1])):
        if (so3[a-1][i] == 1):#如果是横着的方块，则横着画
            write(so1[a-1][i],so2[a-1][i],so1[a-1][i]+a0,so2[a-1][i]+a1,y)
        else:#竖着的方块就竖着画
            write(so1[a-1][i],so2[a-1][i],so1[a-1][i]+a1,so2[a-1][i]+a0,y)
    #time.sleep(5)
    t.done()
    
def find0(n,m,a0,a1,ii,jj,dep):
    '''在(ii,jj)这个坐标上尝试铺第dep块砖
    '''
    global sum
    posibility=False#判断是否能铺
    #横着摆
    if(ii+a0<=n+1 and jj+a1<=m+1):#是否越界
        if (1 not in [map1[i][j] for i in range(ii,ii+a0) for j in range(jj,jj+a1)]):#如果要横着铺，能否铺（砖上有无以前的砖）
            for i in range(ii,ii+a0):
                for j in range(jj,jj+a1):
                    map1[i][j] = 1
            #把砖铺上
            solution1.append(ii)
            solution2.append(jj)
            solution3.append(1)
            #写上目前铺的方案
            if (0 not in [map1[i][j] for i in range(n+1) for j in range(m+1)]):
                #如果铺满了，则记录结果并输出
                sum+=1
                so1.append(tuple(solution1))
                so2.append(tuple(solution2))
                so3.append(tuple(solution3))
                #记录
                print('第',sum,'种')
                for i in range(0,dep+1):
                    print('(',solution1[i]+1,',',solution2[i]+1,'),(',solution1[i]+1+a0,',',solution1[i]+1+a1,')')
                #输出
            if_find=False
            for i in range(n+1):
                for j in range(m+1):
                    if (map1[i][j] == 0 and not if_find):
                       if(find0(n,m,a0,a1,i,j,dep+1)):
                            if_find=True
            #找到下一个能铺的地方，if_find保证只招一个，避免出现死循环
            for i in range(ii,ii+a0):
                for j in range(jj,jj+a1):
                    map1[i][j] = 0
            solution1.pop()
            solution2.pop()
            solution3.pop()
            #把地图与目前的方案恢复原状
            posibility=True
    #竖着铺，a1!=a0保证正方形时不会输出长宽相同的结果，其他和横着铺一样，故不作注释
    if(ii+a1<=n+1 and jj+a0<=m+1 and a1!=a0):
        if (1 not in [map1[i][j] for i in range(ii,ii+a1) for j in range(jj,jj+a0)]):
            for i in range(ii,ii+a1):
                for j in range(jj,jj+a0):
                    map1[i][j] = 1
            solution1.append(ii)
            solution2.append(jj)
            solution3.append(2)
            if (0 not in [map1[i][j] for i in range(n+1) for j in range(m+1)]):
                sum+=1
                so1.append(tuple(solution1))
                so2.append(tuple(solution2))
                so3.append(tuple(solution3))
                print('第',sum,'种')
                for i in range(0,dep+1):
                    print('(',solution1[i]+1,',',solution2[i]+1,'),(',solution1[i]+1+a1,',',solution1[i]+1+a0,')')
            if_find=False
            for i in range(n+1):
                for j in range(m+1):
                    if (map1[i][j] == 0 and not if_find):
                       if(find0(n,m,a0,a1,i,j,dep+1)):
                            if_find=True
            for i in range(ii,ii+a1):
                for j in range(jj,jj+a0):
                    map1[i][j] = 0
            solution1.pop()
            solution2.pop()
            solution3.pop()
            posibility=True
    return posibility

def main():
    n = int(input('请输入行数'))
    m = int(input('请输入列数'))
    a0 = int(input('请输入长度'))
    a1 = int(input('请输入宽度'))
    n-=1
    m-=1
    find0(n,m,a0,a1,0,0,0)
    output(n,m,a0,a1)
    
if __name__ == '__main__':
    main()

