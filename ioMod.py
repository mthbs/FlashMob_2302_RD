import os


def fopen(fpath, mode):
    try:
        file = open(fpath, mode)
    except:
        file = 0
        path, filename = os.path.split(fpath)
        if not os.path.exists(path):
            os.makedirs(path)
    return file

if __name__ == '__main__':
    fpath = "./data/bookDB/booklist.txt"
    try:
        file = open(fpath,"r")
    except:
        file = 0
        path, filename = os.path.split(fpath)
        if not os.path.exists(path):
            os.makedirs(path)



    print(path, filename, sep=" <> ")