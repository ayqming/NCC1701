'''
Created on 2018��1��18��

@author: ayqming
'''
def listprint(the_list):
    #����һ���������б�
    for em_list in the_list:
        if isinstance(em_list, list):
            listprint(em_list)
        else:
            print(em_list)