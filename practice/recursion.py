def reverse(word):
    if len(word) == 0:
        return ''
    # return word[-1] + reverse(word[0:-1])
    return reverse(word[1:]) + word[0]



print(reverse('esiarp'))
print(reverse(''))


def if_palindrome(word):
    if word == '':
        # return '' # This did not work for empty string.
        return True
    if word[0] == word[-1]:
        if_palindrome(word[1:-1])
        return True

    return False

print(if_palindrome('kayak'))
print(if_palindrome('race'))
print(if_palindrome(''))


def dec_to_binary(num):
    if num == 0:
        return ''

    rem, num = str(num % 2), num // 2
    
    return dec_to_binary(num) + rem

print(dec_to_binary(233))


def sum_natural_no(num):
    if num == 1:
        return 1
    return num + sum_natural_no(num - 1)

print(sum_natural_no(10))