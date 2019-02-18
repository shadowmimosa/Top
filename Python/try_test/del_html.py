import os


class FileOperation(object):
    """Addition, deletion, revision and query of files"""

    def add_file(self, path, f_name="default.txt", encoding='uf-8'):
        """Create new file"""

        f_path = os.path.join(path, f_name)

        if not os.path.exists(f_path):
            with open(f_path, 'w', encoding):
                pass
        else:
            raise 'File is already existed!'

    def del_file(self, path, f_name=[], sign=None):

        if type(f_name) == str:
            f_name = [f_name]

        for root, dirs, files in os.walk(path):
            for index in files:
                for value in f_name:
                    f_path = os.path.join(root, index)
                    if sign:
                        if index == value:
                            os.remove(f_path)
                    else:
                        if value in index:
                            os.remove(f_path)

    def del_folder(self, path, folder=[]):

        if type(folder) == str:
            folder = [folder]
        elif len(folder) == 0:
            os.remove(path)
            return

        for root, dirs, files in os.walk(path):
            for index in dirs:
                for value in folder:
                    if index == value:
                        os.remove(os.path.join(root, dirs))


if __name__ == "__main__":
    path = "C:\\Users\\ShadowMimosa\\Documents\\STU\\Top\\ForDjango\\joyrun\\background\\reports"
    FileOperation().del_file(path, ['html', 'xml'])
    FileOperation().del_file(path, ['html', 'xml'], sign=True)

    list_a="["five","ten","half"]"
