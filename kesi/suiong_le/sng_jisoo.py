from kesi import Ku
import sys

def sng():
    jisoo = 0
    for line in sys.stdin:
        jisoo += len(list(Ku(line.rstrip()).thianji()))
        print(jisoo)
    print('long-tsong=', jisoo)

if __name__ == '__main__':
    sng()

