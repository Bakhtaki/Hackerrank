#!/bin/python3

import os
from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#


def acmTeam(topic):
    # Write your code here
    all_teams = combinations(topic, 2)
    max_team_score = []

    for team in all_teams:
        team_score = 0
        for i in range(len(team[0])):
            if team[0][i] == '1' or team[1][i] == '1':
                team_score += 1
        max_team_score.append(team_score)

    max_scores = max(max_team_score)
    count_max_scores = max_team_score.count(max_scores)

    return max_scores, count_max_scores


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
