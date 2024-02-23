# To get the index of a row
#row_idx * no_of_col + col_idx

a = [[1, 3, 5],
     [2, 4, 6],
     [0, 7, 8]]

# To get the index of 0
for row_idx, row_val in enumerate(a):
    for col_idx, col_val in enumerate(row_val):
        if col_val == 6:
            print('I am at', row_idx * len(a) + col_idx)
            break


b = [1, 3, 5, 2, 6, 0, 7, 8]

# To get where a value will be in a matrix if the matrix is 2 X 4
# Find 2
print(divmod(len(b), 4))


# PITFALL IN MATRIX
# Shallow Copy of Matrix (using the copy)
a = [[2, 3], [4, 5]]
b = a.copy()
print(a) # [[2, 3], [4, 5]]
print(b) # [[2, 3], [4, 5]]
b[0][0] = 7
print(b) # [[7, 3], [4, 5]]
print(a) # [[7, 3], [4, 5]]


# 22-02-2021 Checkpoint
# https://docs.google.com/forms/d/e/1FAIpQLSd-CEnD9VkGBUsgh5vxUYlxHcMIOYrBXFqSRN2lnDga2Er0uQ/viewscore?viewscore=AE0zAgDdFxfidxpFBlfCKIdlJnEj6Dev9EHitFMkg242fyup-YUiXmEVipC08C9mFg
