# 计算机网络课程设计
## 任务
  1.曹月华：监听请求，建立连接   
  2.宋静澜：线程管理（线程池）  
  3.曹哲瑀：HTTP报文解析  
  4.郭，叶：CGI（处理GET，POST请求，实现+，学号查询）  
  5.李 帆：出错处理，页面设计（404界面等）  
  6.贺雪莹：日志  
## 一些参考
  1.[小白视角：一文读懂社长的TinyWebServer](https://huixxi.github.io/2020/06/02/%E5%B0%8F%E7%99%BD%E8%A7%86%E8%A7%92%EF%BC%9A%E4%B8%80%E6%96%87%E8%AF%BB%E6%87%82%E7%A4%BE%E9%95%BF%E7%9A%84TinyWebServer/#more)  
  2.[Tomcat处理HTTP请求流程解析](https://juejin.cn/post/7067917428319223845)  
  3.[使用Python开发你的第一个服务器程序](https://cloud.tencent.com/developer/article/1356570)  
  4.[python实现http服务器](https://blog.csdn.net/qq_32426313/article/details/104180402)  
  5.[基于python的简单HTTP服务器实现](https://blog.csdn.net/hu694028833/article/details/80862695)  
  6.[压力测试](https://cloud.tencent.com/developer/article/1684842)  
## 接口设计
各个模块功能流程以及其间的接口说明

连接模块：

工具：pycharm社区版2022

描述：用Django模板创建的文件，html页面在templates文件夹下，app1文件夹下的views文件里写了调用html页面的函数，url.py里有调用的路径

页面设计模块：

工具：VScode

描述：error.html是出错页面，style.css是对应的美化设计；query.html是查询界面，qs.css是对应的美化设计

日志模块：

工具：pycharm社区版2022

描述：LogM类的属性包括ip地址，URL，HTTP状态码，点击后获得的超链接，用户终端浏览器；可通过实例化类传入要写入日志的一条请求的信息


监听+线程管理 MyServer.py ：

工具：pycharm社区版2021

描述：创建了一个大小为20的线程池进行管理，接收到的信息传入http_content函数，经过报文解析(未在此文件中编写)，将回送给浏览器的数据作为返回值，返回到process_conn模块。