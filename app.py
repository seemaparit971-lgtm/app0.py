def main():
    name = input("Enter student name: ")
    dept = input("Enter department: ")
    sem = input("Enter semester: ")

    marks = [float(input(f"Enter subject {i} marks: ")) for i in range(1, 4)]

    if any(m < 0 or m > 100 for m in marks):
        print("Marks must be between 0 and 100")
        return

    avg = sum(marks) / 3

    if avg >= 90:
        grade = "S"
    elif avg >= 80:
        grade = "A"
    elif avg >= 65:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\nName:", name)
    print("Department:", dept)
    print("Semester:", sem)
    print("Marks:", marks)
    print("Average:", round(avg, 2))
    print("Grade:", grade)

if __name__ == "__main__":
    main()