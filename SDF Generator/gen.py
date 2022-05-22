import os, errno
import cv2
import numpy as np
from collections import deque 

def preSDF(img):
    row, col = img.shape
    cell_no = 0
    # bounded_img = np.zeros((row, col))
    graph = [[]]*row*col
    dist = np.full((row, col), 10**7)
    visited = np.zeros((row, col))
    queue = deque()
    for i in range(0, row):
        for j in range(0, col):
            if (i == row - 1):
                if (j != col - 1):
                    if img[i][j] == 0:
                        if img[i][j + 1] > 0:
                            # bounded_img[i][j] = 128
                            dist[i][j] = 0
                            visited[i][j] = True
                            queue.append(cell_no)
                    elif img[i][j + 1] == 0:
                        #bounded_img[i][j] = 128
                        dist[i][j] = 0
                        visited[i][j] = True
                        queue.append(cell_no)
                    # else:
                        # bounded_img[i][j] = 255
                    graph[cell_no].append(cell_no + 1)
                    graph[cell_no + 1].append(cell_no)
            elif (j == col - 1):
                if img[i][j] == 0:
                    if img[i + 1][j] > 0:
                        # bounded_img[i][j] = 128
                        dist[i][j] = 0
                        visited[i][j] = True
                        queue.append(cell_no)
                elif img[i + 1][j] == 0:
                    # bounded_img[i][j] = 128
                    dist[i][j] = 0
                    visited[i][j] = True
                    queue.append(cell_no)
                # else:
                    # bounded_img[i][j] = 255
                graph[cell_no].append(cell_no + col)
                graph[cell_no + col].append(cell_no)
            else:
                if img[i][j] == 0:
                    if img[i][j + 1] > 0 or img[i + 1][j] > 0:
                        # bounded_img[i][j] = 128
                        dist[i][j] = 0
                        visited[i][j] = True
                        queue.append(cell_no)
                elif img[i][j + 1] == 0 or img[i + 1][j] == 0:
                    # bounded_img[i][j] = 128
                    dist[i][j] = 0
                    visited[i][j] = True
                    queue.append(cell_no)
                # else:
                    # bounded_img[i][j] = 255
                graph[cell_no].append(cell_no + 1)
                graph[cell_no + 1].append(cell_no)
                graph[cell_no].append(cell_no + col)
                graph[cell_no + col].append(cell_no)
            cell_no += 1
    return graph, dist, visited, queue

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
        graph, dist, visited, queue = preSDF(img)
        
else:
    print("usage: python gen.py {img_dir} {max_dist}")
