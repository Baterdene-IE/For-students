#!/bin/python3

""" Даалгавар №3 """

from random import randrange, choices, choice
class Name:
    def __init__(self, *args, **kwargs):
        self.fnames = args[0]
        self.lnames = args[1]
    def create(self):
        return choice(self.fnames) + " " + choice(self.lnames) 
class Skill:
    def __init__(self, *args, **kwargs):
        self.skills = kwargs["skills"]
    def collect(self):
        return set(choices(self.skills, k = randrange(1, len(self.skills)-1)))
if __name__ == '__main__':
    my_dict = {
                "fnames": ["Baterdene", "John", "Albert", "Steve"],
                "lnames": ["Borjigin", "Doe", "Einstein", "Jobs"],
                "skills": ["Python", "Java", "Javascript", "C++", "C#", "PHP", "Go", "R", "Ruby"]
            }
    my_name = Name(my_dict["fnames"], my_dict["lnames"])
    my_skill = Skill(skills = my_dict["skills"])
    print("Hello, My name is", my_name.create(), end=".\n")
    print("I'm skilled in", ", ".join(my_skill.collect()), end=".\n")