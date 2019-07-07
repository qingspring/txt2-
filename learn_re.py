import re
in_txt = '1.这是标*题一**A.12.这是标*题二**A.207.这是标*题二A.**'
title = re.findall('([0-9]*?\..*?)A\.', in_txt) # *是贪婪的，总是找出最长的匹配，*？可以找出最短的匹配
print(title)

title_split = re.split('\*\*', in_txt)
print(title_split)