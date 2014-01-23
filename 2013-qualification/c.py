
import math

def palindromeCheck(num):
    num = str(num)
    i = 0
    j = len(str(num))-1
    while True:
        if num[i] == num[j]:
            i = i+1
            j = j-1
            if i>j or i==j:
                return True 
        else:
            return False


def computePalindrome(limit=10**14):
    pval = []
    sqr_pval = []
    i = 1
    sqrt_limit = int (math.sqrt(limit))
    while True:
    # for i in range(1, int(math.sqrt(limit))):
        if palindromeCheck(i):
            if i*i > limit:
                break
            if palindromeCheck(i*i):
                print i
                pval.append(i*i)
        i = i+1
        if i > sqrt_limit:
            break
    print pval
    return pval


def main():
    pval = computePalindrome(limit=10**100)
    f = open('C-large-1.in', 'r')
    r = open('C-large-2.in-result', 'w')

    while True:
        line = f.readline()
        if not line:
            break
        caseNum = int(line)
        for i in range(caseNum):
            start, end = f.readline().rstrip().split(' ')
            result = [ x for x in pval if x >= int(start) and x<=int(end)]
            result_line = 'Case #' + str(i + 1) + ': ' + str(len(result))
            r.write(result_line + '\n')
            print result_line

    f.close()
    r.close()   


if __name__ == '__main__':
    main()









