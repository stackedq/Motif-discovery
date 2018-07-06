Input are n strings (s1, s2, … , sn) of length m each from an alphabet Σ and
two integers l and d. Find all strings x such that |x| = l and every
input string contains at least one variant of x at a Hamming distance of at most d.
Each such x is referred to as an (l, d) motif.

For example, if the input strings are GCGCGAT, CACGTGA, and CGGTGCC; l = 3 and d = 1,
then GGT is a motif of interest. Note that the first input string has GAT as a substring,
the second input string has CGT as a substring, and the third input string has GGT as a substring.
GAT is a variant of GGT that is within a Hamming distance of 1 from GGT, etc.
Call the variants of a motif that occur in the input strings as instances of the motif.
For example, GAT is an instance of the motif GGT that occurs in the first input string.
