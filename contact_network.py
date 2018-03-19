# This code is fro animating the sphere motion
# written by Sidhant Pednekar
# Levich Institute City College of New York

from visual import *

# reading the input files


f = open('./T.txt')   #Reading particle position file
g = open('./C.txt')   #Reading particle contact matrix file

cy = 300  	#Snapshot cycle number
np = 500  	#Number of particles
rp1 = 1.4 	#Radius of particle 1
rp2 = 1   	#Radius of particle 2
xm = 18.318     #x dimension of domain
ym = 18.318	#y dimension of domain
zm = 18.318     #z dimension of domain

scene = display(title='Simple Shear',
     width=1000, height=1000,
     center=(15,15,0), background=(1,1,1), fullscreen = False)


#box = wallR = box(pos=(10,10,10), size=(40.0,40.0,40.0), color=color.blue, opacity = 0.1)


# read initial x

#i = (cy - 1)*np
cy_min = cy - 1
cy_max  = cy + 1
i = 0
j = 1
nn = 0
counter = 0
particles = {}
network = {}

#pointer1 = arrow(pos=(0,0,0), axis=(xm,0,0), shaftwidth=0.8, color=color.red, material = materials.earth)
#pointer2 = arrow(pos=(0,0,0), axis=(0,ym,0), shaftwidth=0.8, color=color.red, material = materials.earth)
#pointer3 = arrow(pos=(0,0,0), axis=(0,0,zm), shaftwidth=0.8, color=color.red, material = materials.earth)

#local_light(pos=(20,20,20), color=color.green)


for line in f:
    cr = line.split()
    if float(cr[0]) >= np + (cy-1)*np and float(cr[0]) < np + cy*np:
        i = float(cr[0])%np
        if float(cr[1]) == 0.0:
          particles[i] = sphere(pos=(float(cr[2]),float(cr[4]),float(cr[3])), radius=rp1, color=color.blue, material=materials.wood, opacity=0.1)
        if float(cr[1]) == 1.0:
          particles[i] = sphere(pos=(float(cr[2]),float(cr[4]),float(cr[3])), radius=rp2, color=color.blue, material=materials.rough, opacity=0.1)
    if float(cr[0]) > (cy+1)*np:
      break
   # i = i + 1

        
for line in g:
    cr1 = line.split()
 #   rate(500)
    #if float(cr1[0]) > 10.0 and float(cr1[0]) < 12.0:
    if float(cr1[0]) > cy_min and float(cr1[0]) < cy_max:
        if (abs(particles[int(cr1[1])].pos.x - particles[int(cr1[2])].pos.x) < xm/2.0) and (abs(particles[int(cr1[1])].pos.y - particles[int(cr1[2])].pos.y) < ym/2.0) and (abs(particles[int(cr1[1])].pos.z - particles[int(cr1[2])].pos.z) < zm/2.0):
            if float(cr1[3]) == 1:
                        network= curve(pos=[(particles[int(cr1[1])].pos),(particles[int(cr1[2])].pos)], radius=0.1, color = color.white)
            if float(cr1[3]) > 1:
                        network= curve(pos=[(particles[int(cr1[1])].pos),(particles[int(cr1[2])].pos)], radius=0.1, color = color.red)
                        #network= curve(pos=[(particles[int(cr1[1])].pos),(particles[int(cr1[2])].pos)], radius=0.1, color = color.white)
    if float(cr1[0]) >= cy_max:
      break
    i = i + 1


print('finished init')

'''
i = 0
strain = 0
l = 0
for line in f:
   rate(500)

   cr = line.split()
   pn = i%np
   i = i + 1
   #print(pn)
   if pn == 0:
       #g.seek(0)
       ind = 0
       j = j+1
       l = 0
        #print(j);
       for obj in scene.objects:
            if isinstance(obj, curve):
                obj.visible = False
       for line in g:
            cr1 = line.split()
            if float(cr1[0]) < j and float(cr1[0]) > j-2:
                if (abs(particles[int(cr1[1])].pos.x - particles[int(cr1[2])].pos.x) < xm/2.0) and (abs(particles[int(cr1[1])].pos.y - particles[int(cr1[2])].pos.y) < ym/2.0) and (abs(particles[int(cr1[1])].pos.z - particles[int(cr1[2])].pos.z) < zm/2.0):
                     l = l+1   
                     if float(cr1[3]) < 0:
                        network[l]= curve(pos=[(particles[int(cr1[1])].pos),(particles[int(cr1[2])].pos)], radius=0.1, color = color.white)
                     if float(cr1[3]) > 2:
                        #rate(50)
                        network[l]= curve(pos=[(particles[int(cr1[1])].pos),(particles[int(cr1[2])].pos)], radius=0.1, color = color.red)#network= curve(pos=[(particles[int(cr1[1])].pos),(particles[int(cr1[2])].pos)], radius=0.1, color = color.cyan)
            if float(cr1[0]) >= j:
                #print(cr1[0])
                break
  # particles[ind].rotate(angle = pi/3200, axis = (0,0,-1), origin = (float(cr[0]),float(cr[1]),float(cr[2])))
   particles[ind].pos[0] = float(cr[2])
   particles[ind].pos[1] = float(cr[4])
   particles[ind].pos[2] = float(cr[3])

   

   ind = ind + 1
'''

f.close()





