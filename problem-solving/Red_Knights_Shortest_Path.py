
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Write your code here
    # Destination
    end = (i_end, j_end)
    # Visited
    visited = set()
    # Add start to visited
    visited.add((i_start, j_start))
    # stack
    stack = [(i_start, j_start, '')]
    # Step Counter
    step_counter = 0
    # Directions
    directions = [('UL', -2, -1), ('UR', -2, 1),
                  ('R', 0, 2), ('LR', 2, 1),
                  ('LL', 2, -1), ('L', 0, -2)]

    # While stack is not empty and end is not in visited
    while stack:
        step_counter += 1
        stack_size = len(stack)
        while stack_size > 0:
            stack_size -= 1  # Decrement stack size
            x, y, path = stack.pop(0)  # Pop from stack
            for direction, dx, dy in directions:
                new_x, new_y = x + dx, y + dy  # Get new coordinates
                if (new_x, new_y) == end:
                    print(step_counter)  # Print step counter
                    path += " " + direction  # Add direction to path
                    print(path[:1])  # Remove first space
                    return
                if 0 <= new_x < n and 0 <= new_y < n and \
                        (new_x, new_y) not in visited:
                    stack.append((new_x, new_y, path + ' ' + direction))
                    visited.add((new_x, new_y))  # Add to visited
    print('Impossible')


if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
