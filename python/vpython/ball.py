import vpython as vp
import numpy as np

ball_radius = 1

ball_one = vp.sphere(radius=ball_radius)
ball_two = vp.sphere(radius=ball_radius,color=vp.color.blue,pos=vp.vector(2 * ball_radius,2*ball_radius,0))

ball_two_velocity = vp.vector(1,1,0)

times = np.linspace(0, 10,10)
for times in times:
    ball_two.pos = ball_two_velocity * time + ball_two_initial_position
vp.sleep(15)