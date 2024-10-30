
# def find_next_greater_indices(arr):
#   """
#   Finds the indices of the next greater element for each element in an array.

#   Args:
#       arr (List[int]): The input array.

#   Returns:
#       List[int]: An array containing the indices of the next greater element for each element in the input array.
#   """

#   stack = []
#   next_greater = [-1] * len(arr)  # Initialize array with -1 for invalid next greater

#   for i in range(len(arr)):
#     # Pop elements from stack while current element is greater
#     while stack and arr[stack[-1]] < arr[i]:
#       print(arr, stack, next_greater)
#       print(i, 'ng')
#       st = stack.pop()
#       print('pop', st)
      
#       next_greater[st] = i # Update next greater element for popped index
#       print(arr, stack, next_greater)
#       print('--------------')

#     print('stack', i)
#     stack.append(i)  # Push current index onto the stack

#   return next_greater

# # Example usage
# arr = [6, 8, 0, 1, 3]
# arr1 = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
# next_greater = find_next_greater_indices(arr)
# print("Next greater elements:", next_greater)
# next_greater1 = find_next_greater_indices(arr1)
# print("Next greater elements:", next_greater1)


"""
The explanation focuses on how the comparison operator used in the `while` loop condition affects the elements stored in the stack, creating either a **monotonic non-increasing stack** or a **monotonic strictly decreasing stack**.

Here's a breakdown:

**Monotonic Stack:**

- A monotonic stack is a data structure where elements follow a specific order based on their values.
- There are two main types:
    - **Monotonic Increasing:** Elements at the bottom are less than or equal to elements on top (increasing or constant values).
    - **Monotonic Decreasing:** Elements at the bottom are greater than or equal to elements on top (decreasing or constant values).

**Code Context:**

The code you provided uses a stack to find the next greater element for each element in an array. The `while` loop condition plays a crucial role in determining the type of elements stored in the stack.

**1. Operator `<` (Monotonic Non-Increasing Stack):**

- In this case, the `while` loop continues as long as the element at the top of the stack (`arr[stack[-1]]`) is **strictly less than** the current element (`arr[i]`).
- This allows elements with the same value to be present in the stack.
- As a result, the stack becomes **monotonic non-increasing**. This means elements at the top are **less than or equal to** elements below.

**2. Operator `<=` (Monotonic Strictly Decreasing Stack):**

- If the operator were changed to `<=`, the condition would be met even if the top element has the same value as the current element.
- This would force the stack to strictly remove any element with the same value as the current element (since they wouldn't be strictly less than anymore).
- Consequently, the stack would become **monotonic strictly decreasing**. This means elements at the top are **strictly less than** elements below.

**Impact on Functionality:**

- In the context of finding the next greater element, using `<` allows for maintaining a more flexible stack that can handle elements with the same value.
- If `<=` were used, elements with the same value wouldn't be considered as "next greater" and might be removed from the stack prematurely, potentially affecting the results.

**In summary:**

- The choice of operator determines whether the stack allows for elements with the same value (`<` for non-increasing) or enforces strict decrease (`<=` for strictly decreasing).
- The specific use case (like finding next greater elements) often dictates the preferred operator to maintain the correct logic.
"""

def find_previous_greater_indices(arr):
  """
  Finds the indices of the previous greater element for each element in an array.

  Args:
      arr (List[int]): The input array.

  Returns:
      List[int]: An array containing the indices of the previous greater element for each element in the input array.
  """

  stack = []
  previous_greater = [-1] * len(arr)  # Initialize array with -1 for invalid previous greater

  for i in range(len(arr)):
    # Pop elements from stack while current element is greater or equal
    while stack and arr[stack[-1]] <= arr[i]:
      print(arr, stack, 'before pop', previous_greater)
      stack.pop()  # Remove equal elements to maintain strictly decreasing
      print(arr, stack, 'after pop', previous_greater)

    # If stack has elements left, set previous greater element
    if stack:
      previous_greater[i] = stack[-1]

    stack.append(i)  # Push current index onto the stack
    print(stack, 'append')


  return previous_greater

# Example usage
arr = [4, 3, 5, 2, 6, 1]
previous_greater = find_previous_greater_indices(arr)
print("Previous greater elements:", previous_greater)