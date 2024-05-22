import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
# rw.x_values, rw.y_values 각각에 5000개의 값이 들어있음
ax.scatter(rw.x_values, rw.y_values, cmap=plt.cm.Blues, s=15)
ax.set_aspect('equal')
plt.show()