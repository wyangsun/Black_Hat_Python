#encoding=utf-8
import re
#统计java报错日志，做到按报错块统计。写的有些渣。。。
log_path = '/Users/apple/'
log_file = 'error.log'
log_dict = {} #定义一个日志统计结果的字典
f = open(log_path + log_file, mode='r')
last_line = '' #保存上一块日志的变量
for newline in f.readlines():
    match_newline = re.match('\[\d{4}\-\d{2}\-\d{2}\ \d{2}\:\d{2}:\d{2}\,\d{3}\](.*)', newline, flags=0)
    if match_newline and last_line not in log_dict and last_line != '':
        log_dict[last_line] = 1
        last_line = match_newline.group(1)
    elif match_newline and log_dict.has_key(last_line) and last_line != '':
        log_dict[last_line] = log_dict[last_line] + 1
        last_line = match_newline.group(1)
    elif match_newline and last_line == '':
        last_line = match_newline.group(1)
    else:
        last_line = last_line + newline
if last_line not in log_dict:
    log_dict[last_line] = 1
elif last_line in log_dict:
    log_dict[last_line] = log_dict[last_line] + 1
f.close()

for i in log_dict:
    print(i)
    print('出现次数：%d'%log_dict[i])
