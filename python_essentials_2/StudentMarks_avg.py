class StudentMarks:
    def __init__(self, marks_list:list[int]):
        self.marks_list = marks_list
    def last_three_avg(self):
        try:
            last_three_marks = self.marks_list[-3:]
            average = sum(last_three_marks) / 3
            print("Average of last 3 marks is:", average)
        except IndexError:
            print("Not enough marks to calculate average")

# Example usage
marks = StudentMarks([80, 90, 85, 70, 95])
marks.last_three_avg()