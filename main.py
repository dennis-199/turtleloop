# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import turtle
wn = turtle.Screen()
dennis = turtle.Turtle()
dennis.color("red")
dennis.shape("turtle")
distance = 5
dennis.up()
for _ in range(40):
    dennis.stamp()
    dennis.forward(distance)
    dennis.right(24)
    distance=distance + 2
wn.exitonclick()
