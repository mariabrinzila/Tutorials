def towers_hanoi(n, first, second, third):
    """
    :param n: the number of the current disk which will be moved
    :param first: the rod where the current disk is currently on
    :param second: the auxiliary rod for moving the current disk from rod first to rod second
    :param third: the rod where the current disk will be moved to
    :return: void
    """
    # The idea is to move almost all disks (n - 1) from the first rod to the second one
    # Taking multiple moves to do so (juggling them between the second and third rods)
    # Move the last remaining disk to the third rod
    # Move almost all disks (n - 1) from the second rod to the third one
    # Just like moving the disks from the first rod to the second one
    # Subproblems <=> getting each disk from the first rod to the third one
    if n > 0:
        towers_hanoi(n - 1, first, third, second)

        print("Moved the disk " + str(n) + " from rod " + first + " to rod " + third)

        towers_hanoi(n - 1, second, first, third)
