# 说明

### quick_insert.py

使用程序方式批量插入数据的脚本，需要引入依赖包 pymysql

### quick_insert_threads.py

使用 5 个线程批量插入数据的脚本，需要引入依赖包 pymysql

### quick_sql_insert.py

生成 insert 批量插入脚本，与上面的方式类似，只不过生成的文件需要手动执行。

### quick_txt_load.py

生成逗号分隔的 txt 文件，之后需要使用 `load data infile` 命令导入数据。



**扫码关注，更多干货。**

![](https://camo.githubusercontent.com/66deba38c0755e91df34abe83b1e3cdcb466d6f7/68747470733a2f2f747661312e73696e61696d672e636e2f6c617267652f30303753385a496c6c7931676664366778353468616a3331347a306e706166702e6a7067)