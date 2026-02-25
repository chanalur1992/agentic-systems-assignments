class StudentScores:
    def __init__(self,scores_list:list[int]):
        self.scores_list = scores_list
    def highest_score(self):
        try:
            highest = max(self.scores_list[-2:])  # Get the highest score among the last two scores in the list
            print("Highest score among last two is:", highest)
        except IndexError:
            print("Not enough scores to find highest value")

# Example usage
scores = StudentScores([80, 90, 85, 70, 95])
scores.highest_score()