"""Suppose there is a class that contains many methods, does too many things.
How to separate categories of functions into their own spaces?"""


# ! God object
class Root:

    # ! the credentials are necessary for every other function to work.
    def __init__(self, credentials):
        self.credentials = credentials

    # Branch A functionality
    # ! want to separate this into it's own class/module, but how to acess Root's credentials necessary for this function to work?
    def function_a_1(self):
        print(f"Root's credentials='{self.credentials}'")

    def function_a_2(self): ...

    # Branch B functionality
    def function_b_1(self): ...

    # ! What if I need to access functions from a different grouping (Branch)?
    def function_b_2(self):
        self.function_a_1()


root = Root("secret")
