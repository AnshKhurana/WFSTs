import sys

if __name__ == '__main__':
    output_filename = sys.argv[1]
    state_set = set()
    input_symbols = set()
    output_symbols = set()
    with open(output_filename, 'r', encoding='utf8') as f:
        with open('transq3.txt', 'w', encoding='utf8') as fout:
            lines = f.readlines()

            for line in lines:
                linesplit = line.split()
                if len(linesplit) < 2:
                    # print(linesplit[0])
                    continue
                state_set.add(linesplit[0])
                state_set.add(linesplit[1])
                fout.write(line)

    with open('transq3.txt', 'a', encoding='utf8') as f:
        for state in state_set:
            f.write(str(state) + "\n" )



