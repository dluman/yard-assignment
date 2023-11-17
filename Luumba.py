import os
import math
import narrator
import gitit

from narrator.Checkpoint import set_flag
from narrator.Checkpoint import check_flag

# TODO: Make sure you read the readme.md completely 
# in order to complete this assignment correctly!!!
# https://github.com/term-world/yard-assignment#brand-new-beautification-proposal-prompts-term-world-tenants-to-tidy-up

# Calculating area
# TODO: Create functions wich represent and complete the
#       shapes/calculations required to build the treehouse.
#       This is (at a minimum) three functions for the following shapes:
# TODO: * Triangle
# TODO: * Rectangle
# TODO: * Circle
# When completing term-world assignments *PAY ATTENTION TO THE README*


# MIGHTDO: It could be helpful to create an additional function
#          to assist with the exponents required by at least 
#          two (2) of the above functions.

def main():

    # TODO: Define the "constants" (given measurements) provided
    #       in the README; add comments defining each group
    
    
    # TODO: Use the total variable to add up all of the areas
    #       calculated below
    total = 0

    # TODO: Call functions with correct arguments

    # TODO: Add all of the calculated areas to achieve the full
    #       amount of lumber used; use the "total" variable

    # TODO: Subtract cut-outs from "total" area of wood

    # NARRATIVE -------------------------------------
    n = narrator.Narrator()
    if int(total) == check_flag("lumber"):
        n.path.change({"act": 1, "scene": 0})
        os.makedirs("treehouse", exist_ok=True)
        if not os.path.isfile("treehouse/reflection.md"):
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
