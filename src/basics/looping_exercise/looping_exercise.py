# Loop through numbers 1-20
# for 4 and 13 print "x is unlucky"
# for even numbers print "x is even"
# for odd numbers print "x is odd"


def loop_through_print_output(start, end):
    for x in range(start, end + 1):
        if x == 4 or x == 13:
            output = 'unlucky'
        elif x % 2 == 1:
            output = 'odd'
        else:
            output = 'even'
        print(f'{x} is {output}')


loop_through_print_output(1, 20)
