class BranchA:

    def __init__(self, main):
        # type: (Root) -> None  # knows about 'Root' before being declared
        self.main = main

    def function_a_1(self):
        print(f"Root's credentials='{self.main.credentials}'")

    def function_a_2(self): ...


class BranchB:

    def __init__(self, main):
        # type: (Root) -> None
        self.main = main

    def function_b_1(self): ...

    def function_b_2(self):
        self.main.branch_a.function_a_1()


class Root:

    def __init__(self, credentials):
        self.credentials = credentials

        self.branch_a = BranchA(self)
        self.branch_b = BranchB(self)

    # def function_a_1(self): ...
    # def function_a_2(self): ...
    # def function_b_1(self): ...
    # def function_b_2(self): ...


root = Root("secret")
root.branch_a.function_a_1()
root.branch_b.function_b_2()
