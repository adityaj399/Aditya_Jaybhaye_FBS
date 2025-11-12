class TYMARKS:
    def __init__(self, theory=0, practical=0):
        self.Theory = theory
        self.Practical = practical

    def display_marks(self):
        print("Theory Marks:", self.Theory)
        print("Practical Marks:", self.Practical)
        print("Total Marks:", self.Theory + self.Practical)