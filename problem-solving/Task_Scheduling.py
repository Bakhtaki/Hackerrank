#!/bin/python3
import os

#
# Complete the 'taskScheduling' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER m
#

negative_infinity = float('-inf')


# Define Segment Tree
class SegmentTree:
    """Segment Tree."""

    def __init__(self, left, right, index, value):
        self.lc, self.rc = left, right

        if left is None or right is None:
            # This is leaf Node
            self.interval = (index, index)
            self.max_node = self
        else:
            # this is internal node
            self.interval = (left.interval[0], right.interval[1])

            left_value = value(left.max_node.interval[0])
            right_value = value(right.max_node.interval[0])

            if left_value > right_value:
                self.max_node = left.max_node
            else:
                self.max_node = right.max_node


# Function To Build Segment Tree top-down
def seg_tree_top_down(left, right, value):
    if left == right:
        return SegmentTree(None, None, left, value)
    else:
        mid = (right + 1 - left) / 2 + left - 1
        left_child = seg_tree_top_down(left, mid, value)
        right_child = seg_tree_top_down(mid + 1, right, value)
        return SegmentTree(left_child, right_child, None, value)


# Function To Build updating Segment Tree
def update_seg_tree(root, index, value):
    """Update Segment Tree."""
    node = root
    path = [node]

    while True:
        if node.lc is None:
            # This is leaf Node
            break
        mid_left = node.lc.interval[1]

        # Left Child Bigger than Mid
        if index > mid_left:
            path.append(node.rc)
            node = node.rc
        else:
            path.append(node.lc)
            node = node.lc
    # Update Node
    # prev = None

    # Iterate Backwards
    for node in path[::-1]:
        if node.lc is None:
            # This is leaf Node
            pass
        else:
            left_value = value(node.lc.max_node.interval[0])
            right_value = value(node.rc.max_node.interval[1])

            if (left_value > right_value):
                node.max_node = node.lc.max_node
            else:
                node.max_node = node.rc.max_node


# Define Binary Indexed Tree
class BinaryIndexedTree:
    """BinaryIndexedTree Class."""

    def __init__(self, size=0):
        self.elements = [(0, 0) for _ in range(size)]
        self.size = size

    def calculate(self, index, value):
        """Calculate the value."""
        response = value

        target_index = index - (index & -index) + 1
        i = index - 1

        while i > target_index:
            response += self.elements[i - 1][1]
            i -= (i & -i)
            self.elements[index - 1] = (value, response)

    # Update Binary Indexed Tree
    def update(self, index, value):
        """Update the Binary Indexed Tree."""
        if index > self.size:
            # Fill the rest with 0
            for i in range(self.size, index):
                self.elements.append((0, None))

            # Calculate the new elements
            for i in range(self.size + 1, index + 1):
                self.calculate(i, 0)
        # Update the size
        self.size = index
        old_frequency, response = self.elements[index - 1]
        difference = value - old_frequency
        self.elements[index - 1] = (value, response)
        self._update(index, difference)

    def _update(self, index, difference):
        """Update the Binary Indexed Tree."""
        if difference == 0:
            return
        while index <= self.size:
            frequency, response = self.elements[index - 1]
            self.elements[index - 1] = (frequency, response + difference)
            index += (index & -index)

    # Sum of Binary Indexed Tree
    def sum(self, index):
        """Sum of Binary Indexed Tree."""
        total = 0
        while index > 0:
            total += self.elements[index - 1][1]
            index -= (index & -index)
        return total


class TaskScheduler(object):
    def __init__(self):
        self._task_by_id = []
        self._task_by_rank = []
        # list for map id to rank
        self._id_to_rank_map = []
        # Task Counter
        self.task_counter = 0

    # Add Task
    def add_task(self, task):
        """Each task is a tuple of (id,deadline,duration)"""
        self._task_by_id.append(task)

        # Add to task counter
        self.task_counter += 1

    # Prepare Tasks
    def prepare_tasks(self):
        """Prepares the tasks by deadline and duration."""
        # Sort Tasks by deadline
        self._task_by_id.sort(key=lambda x: x[1])

        # set task rank
        self._task_by_rank = self._task_by_id

        # Delete task_by_id
        del(self._task_by_id)

        # build an index from task id
        self.id_to_rank_map = [None] * self.task_counter

        for i, task in enumerate(self._task_by_rank):
            self._id_to_rank_map[task[0] - 1] = i

        # Initialize the Binary Indexed Tree and segment tree
        self._bit = BinaryIndexedTree(self.task_counter)
        self._seg_tree = seg_tree_top_down(1, self.task_counter,
                                           negative_infinity)

    # Schedule Task
    def schedule_task(self, task_id):
        """Schedules a task."""
        for idx in range(1, self.task_counter + 1):
            # Get the task rank
            rank = self._id_to_rank_map[task_id - 1] + 1
            # Get the task attributes
            deadline, duration = self.task_by_rank[rank - 1][1:]

            # Update the Binary Indexed Tree
            self._bit.update(rank, duration)

            val_chache = {}

            # Define Value_function
            def value_function(node_rank):
                if node_rank in val_chache:
                    return val_chache[node_rank]
                node_index, node_deadline, node_duration \
                    = self.task_by_rank[node_rank - 1]
                if node_index > task_id:
                    result = float('-inf')
                else:
                    result = self._bit.sum(node_rank) - node_deadline
                val_chache[node_rank] = result
                return result

            # Update the Segment Tree
            update_seg_tree(self._seg_tree, rank, value_function)
            # Maximum rank
            max_rank = self._seg_tree.max_node.interval[0]
            max_over = value_function(max_rank)
            if max_over <= 0:
                return max_rank


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    task_scheduler = TaskScheduler()

    t = int(input().strip())

    for t_itr in range(t + 1):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        # Add to Task Queue
        new_task = (t_itr, d, m)
        task_scheduler.add_task(new_task)

        # Prepare Tasks
        task_scheduler.prepare_tasks()

        result = task_scheduler.schedule_task(t_itr + 1)

        fptr.write(str(result) + '\n')

    fptr.close()
