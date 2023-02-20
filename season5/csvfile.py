import csv
from statistics import mean 

def calculate_averages(input_file, output_file):
    l = list()
    al = list()

    with open(input_file) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            for grade in row[1:]:
                grade = int(grade)
                l.append(grade)
            av = mean(l)
            li = [name, av]
            al.append(li)
            l = []

    with open(output_file, 'w') as fout:
        for pr in al:
            fout.write('%s,%.2f\n' %(pr[0], pr[1]))
    


def calculate_sorted_averages(input_file, output_file):
    l = list()
    al = list()

    with open(input_file) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            for grade in row[1:]:
                grade = int(grade)
                l.append(grade)
            av = mean(l)
            li = [name, av]
            al.append(li)
            l = []

    for i in al:
        for j in al:
            if i[1] < j[1]:
                (i[0], i[1]) = (j[0], j[1])

    with open(output_file, 'w') as fout:
        for pr in al:
            fout.write('%s,%.2f\n' %(pr[0], pr[1]))
    


def calculate_three_best(input_file, output_file):
    l = list()
    al = list()

    with open(input_file) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            for grade in row[1:]:
                grade = int(grade)
                l.append(grade)
            av = mean(l)
            li = [name, av]
            al.append(li)
            l = []

    for i in al:
        for j in al:
            if i[1] < j[1]:
                alt = [i[0], i[1]]
                [i[0], i[1]] = [j[0], j[1]]
                [j[0], j[1]] = alt

    li = list()
    li2 = list()
    for i in al:
        li.append(i[1])

    li2.append(max(li))
    li.remove(max(li))
    li2.append(max(li))
    li.remove(max(li))
    li2.append(max(li))
    li.remove(max(li))

    lis = list()
    for i in li2:
        for j in al:
            if i == j[1]:
                lis.append(j)

    with open(output_file, 'w') as fout:
        for pr in lis:
            fout.write('%s, %.2f\n' % (pr[0], pr[1]))
    


def calculate_three_worst(input_file, output_file):
    l = list()
    al = list()

    with open(input_file) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            for grade in row[1:]:
                grade = int(grade)
                l.append(grade)
            av = mean(l)
            li = [name, av]
            al.append(li)
            l = []

    for i in al:
        for j in al:
            if i[1] < j[1]:
                alt = [i[0], i[1]]
                [i[0], i[1]] = [j[0], j[1]]
                [j[0], j[1]] = alt

    li = list()
    li2 = list()
    for i in al:
        li.append(i[1])

    li2.append(min(li))
    li.remove(min(li))
    li2.append(min(li))
    li.remove(min(li))
    li2.append(min(li))
    li.remove(min(li))

    lis = list()
    for i in li2:
        for j in al:
            if i == j[1]:
                lis.append(j)

    with open(output_file, 'w') as fout:
        for pr in lis:
            fout.write('%.2f\n' % (pr[1]))
    


def calculate_average_of_averages(input_file, output_file):
    l = list()
    al = list()

    with open(input_file) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            for grade in row[1:]:
                grade = int(grade)
                l.append(grade)
            av = mean(l)
            li = [name, av]
            al.append(li)
            l = []

    for i in al:
        for j in al:
            if i[1] < j[1]:
                alt = [i[0], i[1]]
                [i[0], i[1]] = [j[0], j[1]]
                [j[0], j[1]] = alt

    li = list()
    for grade in al:
        li.append(grade[1])

    mn = '%.4f' %mean(li)

    with open(output_file, 'w') as fout:
        fout.write(mn)

calculate_average_of_averages('./scores.csv', './output.txt')