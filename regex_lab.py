#!/usr/bin/env python3
"""
Regex Lab
Bryce Coleman
"""
import re
import sys


# -------------------------
# Challenge 1: Validate IPv4 Address
# -------------------------
def is_valid_ipv4(ip):
    octet = r"(25[0-5]|2[0-4]\d|1?\d?\d)"
    pattern = rf"^{octet}\.{octet}\.{octet}\.{octet}$"
    return re.match(pattern, ip) is not None


# -------------------------
# Challenge 2: Extract Dates
# -------------------------
def extract_dates(text):
    pattern = r"\b(\d{2})[/-](\d{2})[/-](\d{4})\b"
    return re.findall(pattern, text)


# -------------------------
# Challenge 3: Match Hex Colors
# -------------------------
def match_hex_colors(text):
    pattern = r"#?([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b"
    return re.findall(pattern, text)


# -------------------------
# Challenge 4: Parse URLs
# -------------------------
def parse_url(url):
    pattern = (
        r"(?P<protocol>https://|http://)"
        r"(?P<domain>[^/\s]+)"
        r"(?P<path>/[^\?\s]*)?"
        r"\?(?P<query>[^\s]+)"
    )
    match = re.search(pattern, url)
    return match.groupdict() if match else None


# -------------------------
# Challenge 5: Remove HTML Tags
# -------------------------
def remove_html_tags(text):
    return re.sub(r"<[^>]+>", "", text)


# -------------------------
# Challenge 6: Validate Password
# -------------------------
def is_valid_password(password):
    pattern = (
        r"^(?=.*[a-z])"
        r"(?=.*[A-Z])"
        r"(?=.*\d)"
        r"(?=.*[^A-Za-z0-9])"
        r"\S{8,}$"
    )
    return re.match(pattern, password) is not None

    
# -------------------------
# Challenge 7: Find Duplicated Words
# -------------------------
def find_duplicated_words(text):
    pattern = r"\b(\w+)\b\s+\1\b"
    return [m.group(1) for m in re.finditer(pattern, text, re.IGNORECASE)]


# -------------------------
# Challenge 8: Extract Nested Parentheses
# -------------------------
def extract_innermost(text):
    pattern = r"\(([^()]+)\)"
    matches = re.findall(pattern, text)
    return matches[-1] if matches else None


# -------------------------
# Challenge 9: Match Balanced Brackets
# -------------------------
def is_balanced_brackets(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# -------------------------
# Challenge 10: Emulate Calculator Parser
# -------------------------
def tokenize_calc(expression):
    pattern = r"\d+|[+\-*/()]"
    return re.findall(pattern, expression)


# -------------------------
# Test Scenarios (Provided)
# -------------------------
def run_one(n: int):
    if n == 1:
        print("Challenge 1: IPv4")
        print(is_valid_ipv4("192.168.1.1"))  # True
        print(is_valid_ipv4("256.0.0.1"))    # False
        print(is_valid_ipv4("192.168.1"))    # False

    elif n == 2:
        print("Challenge 2: Dates")
        text = "Meeting on 12/25/2023 and 01-01-2024"
        print(extract_dates(text))  # [('12','25','2023'), ('01','01','2024')]

    elif n == 3:
        print("Challenge 3: Hex Colors")
        text = "#FF00AA #F0A #GGGGGG"
        print(match_hex_colors(text))  # ['FF00AA', 'F0A']

    elif n == 4:
        print("Challenge 4: URL Parsing")
        url = "https://example.com/path?query=val"
        print(parse_url(url))

    elif n == 5:
        print("Challenge 5: HTML Tags")
        text = "<p>Hello <b>World</b></p>"
        print(remove_html_tags(text))  # Hello World

    elif n == 6:
        print("Challenge 6: Password")
        print(is_valid_password("Passw0rd!"))  # True
        print(is_valid_password("password"))   # False

    elif n == 7:
        print("Challenge 7: Duplicated Words")
        text = "This is is a test test case"
        print(find_duplicated_words(text))  # ['is', 'test']

    elif n == 8:
        print("Challenge 8: Nested Parentheses")
        text = "outer(inner(more parens))"
        print(extract_innermost(text))  # more

    elif n == 9:
        print("Challenge 9: Balanced Brackets")
        print(is_balanced_brackets("([{}])"))  # True
        print(is_balanced_brackets("([)]"))    # False

    elif n == 10:
        print("Challenge 10: Calculator Tokens")
        expr = "2 + 3 * (4 - 1)"
        print(tokenize_calc(expr))  # ['2','+','3','*','(','4','-','1',')']

    else:
        print("Invalid challenge number. Use 1-10.")


def run_tests():
    # runs everything (useful if you want one big screenshot)
    for i in range(1, 11):
        print()  # blank line between challenges
        run_one(i)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        run_one(int(sys.argv[1]))
    else:
        run_tests()
