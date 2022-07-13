# coding: utf-8
# author: zpta

with open('note.txt', 'r') as f:
    rpm_list = f.readlines()

with open('rpm.txt', 'w') as f:
    rpm_list.sort()
    for i in rpm_list:
        # f.writelines(list(i))
        f.writelines(i)
