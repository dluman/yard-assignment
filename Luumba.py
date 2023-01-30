import os
import math
import narrator
import gitit

from narrator.Checkpoint import set_flag
from narrator.Checkpoint import check_flag

# Create functions wich represent and complete the
# shapes/calculations required to build the treehouse
def triangle(leg: float = 0.0, hyp: float = 0.0) -> float:
    """Triangle function to calculate gable board-feet"""
    return leg * (
        (
            power(
                number = (square(hyp) - square(leg)),
                exp = .5
            )
        ) / 2
    )

def circle(radius: float = 0.0) -> float:
    """Circle functoin to calculate tree cut-out"""
    return math.pi * square(radius)

def square(number: float = 0.0) -> float:
    """Extra function for just squares, 'cause why not?"""
    return power(number = number, exp = 2)

def rectangle(length: float = 0.0, width: float = 0.0) -> float:
    """Calculates the area of a rectangle for walls and cut-outs"""
    return width * length

def power(number: float = 0.0, exp: float = 0.0) -> float:
    """Extra function for powers, turned out to be useful"""
    return number ** exp

def main():

    # Define the "constants" (given measurements) provided
    #       in the README
    building_x = 18
    building_y = 7
    building_z = 27
    # Gable
    gable_leg = 12.73
    # Windows
    window_x = 8
    window_y = 3
    # Door
    door_x = 5
    # Tree
    tree_rad = 4
    
    # Use the total variable to add up all of the areas
    # calculated below
    total = 0

    # Call functions with correct arguments
    walls = 4 * rectangle(width = building_x, length = building_y)
    roofs = 2 * rectangle(width = gable_leg, length = building_z)
    floor = rectangle(length = building_z, width = building_x)
    gables = 2 * triangle(leg = gable_leg, hyp = building_x)

    # Add all of the calculated areas to achieve the full
    # amount of lumber used
    total += walls + roofs + gables + floor

    # Subtract cut-outs
    total -= circle(radius = tree_rad)
    total -= 6 * rectangle(length = window_x, width = window_y)
    total -= square(number = door_x)

    # NARRATIVE -------------------------------------
    n = narrator.Narrator()
    if int(total) == check_flag("lumber"):
        n.path.change(1)
        os.makedirs("treehouse", exist_ok=True)
        gitit.get(
            file_name="treehouse-reflection.md",
            file_type="reflections"
        )
        os.rename(
            "treehouse-reflection.md",
            "treehouse/reflection.md"
        )
    n.narrate()
    # NARRATIVE -------------------------------------

if __name__ == "__main__":
    main()
