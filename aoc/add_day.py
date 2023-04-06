import pathlib
from os import getenv, makedirs, path
from textwrap import wrap
from datetime import datetime

import requests
from bs4 import BeautifulSoup, element
from dotenv import load_dotenv

load_dotenv()
SESSION_COOKIE = getenv("SESSION")


def add_day(day: int, year: int) -> None:
    challenge = get_challenge_md(day, year)
    title = extract_challenge_name(challenge, day)

    dir_name = f"{day:02d}- Day - {title}"
    dir_path = str(pathlib.Path(__file__).parent.resolve().parent.absolute()) + f"/{year}/{dir_name}/"
    makedirs(dir_path, exist_ok=True)

    create_file(dir_path + "input.txt", get_puzzle_input(day, year))
    create_file(dir_path + "challenge.md", challenge)

    # add_day can also be called in order to update the input file or the challenge.md file -> don't override file
    if not path.exists(dir_path + "original.py"):
        template = open("templates/original_template.py").read()
        template = template.replace("%d", f'"{day}"')
        template = template.replace("%y", f'"{year}"')
        create_file(dir_path + "original.py", template)

    if not path.exists(dir_path + "solution.py"):
        create_file(dir_path + "solution.py", open("templates/solution_template.py").read())


def get_challenge_md(day: int, year: int) -> str:
    """Returns the Challenge in markdown syntax
        ---
        MIT License
        Copyright (c) 2019 António Ramadas
        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:
        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.
        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        ---
        This function is basically copied from https://github.com/antonio-ramadas/aoc-to-markdown
        """

    # Simplification of https://github.com/dlon/html2markdown/blob/master/html2markdown.py
    def html_tags_to_markdown(tag: element.Tag, is_first_article: bool) -> None:
        """
        Converts tags in html content to markdown tags
        """
        children = tag.find_all(recursive=False)
        if tag.name != "code":
            for child in children:
                html_tags_to_markdown(child, is_first_article)
        if tag.name == "h2":
            tag.insert_before(f"{'#' if is_first_article else '##'} ")
            tag.insert_after("\n\n")
            tag.unwrap()
        elif tag.name == "p":
            tag.insert_after("\n")
            tag.unwrap()
        elif tag.name == "em":
            style = "**" if tag.has_attr("class") and tag["class"] == "star" else "*"
            tag.insert_before(style)
            tag.insert_after(style)
            tag.unwrap()
        elif tag.name == "a":
            tag.insert_before("[")
            tag.insert_after(f"]({tag['href']})")
            tag.unwrap()
        elif tag.name == "span":
            tag.insert_before("*")
            tag.insert_after("*")
            tag.unwrap()
        elif tag.name == "ul":
            tag.unwrap()
        elif tag.name == "li":
            tag.insert_before(" - ")
            tag.insert_after("\n")
            tag.unwrap()
        elif tag.name == "code":
            if "\n" in tag.text:
                tag.insert_before("```\n")
                tag.insert_after("\n```")
            else:
                tag.insert_before("`")
                tag.insert_after("`")
            tag.unwrap()
        elif tag.name == "pre":
            tag.insert_before("")
            tag.insert_after("\n")
            tag.unwrap()
        elif tag.name == "article":
            pass
        else:
            raise ValueError(f"Missing condition for tag: {tag.name}")

    res = requests.get(f"https://adventofcode.com/{year}/day/{day}", cookies={"session": SESSION_COOKIE})
    if res.ok:
        soup = BeautifulSoup(res.text, features="html.parser")
        articles = soup.body.main.findAll("article", recursive=False)
        content = ""
        # Convert the tags with given function
        for i, article in enumerate(articles):
            html_tags_to_markdown(article, i == 0)
            content += "".join([tag.string for tag in article.contents])
        # User wrap method to make line breaks after 120 chars
        result = ""
        for line in content.split("\n"):
            result += "\n".join(wrap(line, 120, break_long_words=True, break_on_hyphens=False)) + "\n"
        return result
    print(f"Challenge could not be fetched! Code: {res.code}")
    return ""


def extract_challenge_name(challenge_md: str, day: int) -> str:
    if challenge_md:
        title = challenge_md.split("\n")[0]
        title = title.replace(f"# --- Day {day}: ", "")[:len(title) - 4]
        return title
    else:
        print("Name could not be extracted, because the text passed was empty!")
        return ""


def get_puzzle_input(day: int, year: int) -> str:
    res = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": SESSION_COOKIE})

    if res.ok:
        return res.text

    print(f"Input could not be fetched! Code: {res.status_code}")
    return ""


def create_file(file_path: str, content: str) -> None:
    with open(file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    if datetime.now().month == 12 and 1 <= datetime.now().day <= 25:
        add_day(datetime.now().day, datetime.now().year)
    else:
        add_day(1, 2020)
