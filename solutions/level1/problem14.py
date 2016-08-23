from tools.collatz import collatz_length

def longest_collatz_sequence(n):
    max = 1
    result = 1
    for i in range(1, n+1):
        length = collatz_length(i)
        if length > max:
            max = length
            result = i
    return result

if __name__ == '__main__':
    print(longest_collatz_sequence(1000000))
