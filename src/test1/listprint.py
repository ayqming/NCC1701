'''
Created on 2018年1月18日

@author: ayqming
'''
def listprint(the_list):
    #含有一个参数是列表
    for em_list in the_list:
        if isinstance(em_list, list):
            listprint(em_list)
        else:
            print(em_list)