# Method 1: Import with aliases
import helpers.string_utils as str_utils
import helpers.math_utils as math_utils

def demonstrate_functionality():
    print("\n*** Package Import Demonstration ***\n")

    print("Using alias import:")
    print("shout ->", str_utils.shout('hello'))
    print("area ->", math_utils.area(5, 3))


def explain_namespace_collisions():
    print("\n*** Namespace Collision Explanation ***\n")
    print("If two modules define functions with the same name,")
    print("importing them directly can cause a collision — one overwrites the other.")
    print("Using aliases (import ... as ...) gives each module its own namespace.")


if __name__ == "__main__":
    demonstrate_functionality()
    explain_namespace_collisions()