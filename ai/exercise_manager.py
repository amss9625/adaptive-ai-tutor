import time

class ExerciseManager:
    def __init__(self, exercises):
        self.exercises = exercises
        self.current_index = 0
        self.start_time = None
        self.hint_index = 0
        self.wasted_attempts = 0

    def start_exercise(self):
        self.start_time = time.time()
        self.hint_index = 0
        self.wasted_attempts = 0

    def get_current_exercise(self):
        return self.exercises[self.current_index]

    def get_elapsed_time(self):
        if not self.start_time:
            return 0
        return int(time.time() - self.start_time)

    def next_exercise(self):
        if self.current_index < len(self.exercises) - 1:
            self.current_index += 1
            self.start_exercise()

    def use_hint(self):
        self.hint_index += 1
        return self.hint_index
