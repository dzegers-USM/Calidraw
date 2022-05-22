import os, errno
import cv2
import numpy as np

def boundarize(img):
    row, col = img.shape
    bounded_img = np.zeros((row, col))
    for i in range(0, row):
        if (i != row - 1):
            for j in range(0, col):
                if (j != col - 1):
                    if img[i][j] == 0:
                        if (img[i+1][j] > 0 or img[i][j+1] > 0):
                            bounded_img[i][j] = 128
                    else:
                        if (img[i+1][j] == 0 or img[i][j+1] == 0):
                            bounded_img[i][j] = 128
                        else:
                            bounded_img[i][j] = 255
                else:
                    if img[i][j] == 0:
                        if (img[i+1][j] > 0):
                            bounded_img[i][j] = 128
                    else:
                        if (img[i+1][j] == 0):
                            bounded_img[i][j] = 128
                        else:
                            bounded_img[i][j] = 255
        else:
            for j in range(0, col):
                if (j != col - 1):
                    if img[i][j] == 0:
                        if (img[i][j+1] > 0):
                            bounded_img[i][j] = 128
                    else:
                        if (img[i][j+1] == 0):
                            bounded_img[i][j] = 128
                        else:
                            bounded_img[i][j] = 255
                else:
                    if img[i][j] != 0:
                        bounded_img[i][j] = 255
    return bounded_img

if (len(os.sys.argv) == 3):
    img_dir = os.sys.argv[1]
    max_dist = os.sys.argv[2]
    try:
        os.mkdir("out")
    except OSError as err:
        if err.errno != errno.EEXIST:
            raise

    for img_name in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path, 0)  # np array
        bounded_img = boundarize(img)
        fname = "out/" + os.path.splitext(img_name)[0] + '.jpg'
        cv2.imwrite(fname, bounded_img)
        
else:
    print("usage: python gen.py {img_dir}")
