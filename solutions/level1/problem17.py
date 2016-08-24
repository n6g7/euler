from tools.int_to_words import int2word

def number_letter_counts(max):
    s = 0
    for n in range(1, max+1):
        word = int2word(n)
        s += len(word.replace(' ', ''))
    return s

if __name__ == '__main__':
    print(number_letter_counts(1000))
