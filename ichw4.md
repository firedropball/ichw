1.解释概念与意义  
 ======  
 ### 概念
     - 作业：用户向电脑提交，希望电脑执行的任务（程序）（一般从用户角度来看的）  
     - 进程：电脑对任务的执行（一般从电脑角度来看）  
     - 线程：电脑在执行进程时因为各种原因将进程分解的最小单位
 ### 解决问题
     - 进程：解决了cpu同一时间只能处理一个问题，但是往往多个问题需要同时解决的问题  
     - 线程：
       1. 解决了多核解决一个问题时只能由一个去解决的问题  
       2. 可以将同一进程内不同快慢（I/O处理、人机交互与密集计算）分开处理，提高了运算效率  
2.虚拟储存器
 =======   
 ### 概念  
      >虚拟内存是计算机系统内存管理的一种技术。它使得应用程序认为它拥有连续可用的内存（一个连续完整的地址空间），  
      而实际上，它通常是被分隔成多个物理内存碎片，还有部分暂时存储在外部磁盘存储器上，在需要时进行数据交换。
      
      引用自维基百科
 ### 工作原理  
  运行进程时，计算机自动将一部分进程的数据置于内存，一部分置于缓存中，并认为主存中的数据即为虚拟内存。  
  当运算时发现内存不足（程序大小过大）时，只将一部分程序（数据）置于内存中  
  如果进程运算时发现需要未调用入内存的程序（数据）时，则将其调入内存再运算  
  如果内存不足，则按一定算法调出内存内的一部分，装入新的  
  ### 作用  
  大大扩展了电脑能执行的程序的大小，使得电脑能在较小内存下运行较大程序
