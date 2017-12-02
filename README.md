
一个数据处理工具基于python2.7

主要功能是：
	读取文件按照给出的行作为key
	每个key中取出N行

使用python sample.py -h 获取帮助信息

Command:
              python tool.py [-k num,num -t delimiter -n quantity | -h ] file
              Options and arguments:
                 -h              :  help
                 -k num,num      :  sort by row number (default 1)
                 -t delimiter    :  delimiter (default table)
                 -n quantity     :  extract Specific quantity from every key's value(default 1)
              Output: ./output
