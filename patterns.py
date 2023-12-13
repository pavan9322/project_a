def right_traingle_pattern(n):
    """

        *
       **
      ***
     ****
    *****
    """
    for i in range(1, n+1):
        print((n+1-i)*" ", i*"*")

# right_traingle_pattern(5)

def right_downward_traingle(n):
    """
    output:
        *****
         ****
          ***
           **
            *
    """

    for i in range(n):
        print(i*" ",(n-i)*"*")

# right_downward_traingle(5)


def square_pattern(n):
    """
        * * * * *
        * * * * *
        * * * * *
        * * * * *
        * * * * *
    """

    for i in range(n):
        print(n*"* ")
# square_pattern(5)


def hollow_square(n):
    """
        *****
        *   *
        *   *
        *   *
        *****
    """

    for i in range(n):
        if i==0 or i== n-1:
            print(n * "*")
        else:
            print("*" + (n-2)*" " + "*")

# hollow_square(5)

def left_traingle_pattern(n):
    """
        *
        **
        ***
        ****
    """

    for i in range(n+1):
        print(i*"*")

# left_traingle_pattern(5)

def right_traingle_pattern(n):
    """

        *
       **
      ***
     ****
    *****

    """

    for i in range(1,n+1):
        print((n+1-i) *" " + i*"*")

# right_traingle_pattern(5)

def left_downward_traingle(n):
    """
    *****
    ****
    ***
    **
    *
    """

    for i in range(0,n):
        print((n-i) * "*" + i*" ")

# left_downward_traingle(5)


def right_downward_traingle(n):
    """
    *****
     ****
      ***
       **
        *
    """

    for i in range(0,n):
        print(i*" "+ (n-i)*"*")

# right_downward_traingle(5)

def hollow_traingle(n):
    """
    *
    **
    *  *
    *   *
    *    *
    *****
    """

    for i in range(n):
        