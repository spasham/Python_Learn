def upper_low(s):
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1

    print ("The original string is\n", s)
    print ("The upper case chars are", upper)
    print ("The lower case chars are", lower)

s = input ("Enter a string\n")
upper_low(s)

