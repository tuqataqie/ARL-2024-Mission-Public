#!/usr/bin/env python3
import matplotlib.pyplot as plt
from typing import List
from matplotlib.animation import FuncAnimation
from PIL import Image  # Import Pillow for saving GIFs

def numOfYears(a: int, b: int) -> int:

    n = 0
    while a <= b:
        a *= 3  # Stock A triples each year
        b *= 2  # Stock B doubles each year
        n += 1  # Increment year counter
    return n

def visualizer(A_List: List[int], B_List: List[int], n: int) -> None:
   
    fig, ax = plt.subplots()

    # Initial plot setup
    bar = ax.barh(['A', 'B'], [A_List[0], B_List[0]], color=['blue', 'orange'])
    ax.set_xlim(0, max(A_List[-1], B_List[-1]) * 1.1)  # Set x-axis limit
    ax.set_title('Stock Values Over the Years')
    ax.set_xlabel('Stock Value')

    # Update function for animation
    def update(frame):
        # Update the values of the bars
        bar[0].set_width(A_List[frame])  # Update Stock A
        bar[1].set_width(B_List[frame])  # Update Stock B
        return bar

    # Create the animation
    animation = FuncAnimation(fig, update, frames=len(A_List), repeat=False, interval=500)

    # Display the animation
    plt.show()

    # Save the animation as a GIF
    gif_path = 'stock_animation.gif'
    animation.save(gif_path, writer='pillow')

    print(f"Animation saved as {gif_path}")

def main() -> None:
    input_string = input("Please Enter The 2 Numbers: ")

    a, b = map(int, input_string.split())
    years = numOfYears(a, b)  # Calculate the number of years
    A_List, B_List = [a], [b]  # Initialize lists with initial values

    # Calculate stock values for each year
    for _ in range(years):
        a *= 3
        b *= 2
        A_List.append(a)
        B_List.append(b)

    print("Number of years:", years)

    # Show the animation and save it as a GIF
    visualizer(A_List, B_List, years)

if __name__ == "__main__":
    main()
