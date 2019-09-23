import sys

if __name__ == '__main__':
    word = sys.argv[1]
    with open('tA.txt', 'w', encoding='utf8') as f:
        f.write("0 1 "+word+" "+word + '\n')
        f.write("1")
