import numpy as np

image_landmarklist = [[159, 237], [201, 227], [241, 203], [269, 178], [291, 159], [219, 155], [243, 121], [256, 100], [265, 80], [199, 148], [214, 110], [222, 85], [228, 65], [177, 147], [185, 111], [191, 88], [196, 69], [152, 152], [147, 123], [144, 103], [141, 84]]
def calculate_distance(landmark1, landmark2):
    return np.sqrt((landmark1[0] - landmark2[0])**2 + (landmark1[1] - landmark2[1])**2)

distances = []
j = 1
while j < 21:
    demodi = []
    demodi.append(image_landmarklist[0])
    for i in range(j,j+4):
        demodi.append(image_landmarklist[i])
    for k in range(4):
        distance = calculate_distance(demodi[k],demodi[k+1])
        distances.append(distance)
    j = j+4

print(distances)