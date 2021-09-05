def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # Base case
    if len(sequence) == 1:
        return(list(sequence))
    
    # Recursive steps
    else:
        # initialize list of permutations
        permutations = []
        # hold out the first letter of the sequence
        first = sequence[0]
        # create new copy of sequence starting from second letter
        sequence = sequence[1:]
        # list of permutations of new sequence without first letter
        perm_list = get_permutations(sequence)

        # all ways we can insert first letter into each permutation of new sequence
        for perm in perm_list:  # for each permutation in perm_list
            for i in range(0, len(perm)+1):     # for i in the range of the permutation including first letter
                # create new permutation inserting original first
                # letter to each permutation (see example case below)
                new_perm =  perm[i:] + first + perm[:i]
                # adds new permutation to list
                permutations.append(new_perm)
                
        # returns a list of permutations without repeating elements (c/o set function)
        return list(set(permutations))

'''
EXAMPLE CASE
seq = abcd; len(seq) = 4
perm = bcd
len(perm) = 3
for i in range (0,1,2,3,4)
(i = 0) new_perm = perm[0:] + a + perm[:0] --> bcd + a
(i = 1) new_perm = perm[1:] + a + perm[:1] --> cd + a + b
(i = 2) new_perm = perm[2:] + a + perm[:2] --> d + a + bc
(i = 3) new_perm = perm[3:] + a + perm[:3] --> a + bcd
(i = 4) new_perm = perm[4:] + a + perm[:4] --> a + bcd
'''

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # TEST CASE 1
    example_input = 'abc'
    print('-----------------------')
    print()
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print()

    # TEST CASE 2
    example_input = 'mno'
    print('-----------------------')
    print()
    print('Input:', example_input)
    print('Expected Output:', ['mno', 'mon', 'nmo', 'nom', 'omn', 'onm'])
    print('Actual Output:', get_permutations(example_input))
    print()

    # TEST CASE 3
    print('-----------------------')
    print()
    example_input = 'ijk'
    print('Input:', example_input)
    print('Expected Output:', ['ijk', 'ikj', 'jik', 'jki', 'kij', 'kji'])
    print('Actual Output:', get_permutations(example_input))
    print()