class Watcher:
    def __init__(self, user_profile, exercise_manager):
        self.profile = user_profile
        self.em = exercise_manager

    def analyze_attempt(self, difficulty, time_taken, wasted_attempts, hints_used):
        patterns = self.profile["patterns"]

        if time_taken < 10:
            patterns["rushed_attempts"] += 1

        if difficulty <= 1:
            patterns["easy_exercise_grinding"] += 1

        patterns["total_attempts"] += 1
        patterns["total_time"] += time_taken
        patterns["total_hints"] += hints_used
