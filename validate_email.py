'''Solution to the challenge "Validate Email" from the "Python Challenge'''

# ---------------------------------------------------------------
# You are given an integer N.followed by N email addresses.
# Yoy are required to print the valid email addresses in the
# order lexicographically.
#
# Valid email addresses must follow the following rules:
# it must have the username@websitename.extension format.
# the username cat only contains letters, digits, dashes and underscores.
# [a-z],[A-Z],[0-9],[_],[-]
# the username must be at least one character.
# the websitename can only contain letters, digits
# [a-z],[A-Z],[0-9]
# the extension can only contain letters.
# [a-z],[A-Z]
# the maximum length of the extension is 3.
# input format:
# 3
# lara@hackerrank.com
# brian-23@hackerrank.com
# britts_54@hackerrank.com
# ---------------------------------------------------------------
import re

def fun(s):
    # return True if s is valid email address, else False
    return re.match(r'^[a-zA-Z0-9_\-]{1,}@[a-zA-Z0-9]{1,}\.[a-zA-Z]{1,3}$',s)

def filter_mail(emails):
    return list(filter(fun,emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
