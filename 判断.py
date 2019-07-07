import re
import pandas as pd
import numpy as np

# 输入解析文档并将换行符换为*
input_file = "判断.txt"
in_txt = ''
with open(input_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        if '*' in line:
            raise Exception("文档中包含字符*, 无法处理")
        line = line.replace(' ', '')
        line = line.replace('\n','*')
        in_txt += line

# 整体解析标题和答案
title = re.findall('[0-9]{1,3}\.\*(.*?)\*A\.', in_txt)
answer = re.findall('\*\u6b63\u786e\u7b54\u6848\uff1a\s*?([AB])\*', in_txt) #编码部分代表
# 正确答案：
# print(in_txt)
print(len(title))
print(len(answer))

# 输出问题和答案到csv文件
output_list = np.array([title, answer]).T
name=['问题','答案']
output =pd.DataFrame(columns=name, data=output_list)
output.to_csv('判断.csv',encoding='gbk')
print(output)