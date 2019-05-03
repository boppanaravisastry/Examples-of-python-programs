fh=open('sample_data.txt')
lines = [line.split(' ') for line in fh]
output = open("sorted_data.txt", 'w')
for line in sorted(lines[0]):
    output.write(' '.join(line))
output.close()
