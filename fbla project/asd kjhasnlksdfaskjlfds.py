for grade in range(9, 13):
    cursor.execute("SELECT * FROM students WHERE grade = :grade", {'grade': grade})
    gradeValues= cursor.fetchall()
    gradeMax = list()
    max2 = 0
    for i in range(len(gradeValues)):
        if gradeValues[i][3] > max2:
            max2 = gradeValues[i][3]
    for i in range(len(gradeValues)):
        if max2 == gradeValues[i][3]:
            gradeMax.append(gradeValues[i])
    print(gradeMax)

    if len(gradeMax) > 1:
        Label5 = ctk.CTkLabel(win, text= "The students that tied for first place in grade " + str(grade) + " are:" , corner_radius=10)
        Label5.pack()
        for i in range(len(gradeMax)):
            Labe6 = ctk.CTkLabel(win, text=f" {(gradeMax[i][0]).title()} {(gradeMax[i][1][0]).title()}. with a total of: {gradeMax[i][3]} points.", corner_radius=10)
            Labe6.pack()
    else:
        Label7 = ctk.CTkLabel(win, text= "The student that won first place in grade " + str(grade) + " is: ", corner_radius=10)
        Label7.pack()

        Label8 = ctk.CTkLabel(win, text=f" {(gradeMax[0][0]).title()} {(gradeMax[0][1][0]).title()}. with a total of: {gradeMax[0][3]} points.", corner_radius=10)
        Label8.pack()