""" In the RandomWalk class, x_step and y_step are generated from the same set 
of conditions. The direction is chosen randomly from the list [1, -1] and the 
distance from the list [0, 1, 2, 3, 4]. Modify the values in these lists to see 
what happens to the overall shape of your walks. Try a longer list of choices 
for the distance, such as 0 through 8, or remove the −1 from the x- or 
y-direction list. """


import matplotlib.pyplot as pyplot
from random import choice


class RandomWalker:
    """ A class to generate random walk choices. This version has two different 
    max step length of x and y, comparing to previous version 15-3  """

    def __init__(self, walk_steps_num, step_max_length_x, step_max_length_y) -> None:
        """ Init a walker with total steps and max length of each step """
        self.walk_num = walk_steps_num
        self.walk_path_x = [0]
        self.walk_path_y = [0]
        self.step_max_length_x = step_max_length_x
        self.step_max_length_y = step_max_length_y
        
    def walk(self):
        """ Generate a random walk choice """
        previous_walk_position_x = self.walk_path_x[-1]
        previous_walk_position_y = self.walk_path_y[-1]
        current_walk_increment_x = choice([-1, 1]) * choice([0, self.step_max_length_x])
        current_walk_increment_y = choice([-1, 1]) * choice([0, self.step_max_length_y])
        self.walk_path_x.append(previous_walk_position_x + current_walk_increment_x)
        self.walk_path_y.append(previous_walk_position_y + current_walk_increment_y)

    def wall_all(self):
        """ Calculate all the walk choice from start to end """
        for walk_count in range(self.walk_num):
            self.walk()

    
# Make a random walk choice instance
walker = RandomWalker(5000, 6, 30)
walker.wall_all()

# Plot the path of the random walk choice instance       
fig, ax = pyplot.subplots()
ax.plot(walker.walk_path_x, walker.walk_path_y)
pyplot.show()