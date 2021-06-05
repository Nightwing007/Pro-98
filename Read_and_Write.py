def swap():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")

    a = open(file1, 'r')
    data_a = a.read()
    b = open(file2,"r")
    data_b = b.read()
    a_1 = open(file1,"w")
    a_1.write(data_b)
    b_2 = open(file2,"w")
    b_2.write(data_a)

swap()