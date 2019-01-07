import os
import json

path = 'D:\\test\\JoyrunTestOA\\thejoyrunTestcode'

os.listdir(path)
L = []
D = {}
Json_D = {}


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] == '.jpeg':
            list_name.append(file_path)


def file_name(file_dir, D):
    for root, dirs, files in os.walk(file_dir):
        print(root)  #当前目录路径
        print(dirs)  #当前路径下所有子目录
        print(files)  #当前路径下所有非目录子文件

        D[root] = files


def get_dirfilename_all(path):
    if '/' in path:
        path.replace('/', '\\')

    foldername = path.split('\\')[-1]

    Json_D[foldername] = {}

    for root, dirs, files in os.walk(path):

        root_folder = root.split('\\')[-1]

        if root == path:
            for index in dirs:
                if 'git' not in index:
                    Json_D[foldername][index] = {}

        elif len(root) > len(path):
            if root_folder in Json_D[foldername].keys():
                Json_D[foldername][root_folder] = files
                # write_file(".//robottxt.txt", Json_D)

    return (Json_D)


def write_file(path, data):
    with open(path, 'w', encoding='utf-8') as write_f:
        write_f.write(json.dumps(data))


def initial_testcase(path):
    initial_tests = get_dirfilename_all(path)


# walk=os.walk(path)
# print(walk)

# listdir(path, L)
# file_name(path,D)
count = 0

with open("Python\\try_test\\robottxt.json", 'r', encoding='utf-8') as write_f:
    f = write_f.readlines()
f = eval(f[0])
for keys, values in f['thejoyrunTestcode'].items():
    before_count = count
    for index in values:
        if 'init' not in index and 'git' not in index:
            count += 1
        else:
            pass
            # print("The exclude element is %s" % index)
    print("The %s Class has %s" % (keys, count - before_count))
    before_count = count
