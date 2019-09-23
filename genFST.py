import os
import sys
# Single script that generates transq1itions, isymsq1 and osymsq1

if __name__ == '__main__':
    file_name = sys.argv[1]
    f = open(file_name, 'rU', encoding='utf8')

    voc = f.readlines()
    f.close()
    state_0 = 0

    input_symbols = {}
    output_symbols = {}
    input_symbols['eps'] = 0
    next_input_number = 1
    next_output_number = 1
    output_symbols['eps'] = 0
    cur_state = 0
    final_state = 1
    state_num_next = 2

    for line in voc:
        tokens = line.split()
        if not tokens[0] in input_symbols.keys():
            input_symbols[tokens[0]] = next_input_number
            next_input_number = next_input_number + 1

        for i in range(1, len(tokens)):
            if not tokens[i] in output_symbols.keys():
                output_symbols[tokens[i]] = next_output_number
                next_output_number = next_output_number + 1

    with open('isymsq1.txt', 'w', encoding='utf8') as f:
        for word in input_symbols.keys():
            f.write(word + " " + str(input_symbols[word]) + "\n")

    with open('osymsq1.txt', 'w', encoding='utf8') as f:
        for sym in output_symbols.keys():
            f.write(sym + " " + str(output_symbols[sym]) + "\n")


    with open('transq1.txt', 'w', encoding='utf8') as f:
        for line in voc:
            tokens = line.split()
            if (len(tokens) == 2):
                f.write("0 1 " + tokens[0] + " " + tokens[1] + "\n")
            else:
                for i in range(len(tokens)-1):
                    if i == 0:
                        f.write("0 " + str(state_num_next) + " " + tokens[0] + " " + tokens[1] + "\n")
                        cur_state = state_num_next
                        state_num_next = state_num_next + 1

                    elif i == len(tokens) - 2:
                        f.write(str(cur_state) + " 1 " + "eps " + str(tokens[i+1]) + '\n')
                    else:
                        f.write(str(cur_state) + " " + str(state_num_next) + " eps " + tokens[i+1] + '\n')
                        cur_state = state_num_next
                        state_num_next = state_num_next + 1

        f.write("1\n")









