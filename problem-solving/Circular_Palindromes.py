#!/bin/python3

import os
#
# Complete the circularPalindromes function below.
#


def circularPalindromes(s):
    #
    # Write your code here.
    #
    os = []
    ocs = []
    es = []
    ecs = []
    l = len(s)
    b = 3 * s
    curchar = '\0'
    curstart = 0
    curcount = 0
    triplets = []
    for i, c in enumerate(b):
        if not i:
            curstart = 0
            curcount = 1
            curchar = c
        else:
            if c == curchar:
                curcount += 1
            else:
                for j in range(curcount):
                    triplets.append((curchar, curcount, curstart))
                curstart = i
                curcount = 1
                curchar = c
    for i in range(curcount):
        triplets.append((curchar, curcount, curstart))
    for i in range(l):
        center = l + i
        o = -1
        if triplets[center][1] % 2\
                and center == triplets[center][2] + triplets[center][1] // 2:
            ociinner = triplets[center][1]
            ocicenter = i
            o = triplets[center][1]
            p1 = triplets[center][2] - 1
            p2 = triplets[center][2] + triplets[center][1]
            while p1 >= 0 and p2 < 3 * l and\
                    triplets[p1][0] == triplets[p2][0]:
                if triplets[p1][1] != triplets[p2][1]:
                    o += 2 * min(triplets[p1][1], triplets[p2][1])
                    break
                o += 2 * triplets[p1][1]
                p1 -= triplets[p1][1]
                p2 += triplets[p2][1]
            ocitotal = o
            ocs.append((ocitotal, ocicenter, ociinner))
        else:
            o = 1 + 2 * min(center-triplets[center][2], triplets[center]
                            [2] + triplets[center][1] - 1 - center)
        os.append(min(l, o))

        e = 0
        if triplets[center][1] % 2 == 0 and\
                center == triplets[center][2] + triplets[center][1]//2:
            eciinner = triplets[center][1]
            ecicenter = i
            e = triplets[center][1]
            p1 = triplets[center][2] - 1
            p2 = triplets[center][2] + triplets[center][1]
            while p1 >= 0 and p2 < 3 * l\
                    and triplets[p1][0] == triplets[p2][0]:
                if triplets[p1][1] != triplets[p2][1]:
                    e += 2*min(triplets[p1][1], triplets[p2][1])
                    break
                e += 2 * triplets[p1][1]
                p1 -= triplets[p1][1]
                p2 += triplets[p2][1]
            ecitotal = e
            ecs.append((ecitotal, ecicenter, eciinner))
        else:
            e = 2 + 2 * min(center - 1 - triplets[center][2],
                            triplets[center][2] +
                            triplets[center][1] - 1 - center)
        es.append(min(l, e))

    rocs = sorted(ocs, key=lambda x: x[0], reverse=True)

    recs = sorted(ecs, key=lambda x: x[0], reverse=True)
    bests = []
    if l % 2:
        bests = [max(os[(i + l // 2) % l], min(l - 1, max(es[(i + l // 2) %
                     l], es[(i + l // 2 + 1) % l]))) for i in range(l)]
    else:
        bests = [max(es[(i + l // 2) % l], min(l - 1, max(os[(i + l // 2) %
                     l], os[(i+l//2-1) % l]))) for i in range(l)]

    for i in range(l):
        top = bests[i]
        rosi = 0
        while(rosi < len(rocs) and rocs[rosi][0] > top):
            centerresult = min(
                rocs[rosi][0], 1 + 2 * min((rocs[rosi][1] - i) % l,
                                           (i - 1 - rocs[rosi][1]) % l))
            if centerresult < rocs[rosi][2]:
                centerresult = min(rocs[rosi][2], max(
                    (i - (rocs[rosi][1] - rocs[rosi][2]//2)) % l,
                    (rocs[rosi][1] + rocs[rosi][2] // 2 + 1 - i) % l))
            top = max(top, min(centerresult, l))
            rosi += 1
        resi = 0
        while(resi < len(recs) and recs[resi][0] > top):
            centerresult = min(
                recs[resi][0], 2 * min((recs[resi][1]-i) % l,
                                       (i - recs[resi][1]) % l))
            if centerresult < recs[resi][2]:
                centerresult = min(recs[resi][2], max(
                    (i - (recs[resi][1] - recs[resi][2]//2)) % l,
                    (recs[resi][1] + recs[resi][2] // 2 - i) % l))
            top = max(top, min(centerresult, l))
            resi += 1
        bests[i] = top
    return bests


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = circularPalindromes(s)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
