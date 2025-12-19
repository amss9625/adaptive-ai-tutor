import tkinter as tk
from tkinter import ttk
import json
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.exercise_manager import ExerciseManager
from ai.watcher import Watcher
from ai.progression_engine import ProgressionEngine
from ai.coding_evaluator import CodingEvaluator
from ai.concept_gap_manager import ConceptGapManager

DATA_PATH = "data/user_attempts.json"

def load_exercises():
    with open("data/coding_exercises.json", "r") as f:
        return json.load(f)

class TutorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adaptive AI Tutor")

        self.user_profile = {
            "patterns": {
                "rushed_attempts": 0,
                "easy_exercise_grinding": 0,
                "total_attempts": 0,
                "total_time": 0,
                "total_hints": 0
            }
        }

        self.exercises = load_exercises()
        self.em = ExerciseManager(self.exercises)
        self.watcher = Watcher(self.user_profile, self.em)
        self.progression = ProgressionEngine()
        self.evaluator = CodingEvaluator()
        self.concept_manager = ConceptGapManager()

        self.build_ui()
        self.load_exercise()

    def build_ui(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.coding_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.coding_tab, text="Coding")

        self.prompt = tk.Label(self.coding_tab, text="", wraplength=500)
        self.prompt.pack(pady=10)

        self.input_box = tk.Text(self.coding_tab, height=10)
        self.input_box.pack()

        self.submit_btn = tk.Button(self.coding_tab, text="Submit", command=self.submit)
        self.submit_btn.pack(pady=5)

        self.feedback = tk.Label(self.coding_tab, text="", fg="blue", wraplength=500)
        self.feedback.pack(pady=10)

    def load_exercise(self):
        self.em.start_exercise()
        exercise = self.em.get_current_exercise()
        self.prompt.config(text=exercise["prompt"])
        self.input_box.delete("1.0", tk.END)
        self.feedback.config(text="")

    def submit(self):
        user_code = self.input_box.get("1.0", tk.END)
        exercise = self.em.get_current_exercise()

        result = self.evaluator.evaluate(user_code, exercise)
        time_taken = self.em.get_elapsed_time()

        self.watcher.analyze_attempt(
            difficulty=exercise["difficulty"],
            time_taken=time_taken,
            wasted_attempts=self.em.wasted_attempts,
            hints_used=self.em.hint_index
        )

        log_entry = {
            "timestamp": int(time.time()),
            "exercise_id": exercise["id"],
            "correct": result["correct"],
            "logic_features": result["logic_features"],
            "time_taken": time_taken
        }

        self.log_attempt(log_entry)

        if result["correct"]:
            self.feedback.config(text="Correct. Moving to next exercise.")
            self.em.next_exercise()
            self.load_exercise()
        else:
            gaps = self.concept_manager.detect_gaps(result["logic_features"])
            lessons = self.concept_manager.get_micro_lessons(gaps)
            self.feedback.config(text="\n".join(lessons))

    def log_attempt(self, entry):
        if not os.path.exists("data"):
            os.makedirs("data")

        attempts = []
        if os.path.exists(DATA_PATH):
            with open(DATA_PATH, "r") as f:
                attempts = json.load(f)

        attempts.append(entry)

        with open(DATA_PATH, "w") as f:
            json.dump(attempts, f, indent=2)

root = tk.Tk()
TutorGUI(root)
root.mainloop()
