import glob
from struct import unpack
from os import path, rename, remove, mkdir, getcwd


def read_bin(filepath):
    features = list()
    binfile = open(filepath, 'rb')
    size = path.getsize(filepath)

    for _ in range(size//4):
        data = binfile.read(4)
        num = unpack('f', data)
        features.append(num[0])
    binfile.close()

    return features


for i in glob.glob(r"log/*"):
    print("{:50s} {}".format(i, read_bin(i)))