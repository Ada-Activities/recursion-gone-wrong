# Examples of broken recursion ##############

# See how each is broken due to the bit that it lacks
# Note, Python RecursionErrors are artificial, the stack isn't really in the system stack, it's a chain of stackframes in the heap
# Python artificially chooses to report RecursionErrors when this chain reaches around 1000 entries "deep"

def call_ourself_01(n):
    print(f"call_ourself_01: {n=}")
    # no base case, recursion never gets smaller
    call_ourself_01(n)

# call_ourself_01(10)

def call_ourself_02(n):
    print(f"call_ourself_02: {n=}")
    # no base case, recursion gets smaller
    call_ourself_02(n - 1)

# call_ourself_02(10)

def call_ourself_03(n):
    print(f"call_ourself_03: {n=}")
    # base case, recursion never gets smaller
    if n:
        call_ourself_03(n)

# call_ourself_03(10)

# Successful recursion, notice that the output resembles a loop counting from 10 to 0

def call_ourself_04(n):
    print(f"call_ourself_04: {n=}")
    # base case, recursion gets smaller
    if n:
        call_ourself_04(n - 1)

# call_ourself_04(1000) # should crash with RecursionError, even though it _would_ finish in just a few more invocations
# call_ourself_04(10)
