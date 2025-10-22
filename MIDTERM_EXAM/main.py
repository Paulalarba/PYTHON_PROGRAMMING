# Import modules using aliases
import helpers.string_utils as su
import helpers.math_utils as mu

# Import specific functions
from helpers.string_utils import shout
from helpers.math_utils import area

def main():
    # Using alias
    print("Using alias:", su.shout("hello world"))
    print("Using alias:", mu.area(5, 10))

    # Using direct import
    print("Direct import:", shout("python rocks"))
    print("Direct import:", area(3, 7))

if __name__ == "__main__":
    main()
