# Created by: Serge Hamouche
# Created on: Feb 27, 2025
# This module shows how local and global variables work
# global variable
variable_x = 35


def local_variable() -> None:
    """The local_variable() function creates local variables, returns None."""
    variable_x = 15
    variable_y = 25

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Local variable:  {variable_x} + {variable_y} = {variable_z}")


def global_variable() -> None:
    """The global_variable() function uses a global variable, returns None."""
    global variable_x
    variable_y = 30

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main() -> None:
    """The main() function shows local and global variables, returns None."""
    local_variable()
    global_variable()

    print("\nDone.")


if __name__ == "__main__":
    main()
