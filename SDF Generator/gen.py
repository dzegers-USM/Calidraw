import os, errno
import cv2
import numpy as np
from collections import deque 

def preSDF(img):
    row, col = img.shape
    cell_no = 0
    graph = [[] for i in range(row*col)]
    dist = np.full(row*col, 10**7)
    visited = np.zeros(row*col)
    queue = deque()
    for i in range(0, row):
        for j in range(0, col):
            cell_no = col*i + j
            if (i == row - 1):
                if (j != col - 1):
                    if img[i][j] == 0:
                        if img[i][j + 1] > 0:
                            dist[cell_no] = 0
                            visited[cell_no] = True
                            queue.append(cell_no)
                    elif img[i][j + 1] == 0:
                        dist[cell_no] = 0
                        visited[cell_no] = True
                        queue.append(cell_no)
                    graph[cell_no].append(cell_no + 1)
                    graph[cell_no + 1].append(cell_no)
            elif (j == col - 1):
                if img[i][j] == 0:
                    if img[i + 1][j] > 0:
                        dist[cell_no] = 0
                        visited[cell_no] = True
                        queue.append(cell_no)
                elif img[i + 1][j] == 0:
                    dist[cell_no] = 0
                    visited[cell_no] = True
                    queue.append(cell_no)
                graph[cell_no].append(cell_no + col)
                graph[cell_no + col].append(cell_no)
            else:
                if img[i][j] == 0:
                    if img[i][j + 1] > 0 or img[i + 1][j] > 0:
                        dist[cell_no] = 0
                        visited[cell_no] = True
                        queue.append(cell_no)
                elif img[i][j + 1] == 0 or img[i + 1][j] == 0:
                    dist[cell_no] = 0
                    visited[cell_no] = True
                    queue.append(cell_no)
                graph[cell_no].append(cell_no + 1)
                graph[cell_no + 1].append(cell_no)
                graph[cell_no].append(cell_no + col)
                graph[cell_no + col].append(cell_no)
            cell_no += 1
    return graph, dist, visited, queue

def BFS(visited, dist, graph, queue):
    while len(queue) > 0:
        temp = queue.popleft()
        for i in graph[temp]:
            if (visited[i] != True):
                dist[i] = min(dist[i], dist[temp] + 1)
                queue.append(i)
                visited[i] = True
    return dist

def recenterSDF(img, dist_matrix, max_dist):
    row, col = img.shape
    dist_matrix = np.reshape(dist_matrix, (row, col))
    img_sdf = np.full((row, col), -1)
    for i in range(0, row):
        for j in range(0, col):
            dist = min(dist_matrix[i][j], max_dist)
            color_diff = dist * 128/max_dist
            color_diff *= 1 if (img[i][j] != 0) else -1
            new_color = min(128 + color_diff, 255)
            img_sdf[i][j] = new_color
    return img_sdf

def SDF(img, max_dist):
    graph, dist, visited, queue = preSDF(img)
    dist = BFS(visited, dist, graph, queue)
    return recenterSDF(img, dist, max_dist)

if (len(os.sys.argv) == 3):
    img_dir = os.sys.argv[1]
    max_dist = os.sys.argv[2]
    try:
        max_dist = int(max_dist)
    except ValueError:
        print("max_dist \"", max_dist, "\" cannot be cast as int.")
        os._exit()

    try:
        os.mkdir("out")
    except OSError as e:
        if e.errno != errno.EEXIST:
            print(os.strerror(e.errno))
            os._exit()

    for img_name in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path, 0)  # np array
        if (img.size == 0):
            print("Failed to read ", img_name)
        else:
            sdf_img = SDF(img, max_dist)
            out_path = os.path.join("./out/", img_name)
            cv2.imwrite(out_path, sdf_img)
            print("Exported \"" + img_name + "\"")
   
else:
    print("Usage: python gen.py {img_dir} {max_dist}")
