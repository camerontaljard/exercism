__author__ = 'cameron'

def hamming(x, y):

    if len(x) > len(y):

        y = y + ('0' * (len(x) -len(y)))

    if len(x) < len(y):
        x = x + ('0' * (len(y) - len(x)))

    i = 0
    mut = 0

    for a in x:
        if a != y[i]:
            print a, y[i]
            mut += 1
        i += 1

    return mut



#hamming('AAGCTAC','ACGTT')
hamming('AAGCTAC','ACGTTACGTC')


__author__ = 'cameron'

def hamming(x, y):

    xl = len(x)
    yl = len(y)

    if len(x) > len(y):
        y = y + ('0' * (xl -yl))
    if len(x) < len(y):
        x = x + ('0' * (yl - xl))

    i = 0
    mut = 0

    for a in x:
        if a != y[i]:
            #print a, y[i]
            mut += 1
        i += 1

    return mut

    #
    # return (sum(a != b for a, b in zip(original, new)) +
    #         abs(len(original) - len(new)))