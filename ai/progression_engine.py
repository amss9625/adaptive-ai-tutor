class ProgressionEngine:
    def __init__(self):
        self.progress_score = 0

    def calculate_progress(self, difficulty, time_taken, wasted_attempts):
        base = difficulty * 10

        if time_taken < 10:
            base *= 0.5

        if wasted_attempts > 2:
            base *= 0.7

        return int(base)
