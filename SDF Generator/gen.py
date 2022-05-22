import os, errno
import cv2
import numpy as np

def boundarize(img):
    row, col = img.shape
    bounded_img = np.zeros((row, col))
    for i in range(0, row):
        for j in range(0, col):
            if (i == row - 1):
                if (j != col - 1):
                    if img[i][j] == 0:
                        if img[i][j + 1] > 0:
                            bounded_img[i][j] = 128
                    elif img[i][j + 1] == 0:
                        bounded_img[i][j] = 128
                    else:
                        bounded_img[i][j] = 255
            elif (j == col - 1):
                if img[i][j] == 0:
                    if img[i + 1][j] > 0:
                        bounded_img[i][j] = 128
                elif img[i + 1][j] == 0:
                    bounded_img[i][j] = 128
                else:
                    bounded_img[i][j] = 255
            else:
                if img[i][j] == 0:
                    if img[i][j + 1] > 0 or img[i + 1][j] > 0:
                        bounded_img[i][j] = 128
                elif img[i][j + 1] == 0 or img[i + 1][j] == 0:
                    bounded_img[i][j] = 128
                else:
                    bounded_img[i][j] = 255
    return bounded_img

def matrix_graph(graph, row, col):
    cell_no = 0
    for i in range(0, row):
        for j in range(0, col):
            if (i == row - 1):
                if (j != col - 1):
                    graph[cell_no].append(cell_no + 1)
                    graph[cell_no + 1].append(cell_no)
            elif (j == col - 1):
                graph[cell_no].append(cell_no + col)
                graph[cell_no + col].append(cell_no)
            else:
                graph[cell_no].append(cell_no + 1)
                graph[cell_no + 1].append(cell_no)
                graph[cell_no].append(cell_no + col)
                graph[cell_no + col].append(cell_no)
            cell_no += 1

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
    print("usage: python gen.py {img_dir} {max_dist}")
