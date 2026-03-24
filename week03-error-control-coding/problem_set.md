 Week 3 Problem Set: Error Control Coding

 Topic
Link Layer – Error Control Coding (Lecture 5)

---

 Problem 1: Code Rate

A block code takes k = 4 data bits and produces an n = 7 bit codeword.

 Solution

The code rate is:

Rc = k / n = 4 / 7 ≈ 0.571

So about 57.1% of the transmitted bits carry data, while the rest are redundant bits used for error protection.

---

 Problem 2: Hamming Distance

Find the Hamming distance between the two codewords:

1011010  
1110011

 Solution

Compare the bits position by position:

- Position 1: same
- Position 2: different
- Position 3: same
- Position 4: different
- Position 5: same
- Position 6: same
- Position 7: different

There are 3 positions where the bits differ.

Answer: d = 3

---

 Problem 3: Minimum Distance of a Code

Consider the code:

C = {000, 011, 101, 110}

Find the minimum distance d_min.

 Solution

Compute all pairwise Hamming distances:

- dist(000, 011) = 2
- dist(000, 101) = 2
- dist(000, 110) = 2
- dist(011, 101) = 2
- dist(011, 110) = 2
- dist(101, 110) = 2

The smallest distance is 2.

Answer: d_min = 2

---

 Problem 4: Error Detection and Correction Capability

For a code with minimum distance d_min = 5:

1. What is the maximum number of errors that can be detected?
2. What is the maximum number of errors that can be corrected?

 Solution

Using the d_min rules:

To detect d errors, need:
d_min ≥ d + 1

So maximum detection is:

ed = d_min - 1 = 5 - 1 = 4

To correct d errors, need:
d_min ≥ 2d + 1

So:

2d + 1 ≤ 5  
2d ≤ 4  
d ≤ 2

Maximum correction is 2 errors.

Answer:
- Maximum detection: 4 errors
- Maximum correction: 2 errors

---

Problem 5: Valid (e_c, e_d) Pairs

A code has d_min = 7.

Find all valid (e_c, e_d) pairs.

Solution

The d_min theorem says:

e_c + e_d ≤ d_min - 1  
e_c ≤ e_d

Since d_min = 7:

e_c + e_d ≤ 6  
e_c ≤ e_d

Check valid pairs:

- (0, 6)
- (1, 5)
- (2, 4)
- (3, 3)

These are the valid pairs.

Answer:
(0, 6), (1, 5), (2, 4), (3, 3)

---

 Problem 6: Repetition Code

A (3,1) repetition code uses the codewords {000, 111}.

1. What is the code rate?
2. What is d_min?
3. What are two possible error-control strategies?

 Solution

1. Code rate:

Rc = k / n = 1 / 3

2. Minimum distance:

dist(000, 111) = 3

So d_min = 3.

3. Since d_min = 3, the code can support:

- Maximum correction: (e_c, e_d) = (1, 1)
- Maximum detection: (e_c, e_d) = (0, 2)

Answer:
- Rc = 1/3
- d_min = 3
- Possible strategies: correction of 1 error or detection of up to 2 errors

---

 Problem 7: Parity Code

An even-parity code adds one parity bit to 3 data bits, creating a (4,3) code.

1. What is the code rate?
2. What is d_min?
3. What can this code detect and correct?

 Solution

1. Code rate:

Rc = 3 / 4 = 0.75

2. For even parity, every valid codeword differs from another valid codeword by at least 2 bits.

So:

d_min = 2

3. A code with d_min = 2 can:

- Detect 1 error
- Correct 0 errors

Answer:
- Rc = 0.75
- d_min = 2
- Detects single-bit errors, cannot correct errors

---

 Problem 8: Design Comparison

Compare these two 3-bit code designs:

Design A: {000, 111}  
Design B: {000, 011, 101, 110}

Discuss the tradeoff between rate and error protection.

 Solution

 Design A
- Number of codewords = 2
- k = 1
- n = 3
- Rc = 1/3
- d_min = 3

This design has a low rate but stronger error protection.
It can detect 2 errors or correct 1 error.

 Design B
- Number of codewords = 4
- k = 2
- n = 3
- Rc = 2/3
- d_min = 2

This design has a higher rate but weaker protection.
It can detect 1 error but cannot correct errors.

 Main tradeoff

Packing more codewords into the same n-bit space increases the rate, but usually reduces d_min.
That weakens error-control capability.

Answer:
Higher rate usually means weaker protection, while stronger protection requires more redundancy and a lower rate.

---

 Reflection

This problem set made the tradeoff in error control much clearer to me.

At first, block codes just looked like a list of binary strings, but working through the code rate, Hamming distance, and d_min theorem showed how everything connects. The rate tells how efficient the code is, while d_min tells how much protection it provides.

The biggest takeaway for me is that there is no free improvement. If I want more detection or correction power, I usually need more redundancy, which lowers throughput. That makes the link layer feel more like an engineering tradeoff than just a formula sheet.
