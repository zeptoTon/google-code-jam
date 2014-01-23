"""
2013 - qualification Problem B
Lawnmower
"""

"""
find the top row, left col
sort them from small to large
check do they have a row or col height equal to them (not greater or smaller)
If not satisfy, return NO

dict data structure:
lawn('1'): {h=1..100, clear=True|False}
tuple(height, coord, 'row|col', check)
"""

def lawnSort(lawn, n , m):
	# pick out the 1st row and col
	row = lawn[0]
	col = [col[0] for col in lawn]
	trueTable = [ ]
	# sort them from small to large, remember to keep the coord
	for i in range(m):
		for j in range(n):
			h = int(lawn[j][i])


	return False



def main():
    f = open('B-small-attempt0.in', 'r')
    r = open('A-small-attempt0.in-result', 'w')

    while True:
        line = f.readline()
        if not line:
            break
        totalCaseNum = int(line)
        for i in range(totalCaseNum):
        	n , m = f.readline().split(' ')
        	lawn = []
            for j in range(n):
                row = f.readline().rstrip().split(' ')
                lawn.append(row)
            # ready to check case
            lowSort(lawn, int(n) , int(m))
            result_line = 'Case #' + str(i + 1) + ': ' + result
            r.write(result_line + '\n')
            print result_line


    f.close()
    r.close()



if __name__ == '__main__':
    main()
