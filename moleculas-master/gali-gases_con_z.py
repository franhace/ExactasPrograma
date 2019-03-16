#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:34:09 2019

@author: ep-m2-07
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:44:26 2019

@author: Galileo Cappella
"""

import random
import numpy as np

def random_start(n, x_size, y_size, z_size): #U: Creates random positions for each molecule #A: Stolen from my Prey vs Predator simmulator
    r= np.repeat(" ", x_size*y_size*z_size).reshape(x_size, y_size, z_size)
    x_pos= []
    y_pos= []
    z_pos= []
    
    i= 0
    while i < n:
        pos= (random.randint(0, x_size-1), random.randint(0, y_size-1), random.randint(0, z_size-1))
        if r[pos] == " ":
            r[pos]= "P"
            x_pos.append(pos[0])
            y_pos.append(pos[1])
            z_pos.append(pos[2])
            i+= 1
        
    return x_pos, y_pos, z_pos

def random_vel(n, vmin, vmax): #U: Creates n random start speeds (x y and z are the same)
    r= []
    for i in range(n):
        r.append(random.randint(vmin, vmax)**(1./3.))
        
    return r, r, r

def random_mass(n, which): #U: Chooses between the possible masses for each molecule #XXX: Add ammounts for each
    r= []
    for i in range(n):
        r.append(which[random.randint(0, len(which)-1)])

    return r
    
def calc_force(i, pos_x, pos_y, pos_z, K): #U: Calculates the force "felt" by this molecule
    #A: For the formulas see README
    Fx, Fy, Fz= [0] * 3 #A: Each force starts with a value of zero
    for j in range(len(pos_x)):
        if j != i:
            distance= (pos_x[i]-pos_x[j])**2 + (pos_y[i]-pos_y[j])**2 + (pos_z[i]-pos_z[j])**2
            Fx+= (pos_x[i]-pos_x[j])/(distance**3)
            Fy+= (pos_y[i]-pos_y[j])/(distance**3)
            Fz+= (pos_z[i]-pos_z[j])/(distance**3)
    Fx= 4*K*Fx
    Fy= 4*K*Fy
    Fz= 4*K*Fz
    
    return Fx, Fy, Fz

def calc_cinetic(m, vx, vy, vz): #U: Calculates the cinetic energy of the sistem
    Ce= 0
    for i in range(len(m)):
        v= vx[i]**2 + vy[i]**2 + vz[i]**2
        Ce+= 0.5*m[i]*v #A: See README
    return Ce

def calc_pot(K, pos_x, pos_y, pos_z): #U: Calculates the potential energy of the sistem
    Pe= 0
    for i in range(len(pos_x)):
        for j in range(len(pos_x)):
            if i != j:
                Pe+= K/((pos_x[i]-pos_x[j])**2 + (pos_y[i]-pos_y[j])**2 + (pos_z[i]-pos_z[j])**2)
    return Pe

def check_sides(pos, v, side): #U: Checks if the molecule bounced with a side
    if pos > side:
        v= -v
        pos-= 2*(pos-side)
    if pos < 0:
        v= -v
        pos-= 2*pos

    return pos, v

def simmulate(n=20, r=1, dt=1, which=[1], vol= 50, vmin=0, vmax=0): 
    #A: n=ammount of molecules; r= ammount of frames; dt= delta time in seconds; which= possible masses for the molecules; vol= volume in cm3; vmin/vmax= range for the initial speeds
    print("START simmulation")
    K= 1E-1 #A: I use this value because it works for me, but the actual constant K = 1.38064852E-23
    
    pos_x, pos_y, pos_z= random_start(n, vol, vol, vol)
    vx, vy, vz= random_vel(n, vmin, vmax)
    m= random_mass(n, which)
    
    energy= open("energy.xyz", "w") #A: For storing the energy values #XXX: Change extension
    salida= open("salida.xyz", "w") #A: For making the ".xyz" file and storing the coordinates
    for l in range(r):
        Ce= calc_cinetic(m, vx, vy, vz)
        Pe= calc_pot(K, pos_x, pos_y, pos_z)
        print(l, Pe, Ce, Pe+Ce, file=energy)
        
        print(n, file=salida)
        print(" ", file=salida)
        for jj in range(n):
            print("6", pos_x[jj], pos_y[jj], pos_z[jj], "0", file=salida)
        
        paso_x= []
        paso_y= []
        paso_z= []
        
        for i in range(n):
            Fx, Fy, Fz= calc_force(i, pos_x, pos_y, pos_z, K)
            
            vx[i]+= (Fx/m[i])*dt #A: See README
            vy[i]+= (Fy/m[i])*dt
            vz[i]+= (Fz/m[i])*dt
            
            esta_x= pos_x[i]+vx[i]*dt
            esta_y= pos_y[i]+vy[i]*dt
            esta_z= pos_z[i]+vz[i]*dt
            
            esta_x, vx[i]= check_sides(esta_x, vx[i], vol)
            esta_y, vy[i]= check_sides(esta_y, vy[i], vol)
            esta_z, vz[i]= check_sides(esta_z, vz[i], vol)
        
            paso_x.append(esta_x)
            paso_y.append(esta_y)
            paso_z.append(esta_z)

        pos_x= paso_x.copy()
        pos_y= paso_y.copy()
        pos_z= paso_z.copy()
        
    print("END simmulation")
    
simmulate(250, 1000)