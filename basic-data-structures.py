# Базовые структуры данных

#1 Модуль назвал - basic-data-structures.py
# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# 2
average_score = [0.0, 0.0, 0.0, 0.0, 0.0]
# 3
average_score[0]=sum(grades[0],0)/grades[0].__len__()
average_score[1]=sum(grades[1],0)/grades[1].__len__()
average_score[2]=sum(grades[2],0)/grades[2].__len__()
average_score[3]=sum(grades[3],0)/grades[3].__len__()
average_score[4]=sum(grades[4],0)/grades[4].__len__()
# 4
students_list = list (students)
# 5
sorted_list_of_students = sorted(students_list)
# 6
list_average_score = {sorted_list_of_students[0] : average_score[0],
                      sorted_list_of_students[1] : average_score[1],
                      sorted_list_of_students[2] : average_score[2],
                      sorted_list_of_students[3] : average_score[3],
                      sorted_list_of_students[4] : average_score[4]}
# 7
print(list_average_score)