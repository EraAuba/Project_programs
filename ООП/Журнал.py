names = []
counts = []
how_mush = int(input("How mush students? "))

if how_mush>=12:
    for i in range(1, how_mush+1):
        names.append(input('Who is student? '))
    for i in range(1, how_mush+1):
        counts.append(i)
    list_students = dict(zip(names, counts))
    print("List of students: ")
    
    #delete
    def Delete(list1):
        name = str(input('Какое имя? '))
        list1.pop(name)
        values_list = list(list_students.values())
        names_list = list(list_students.keys())
        global counts
        counts.pop()
        for i in range(len(counts)):
            values_list[i] = counts[i] #list = list
        list1 = dict(zip(names_list, values_list))
        print("Удаленный студент: ", list1)

Delete(list_students)





