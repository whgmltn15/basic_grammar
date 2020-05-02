'''
f = open("multiflication_chart.txt", "a")
for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = %d \n" % (i, j, i * j))
        f.write("%d * %d = %d \n" % (i, j, i * j))
f.close()

f = open("multiflication_chart.txt", "r")
for i in range(1, 10):
    for j in range(1, 10):
        line = f.readline()
        print(line)

f = open("multiflication_chart.txt", "r")
while True:
    line = f.readline()
    if line == "":
        break
    print(line)
'''
f = open("multiflication_chart.txt", "r")
while True:
    line = f.readline()
    if line == "":
        break
    temp = line.split("*")
    temp_2 = temp[1].split("=")
    temp_3 = temp_2[1].split("\n")
    print(temp[0], temp_2[0], temp_3[0])
f.write('"*" + "=" + "\n"' % (temp[0], temp_2[0], temp_3[0]))