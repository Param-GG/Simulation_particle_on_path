import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

#defining trajectory constraints
g, s, h = 9.8, 200, 45
theta = np.arctan(4*h /s)
u = np.sqrt((g*s)/np.sin(2*theta))
T = 2*u*np.sin(theta) /g


def get_intervals():
    
    intervals = []
    start = 0.0
    interval = 0.01     #increase value to increase speed of animation
    while start<2*T:
        intervals.append(start)
        start+=interval
    return intervals

def update_position(i, circle, intervals_actual, T, u, theta):

    if i > len(intervals_actual):
        i = 0
    t = intervals_actual[i]
    if t<T:
        x = u*np.cos(theta)*t - 100
        y = u*np.sin(theta)*t - 0.5*g*(t**2)
    else:
        x = -u*np.cos(theta)*(t-T) + 100
        y = 0
    circle.center = (x,y)
    return circle,

def create_animation():

    circle = plt.Circle((x_min,y_min), 10)
    ax.add_patch(circle)

    anim = animation.FuncAnimation(fig, update_position, 
                                        fargs=(circle, intervals_actual, T, u, theta), 
                                        frames = len(intervals_actual), interval=1, 
                                        repeat=True)
    plt.show()



#defining plot
fig, ax = plt.subplots(figsize=(6,3))
ax.set_xlabel('X/mm')
ax.set_ylabel('Y/mm')
ax.set_xlim(-150, 150)
ax.set_ylim(-50, 100)
ax.set_xticks(np.arange(-150,200,50))
ax.set_yticks(np.arange(-50,150,50))
ax.grid(True)
x_min, y_min = -s/2, 0
x_max, y_max = s/2, h

#defining 'time' for eqns of trajectories
intervals = get_intervals()
for i in intervals:
    if not i<=T:
        first, second = np.split(intervals, [intervals.index(i)])
        break
intervals_standing = second[::4]     # 4 taken to make supporting phase 4x faster than swinging phase
intervals_actual = list(first) + list(intervals_standing)

########

create_animation()
