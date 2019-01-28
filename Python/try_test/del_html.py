import os


class FileOperation(object):
    def del_file(self, path, sign=[]):

        if type(sign) == str:
            sign = [sign]

        for root, dirs, files in os.walk(path):
            for index in files:
                for value in sign:
                    if value in index:
                        os.remove(root + '\\' + index)


if __name__ == "__main__":
    path = "C:\\Users\\ShadowMimosa\\Documents\\STU\\Top\\ForDjango\\joyrun\\background\\reports"
    FileOperation().del_file(path, ['html', 'xml'])
    