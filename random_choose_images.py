import os
import glob
import shutil
import numpy as np


def run(path):
    imgs = glob.glob("{}/*/*.jpg".format(path))
    a = np.array(imgs)
    a = np.random.choice(a, (2000, 1), replace=False)
    for idx, i in enumerate(a):
        print(i[0])
        shutil.copyfile(i[0], 'images/{}.jpg'.format(idx+1))



if __name__ == "__main__":
    run("F:\lfw-deepfunneled_with_mask_each4")