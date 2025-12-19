class CodingEvaluator:
    def evaluate(self, user_code, exercise):
        logic_features = {
            "base_case_missing": False,
            "uses_loop_instead_of_recursion": False
        }

        correct = False

        if "recursion" in exercise["concepts"]:
            if "def" in user_code and exercise["function_name"] in user_code:
                if "return" in user_code:
                    if exercise["base_case"] not in user_code:
                        logic_features["base_case_missing"] = True
                    else:
                        correct = True

        return {
            "correct": correct,
            "logic_features": logic_features
        }
