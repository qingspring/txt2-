import re
import pandas as pd
import numpy as np

# 输入解析文档并将换行符换为*
input_file = "多选.txt"
in_txt = ''
with open(input_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        if '*' in line:
            raise Exception("文档中包含字符*, 无法处理")
        line = line.replace(' ', '')
        line = line.replace('\n','*')
        in_txt += line

# 分割文档
txt_split = re.split('\*\*', in_txt)
# print(in_txt)
# print(txt_split)
print(len(txt_split))

title, answer = [], []
option_A, option_B, option_C, option_D, option_E, option_F, option_G = [], [], [], [], \
                                                                      [], [], []
# 解析分割后文档的标题和答案
for txt in txt_split:
    title.append(''.join(re.findall('[0-9]{1,3}\.\*(.*?)\*A\.', txt)))
    answer.append(''.join(re.findall('\*\u6b63\u786e\u7b54\u6848\uff1a\s*?([A-G]*)',
                                     txt)))
    option_A.append(''.join(re.findall('\*A\.(.*?)\*B\.', txt)))
    option_B.append(''.join(re.findall('\*B\.(.*?)\*C\.', txt)))
    option_C.append(''.join(re.findall('\*C\.(.*?)\*', txt)))
    option_D.append(''.join(re.findall('\*D\.(.*?)\*', txt)))
    option_E.append(''.join(re.findall('\*E\.(.*?)\*', txt)))
    option_F.append(''.join(re.findall('\*F\.(.*?)\*', txt)))
    option_G.append(''.join(re.findall('\*G\.(.*?)\*', txt)))
# 打印长度
print(len(title),len(answer),len(option_A),len(option_B),len(option_C),len(option_D),
      len(option_E),len(option_F),len(option_G))

# 输出问题和答案到csv文件
output_list = np.array([title, option_A, option_B, option_C, option_D,
option_E, option_F, option_G, answer]).T
name=['问题','A','B','C','D','E','F','G','答案']
output =pd.DataFrame(columns=name, data=output_list)
output.to_csv('多选.csv',encoding='gbk')

## print语句：
# print(in_txt)
# print(title)
# print(answer)
# print(option_A)
# print(option_B)
# print(option_C)
# print(option_D)
# print(option_E)
# print(option_F)
# print(option_G)
# print(output)