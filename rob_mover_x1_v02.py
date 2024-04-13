# *********************************
# 
#   Robot Kinetics X1 util 
#   2L Planar Robot move tester
#   Dev: AmanB
# 
# *********************************

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Link data
L1 = 2
L2 = 2
theta1 = np.pi/4
theta2 = np.pi/4

# delta time
dt = 0.05
t  = np.arange(0, 10, dt)

# Forward Kinematics for Robot links
def forward_kinematics(theta1, theta2):
    x = L1*np.cos(theta1) + L2*np.cos(theta1+theta2)
    y = L1*np.sin(theta1) + L2*np.sin(theta1+theta2)
    return x,y

def update_plot(i):
    global theta1, theta2
    #if theta1 > 0 and theta1 < 4:
    #for a in range (min(0), max(5)):
    theta1 += 0.10
    theta2 += 0.05
    x, y = forward_kinematics(theta1, theta2)
    
    ax.clear()
    ax.plot([0, L1*np.cos(theta1), x], [0, L1*np.sin(theta1), y], '-o')

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("2 Link Planar Robot")
    print(theta1)

fig, ax = plt.subplots()

# animation set
anim = animation.FuncAnimation(fig, update_plot, frames=len(t), interval=30)
plt.show()




