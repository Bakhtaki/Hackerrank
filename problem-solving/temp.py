# Define Binary Index tree]

class BIT:
    def __init__(self, array: list[int]):
        self.bit = [0] * (len(array) + 1)
        self.size = len(array)

        # Fill Empty BIT with array values
        for index in range(self.size):
            self.build(index + 1, array[index])

    # Build BIT
    def build(self, index: int, value: int):
        while index <= self.size:
            self.bit[index] += value
            index += index & (-index)

    # Update BIT
    def update(self, index: int, value: int):
        index += 1
        while index <= self.size:
            self.bit[index] -= value
            index += index & (-index)

    # Get sum of range [0, index]
    def get_sum(self, index: int):
        index += 1
        sum = 0
        while index > 0:
            sum += self.bit[index]
            index -= index & (-index)
        return sum

    # Get sum of range [left, right]
    def get_range_sum(self, left: int, right: int):
        return self.get_sum(right) - self.get_sum(left - 1)

    # Print BIT
    def print_tree(self):
        print(self.bit)


# Define Main function
def main():
    # Define array
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # Create BIT
    bit = BIT(array)

    # Print BIT
    print("BIT: ")
    bit.print_tree()

    # Total sum of array
    print("Total sum of tree.. ")
    print(bit.get_sum(len(array) - 1))

    # Update BIT
    bit.update(2, 10)

    # Print BIT
    print("BIT: ")
    bit.print_tree()

    # Total sum of array
    print("Total sum of tree after update.. ")
    print(bit.get_sum(len(array) - 1))

    # Get sum of range [3, 6]
    print("Sum of range [3, 6].. ")
    print(bit.get_range_sum(3, 6))


if __name__ == "__main__":
    main()
