#!/usr/bin/env python3
# =========================
# Part 3: Advanced Regular Expressions
# =========================

import re

# 3.1 Groups and Capturing
pattern = r"(\d{3})-(\d{2})-(\d{4})"
match = re.search(pattern, "123-45-6789")

if match:
    print(match.group(1))   # 123
    print(match.groups())   # ('123', '45', '6789')

# Named groups example (mentioned in notes)
named_pattern = r"(?P<area>\d{3})-(?P<mid>\d{2})-(?P<last>\d{4})"
named_match = re.search(named_pattern, "123-45-6789")
if named_match:
    print(named_match.group("area"))  # 123
    print(named_match.groupdict())    # {'area': '123', 'mid': '45', 'last': '6789'}


# 3.2 Lookahead and Lookbehind
# Example: Match "foo" only if followed by "bar"
print(re.search(r"foo(?=bar)", "foobar"))  # Matches "foo"
print(re.search(r"foo(?=bar)", "foobaz"))  # No match (None)

# (Extra quick demos for the bullet list)
# Negative lookahead: "foo" not followed by "bar"
print(re.search(r"foo(?!bar)", "foobaz"))  # Matches "foo"
print(re.search(r"foo(?!bar)", "foobar"))  # None

# Lookbehind: match "bar" only if preceded by "foo"
print(re.search(r"(?<=foo)bar", "foobar"))  # Matches "bar"


# 3.3 Flags and Substitution
# Flags: case-insensitive matching
print(re.search(r"hello", "HELLO", re.IGNORECASE))  # Match object (not None)

# re.sub(): Replace matches
text = "Hello, world!"
new_text = re.sub(r"world", "Python", text)
print(new_text)  # "Hello, Python!"


# 3.4 Compilation
# For efficiency: compile once, use many times
regex = re.compile(r"\d{3}-\d{2}-\d{4}")
print(regex.search("SSN: 123-45-6789"))  # Match object

# Exercise (3.4): Use re.sub() to replace all digits in a string with "*".
sample = "Call me at 404-555-1234 on 2/6/2026."
masked = re.sub(r"\d", "*", sample)
print(masked)
