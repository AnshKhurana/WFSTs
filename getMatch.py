import os, sys
import subprocess
# output = subprocess.check_output("cat /etc/services", shell=True)

def removeeps(out):
    out = out.split()
    # print(out)
    cleanedout = []
    for token in out:
        if token == 'eps':
            continue
        else:
            cleanedout.append(token)
    # print(cleanedout)
    return " ".join(cleanedout)

if __name__ == '__main__':
    fstdir = sys.argv[1]
    word = sys.argv[2]
    Qsuf = os.path.join(fstdir, "Qsuffix.fst")
    Qpre = os.path.join(fstdir, "Qprefix.fst")
    ctr = 0
    for i in range(len(word)-1):
        ctr += 1
        wpre = word[:i+1]
        wsuf = word[i+1:]
        outputpre = subprocess.check_output("./lookup.sh 3 " + Qpre + " " + wpre, shell=True).decode('utf8')
        if outputpre is None:
            continue
        if len(outputpre) == 0:
            continue
        outputpre = outputpre[:-1]
        outputsuf = subprocess.check_output("./lookup.sh 4 " + Qsuf + " " + wsuf, shell=True).decode('utf8')

        if outputsuf is None:
            continue
        if outputsuf == '\n':
            continue
        if len(outputsuf) == 0:
            continue
        outputsuf = outputsuf[:-1]
        outputsuf = removeeps(outputsuf)
        print(outputpre + outputsuf)
        break
    if ctr == len(word) - 1:
        print("Not found")
