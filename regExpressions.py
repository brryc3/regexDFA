#!/usr/bin/env python3
# =========================
# Part 2: Regular Expressions Basics
# =========================

import re

# 2.1 Importing and Basic Matching
# Example from lab:
text = "The rain in Spain"
match = re.search("rain", text)
if match:
    print("Found:", match.group())  # Found: rain

# Exercise (2.1): Search for "cat" in "The cat sat on the mat." using re.search()
text2 = "The cat sat on the mat."
match2 = re.search("cat", text2)
if match2:
    print("Found:", match2.group())
else:
    print("Not found")


# 2.2 Metacharacters
# Example from lab (SSN pattern):
pattern_ssn = r"\d{3}-\d{2}-\d{4}"   # SSN format like 123-45-6789
text_ssn = "My SSN is 123-45-6789"

# re.match checks from the START of the string, so this will usually be False here.
# The lab screenshot uses re.match; we’ll keep it as-is.
if re.match(pattern_ssn, text_ssn):
    print("Valid SSN (match at start)")
else:
    print("SSN pattern not at start (re.match failed)")

# If you actually want to find it anywhere in the string, use re.search:
if re.search(pattern_ssn, text_ssn):
    print("Valid SSN (found with search)")


# Exercise (2.2): Write a regex to match emails like "user@example.com"
# Basic version given: \w+@\w+\.\w+
email_pattern = r"\w+@\w+\.\w+"

tests = [
    "user@example.com",
    "my_email123@school.edu",
    "not an email",
    "bad@email",
    "a@b.c",
]

for t in tests:
    if re.fullmatch(email_pattern, t):
        print("Valid email:", t)
    else:
        print("Invalid email:", t)
