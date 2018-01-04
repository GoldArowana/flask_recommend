|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
开发进度：

进行目录结构设计，https://github.com/GoldArowana/flask_mvc_demo
    设计成平时写Java项目的mvc的样子做的
    template文件夹下的jinja2模板不智能提示，整出来后自己写了个博客。http://www.cnblogs.com/noKing/p/8117461.html
    static文件夹下的资源不自动提示，不识别。可以搞出来。但是弄出来后jinja模板又不能自动提示了。二者只能选其一。还没有别的解决办法


数据库设计
    python模块不熟，调不出model
    表结构很纠结，想了一下午。
    日期函数不熟，卡住了。https://docs.python.org/2/library/datetime.html
    设置mysql后端的日期字段默认值，卡住了。http://docs.sqlalchemy.org/en/latest/core/defaults.html
    字符串+数字，总忘了str()来转换。
    随机数函数randint(x,y)是左闭右闭区间，整错了。
    python的None对应mysql端的null。

插入测试数据，基本每个表都有了数据。方便开发的时候进行查看

完善sqlalchemy的表和表之间的关系。
    参考博客：http://blog.csdn.net/Jmilk/article/details/52445093#one-to-many

首页页面模板修改

登陆登出功能，简易版，简单session

Topic页功能

Topic发布功能--一半

首页-用数量，ajax。加载错误后可以支持手动刷出来。

首页最新10条news，ajax。

vip页面样式

settings页面样式

加入404小游戏 https://github.com/litong9406/flappy_bird

注册页面完成。ajax检查，邮箱正则匹配检查。

防止回车键自动提交表单

定时器，倒计时120秒，发送验证码

另开一个线程，保持后台验证码数据是最新120秒内的。未设置为阻塞式。

bug:::Email类向数据库插入数据时，插不进去数据。原因：init函数里忘了写‘self.’

注册功能完成。（缺少后台验证，只有前端验证）

禁用了回车submit。原因：发布内推信息页按回车就自动提交。

发布内推信息的功能，已成功。缺少验证，和添加公司等功能。

bug:::首页的最新10条数据，按时间排序的逻辑错乱，已改正。

添加logging模块.记录系统日志。