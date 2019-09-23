import os
# Single script that generates transq1itions, isymsq1 and osymsq1

if __name__ == '__main__':
    f = open("lex.txt", 'rU', encoding='utf8')

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
    state_num_next = 1

    for line in voc:
        tokens = line.split()
        if not tokens[0] in input_symbols.keys():
            input_symbols[tokens[0]] = next_input_number
            next_input_number = next_input_number + 1

        # for i in range(1, len(tokens)):
        #     if not tokens[i] in output_symbols.keys():
        #         output_symbols[tokens[i]] = next_output_number
        #         next_output_number = next_output_number + 1
        for let in list(tokens[0]):
            if not let in output_symbols.keys():
                output_symbols[let] = next_output_number
                next_output_number = next_output_number + 1


    with open('isymsq3.txt', 'w', encoding='utf8') as f:
        for word in input_symbols.keys():
            f.write(word + " " + str(input_symbols[word]) + "\n")

    with open('osymsq3.txt', 'w', encoding='utf8') as f:
        for sym in output_symbols.keys():
            f.write(sym + " " + str(output_symbols[sym]) + "\n")


    with open('transq3.txt', 'w', encoding='utf8') as f:
        for line in voc:
            tokens = line.split()
            word = tokens[0]
            if len(word) == 1:
                f.write("0 0 " + tokens[0] + " " + tokens[0] + "\n")
            else:
                for i in range(len(word)):
                    if i == 0:
                        f.write("0 " + str(state_num_next) + " " + word + " " + word[0] + "\n")
                        cur_state = state_num_next
                        state_num_next = state_num_next + 1

                    elif i == len(word) - 1:
                        f.write(str(cur_state) + " 0 " + "eps " + str(word[i]) + '\n')
                    else:
                        f.write(str(cur_state) + " " + str(state_num_next) + " eps " + word[i] + '\n')
                        cur_state = state_num_next
                        state_num_next = state_num_next + 1
        for i in range(state_num_next):
            f.write(str(i) + "\n")










