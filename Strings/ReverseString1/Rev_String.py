def rev(self, s: List[str]) -> None:
    s[:]=s[::-1]

# Look at function header it accepts no return and expects to modify s itself so s[:] allows us to do that 
