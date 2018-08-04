#计算两个原子之间的距离
import numpy as np
box=np.zeros((3,2))
with open("20180804.txt") as f:
    for line in f:
        s=line.split()
        if "atoms" in line:
            crd=np.zeros((int(s[0]),3))
        for index,keyword in enumerate([("xlo","xhi"),("ylo","yhi"),("zlo","zhi")]):
            if keyword[0] in line and keyword[1] in line:
                box[index]=[float(s[i]) for i in range(2)]
        if len(s)==8:
            crd[int(s[0])-1]=[float(s[i]) for i in range(3,6)]
boxsize=np.abs(box[:,0]-box[:,1])
atom1,atom2=(int(x)-1 for x in input("input atom id: ").split())
dxyz=crd[atom1]-crd[atom2]
dxyz-=np.round(dxyz/boxsize)*boxsize
print("distance:%.6f"%np.linalg.norm(dxyz))
