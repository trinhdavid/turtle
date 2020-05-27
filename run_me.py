from turtle import Turtle
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
plt.title("Turtle's Path")

ax = plt.axes()
ax.grid()
my_turtle = Turtle(0, 0)


def animate(i):
    xs = []
    ys = []
    x = 0
    y = 0
    count = 0
    while count <= i and count < len(my_turtle.full_path()):
        x = my_turtle.full_path()[count][0]
        y = my_turtle.full_path()[count][1]
        xs.append(float(x))
        ys.append(float(y))
        count += 1
    ax.plot(xs, ys, 'o-', color='gray', Lw=3)
    ax.plot(x, y, color='green', marker='o', linewidth=3)


    # mark points where turtle has visted more than once
    # at the end of the journey.
    if i == len(my_turtle.full_path())-1:
        count = 0
        xs_visited = []
        ys_visited = []
        while count < len(my_turtle.visited_multiple_times()):
            x_visited = my_turtle.visited_multiple_times()[count][0]
            y_visited = my_turtle.visited_multiple_times()[count][1]
            xs_visited.append(float(x_visited))
            ys_visited.append(float(y_visited))
            count += 1

        ax.plot(xs_visited, ys_visited, color='blue', marker='x', linewidth=0)


def start(filename):

    print('\nFilename: {}\n'.format(filename))

    with open(filename, mode='r') as f:
        while True:
            move = f.read(1)
            if not move:
                break
            if move == 'F':
                my_turtle.move_forward()
            elif move == 'L':
                my_turtle.turn_left()
            elif move == 'R':
                my_turtle.turn_right()

    ax.set_xlim([my_turtle.x_min-10, my_turtle.x_max+10])
    ax.set_ylim([my_turtle.y_min-10, my_turtle.y_max+30])

    print('Journey ended at position: {}\n'.format(my_turtle.current_position()))
    my_turtle.print_full_path()
    my_turtle.print_visited_more_than_once()

    ani = animation.FuncAnimation(fig, animate, frames=len(my_turtle.full_path()), interval=100, repeat=False)
    plt.show()


if __name__ == '__main__':
    # ("FFFLFFLLF" would, for example return: (-1,3)
    #start('directions-0.txt')

    # Uncomment to run the direction file. Direction files
    # must be located in the same directory as
    # run_me.py. Run only one direction at a time.
    #
    #start('directions-1.txt')
    #start('directions-2.txt')
    start('directions-3.txt')
    #start('directions-4.txt')
    #start('directions-5.txt')
    #start('directions-6.txt')
