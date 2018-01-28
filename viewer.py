from os.path import join

from mayavi import mlab


input_file = join('/home/phil/Data', 'pcd_examples.pcd')

with open(input_file, 'r') as f:
    data = f.read()

data1 = data.split('\n')
data = data1[11:]  # skip the header

x = []
y = []
z = []

for i in data[:-1]:
    temp = i.split(' ')
    x.append(float(temp[0]))
    y.append(float(temp[1]))
    z.append(float(temp[2]))


mlab.points3d(x, y, z, mode='point')  # 'points' render mode significantly faster than 'spheres'
mlab.show()
