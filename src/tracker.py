class Tracker:
    def __init__(self):
        self.progress = []

    def add_progress(self, entry):
        self.progress.append(entry)  # Method to add progress entry

    def view_progress(self):
        return self.progress  # Method to view all progress entries