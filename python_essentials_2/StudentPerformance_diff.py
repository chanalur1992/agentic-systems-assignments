class StudentPerformance:
    def __init__(self,scores_list:list[int]):
        self.scores_list = scores_list
    def score_difference(self):
        try:
            diff = self.scores_list[-1] - self.scores_list[0]  # Calculate the difference between the last and first scores in the list
            print("Difference between last and first score is:", diff)
        except IndexError:
            print("No scores available to calculate difference")

# Example usage
performance = StudentPerformance([80, 90, 85, 70, 95])
performance.score_difference()