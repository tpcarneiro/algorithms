# The Unique Sum Sequence

The unique sum sequence is a sequence of natural numbers that starts with 1 and 2.
The remaining of the sequence can be calculated by adding 2 numbers already in the list. 

The following rules apply:
1. The calculated sum is a valid element of the sequence only if no other two elements would result the same number
2. The same element cannot be used more than once in each sum.

For example, following these rules, the first 5 elements of the sequence will be:
[1, 2, 3, 4, 6]

The number 5 is not a valid element of the unique sum sequence because it can be obtained by adding more than one combination of elements. In this case: 1+4 = 5 and 2+3 = 5.

Problem: What is the number that occupies the 1000000th position in the sequence? 