# hygx huiyuan competition
## “慧源共享”上海高校开放数据创新研究大赛
environment:  python 3.6.8   Neo4j 3.5.7   WIN10
首先将数据解压到当前目录(和代码文件在一个目录)，解压后的目录如下:

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/1.PNG)

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/2.PNG)

#### 运行excel2csv.py

代码将原始的xlsx文件转换成csv文件(后续处理速度会快)，代码将生成 读者入馆数据集 和 图书外借数据集 两个文件夹，并将相应文件存入。

读者入馆数据集目录:

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/3.PNG)

将 to_neo4j.py 拖入 图书外借数据集 文件夹，目录:

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/4.PNG)

#### 运行to_neo4j.py(在 图书外借数据集 目录下)

代码会处理该目录下csv文件，使其格式匹配图数据库Neo4j的接口(这次我们共导入复旦，同济，财大，海洋，上电五所学校，可以修改代码决定导入哪几所高校)。最后会在该目录下生成文件夹 to_neo4j。 目录:

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/9.PNG)

#### 运行import.bat(命令行切换到当前目录运行)

将数据导入图数据库Neo4j(必须是全新的数据库，可以在Neo4j安装目录下neo4j.conf这个文件中修改激活的数据库)。打开Neo4j可以看到导入了五所高校的963,967个学生(节点)，5,470,860条借阅记录(边)。

输入:

MATCH (n:Student{Student:'33c01cb5888b58e8124f9d9e964ba67f'}),(m:Student{Student:'9e5d2f2e'}),

p=allshortestpaths((n)-[*..5]-(m)) 

return p limit 10

返回结果如下:

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/10.PNG)

#### 运行extract.py

代码会抽取出对比数据(具体的对比内容见生成文件及代码注释)，存储于生成的 数据分析 文件夹， 目录:

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/5.PNG)

到馆数据 文件夹目录:

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/6.PNG)

外借数据 文件夹目录:

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/7.PNG)

![image](https://github.com/Tianchen627/hygx-huiyuan-competition/blob/master/screenshots/8.PNG)

