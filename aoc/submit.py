from os import getenv
from typing import Union

import requests
from dotenv import load_dotenv

load_dotenv()
SESSION_COOKIE = getenv("SESSION")
def submit(answer: Union[int, str], part: int, day: int, year: int, auto_submit: bool = False):
    res = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", cookies={"session": SESSION_COOKIE},
                        data={"level": part, "answer": str(answer)})
    lower_case_res = res.text.lower()
    if "that's the right answer" in lower_case_res:
        print(f"Part {part} of day {day} of year {year} is correct!")
        if auto_submit and day == 25 and part == 1:
            print("It's Christmas! The second part will be automatically submitted!")
            submit(0, 2, 25, year, True)
    elif "did you already complete it?" in lower_case_res:
        print("Already completed!")
    elif "that's not the right answer" in lower_case_res or "you gave an answer too recently" in lower_case_res:
        if "your answer is too low" in lower_case_res:
            print("Your answer is False! Hint: Answer too low")
        if "your answer is too high" in lower_case_res:
            print("Your answer is False! Hint: Answer too high")
        if "you have to wait after" in lower_case_res or "you gave an answer too recently" in lower_case_res:
            matches = compile(r'please wait ([\w ]+) before trying again.').findall(res.text)
            matches += compile(r'have ([\w ]+) left to wait').findall(res.text)
            if matches:
                print(f"Submission to fast! There are {matches[0]} left to wait.")
            else:
                print("Submission to fast!")
    else:
        print("Could not detect submission state!\n\n\n")
        print(res.text)
