# # -*- coding: utf-8 -*-
# You are given an integer, NN. Your task is to print an alphabet rangoli of size NN. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------
# The center of the rangoli has the first alphabet letter a, and the boundary has the NNtthh alphabet letter (in alphabetical order).

# Input Format

# Only one line of input containing NN, the size of the rangoli.

# Constraints

# 0<N<270<N<27
# Output Format

# Print the alphabet rangoli in the format explained above.

# Sample Input

# 5
# Sample Output

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


import string

size = int(input())
alphabet = string.ascii_lowercase

for i in range(size - 1, 0, -1):
    row = ["-"] * (size * 2 - 1)
    for j in range(0, size - i):
        row[size - 1 - j] = alphabet[j + i]
        row[size - 1 + j] = alphabet[j + i]
    print("-".join(row))

for i in range(0, size):
    row = ["-"] * (size * 2 - 1)
    for j in range(0, size - i):
        row[size - 1 - j] = alphabet[j + i]
        row[size - 1 + j] = alphabet[j + i]
    print("-".join(row))