def GradingStudents(grades):
    grades_final = []
    nota_final = 0
    for grade in grades:
        multiplo5 = grade + (5 - grade % 5)
        dif = multiplo5 - grade

        if grade < 38:
            nota_final = grade
            grades_final.append(nota_final)
        elif grade >= 38 and dif < 3:
            nota_final = multiplo5
            grades_final.append(nota_final)
        elif grade > 38 and dif >= 3:
            nota_final = grade
            grades_final.append(nota_final)
    return grades_final