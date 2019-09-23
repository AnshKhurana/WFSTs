import sys

if __name__ == '__main__':
    word = input()
    with open('tA.txt', 'w', encoding='utf8') as f:
        last = len(word)
        cur_state = 0
        next_state = 1
        for letter in list(word):
            f.write(str(cur_state) + " " + str(next_state) + " " + letter + " " + letter + "\n")
            cur_state = next_state
            next_state = next_state + 1
        f.write(str(cur_state) + "\n")





