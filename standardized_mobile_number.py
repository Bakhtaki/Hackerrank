'''Solution for HackerRank problem "Standardized Mobile Number"'''
# -----------------------------------------------------------------------------
# Task:
# You are given N mobile numbers.Sort them in ascending
# order and print them in the standard format of +91 xxxxx xxxxx.
# the given mobile numbers may have +91 or 91 or 0 written before the
# actual 10 digit number. alternatively,there may not be any prefix at all.
#
# Input Format:
# the first line of input contains an integer N,the number of mobile numbers.
# N lines follow,each containing a mobile number.
#
# Output Format:
# print N mobile numbers on separate lines in the required format.
#
# Sample Input:
# 3
# 07895462130
# 919875641230
# 9195969878
#
# Sample Output:
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230
# -----------------------------------------------------------------------------
# Solution:


def wrapper(f):
    def fun(ph):
        # complete the function
        f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in ph)
    return fun


@wrapper
def sort_phone(ph):
    print(*sorted(ph), sep='\n')


if __name__ == '__main__':
    ph = [input() for _ in range(int(input()))]
    sort_phone(ph)
