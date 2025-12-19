class ConceptGapManager:
    def __init__(self):
        self.micro_lessons = {
            "Recursion Base Case": [
                "Every recursive function must have a condition that stops it.",
                "Try solving the simplest possible input first."
            ]
        }

    def detect_gaps(self, logic_features):
        gaps = []

        if logic_features.get("base_case_missing"):
            gaps.append("Recursion Base Case")

        return gaps

    def get_micro_lessons(self, gaps):
        lessons = []
        for gap in gaps:
            lessons.extend(self.micro_lessons.get(gap, []))
        return lessons
