

class Student:
    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort
        self._phrase = "I can talk!"
        

    def talk(self):
        return self._phrase

    def say_favourite_language(self, language):
        return f"I love {language}"