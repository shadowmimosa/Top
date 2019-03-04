def read_file(path):
    """打开文件，按行读取；返回所有行

    ``path`` 文件路径  
    ``type(return) = list``
    """
    with open(path, 'r', encoding='utf-8') as fn:
        lists = fn.readlines()
    return lists

if __name__ == "__main__":
    path="C:\\Users\\ShadowMimosa\\Documents\\GitRepository\\PYthon_Public\\joyrun\\background\\thejoyrunTestcode\\betapi\\class_detail_info_Get.txt"
    
    read_file(path)