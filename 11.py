def _find_largest_set(grid):
    largest_set = []
    largest_product = 0
    grid_length = len(grid)
    last_row = grid_length - 4
    for row_index in range(grid_length):
        row = grid[row_index]
        row_length = len(row)
        first_index = 3
        last_index = row_length - 4
        row = grid[row_index]
        for num_index in range(row_length):
            current_sets = []
            current_products = []
            if num_index <= last_index:
                current_set = []
                current_product = 1
                for current_num_index in range(num_index, num_index+4):
                    current_num = row[current_num_index]
                    current_set.append(current_num)
                    current_product *= current_num
                current_sets.append(current_set)
                current_products.append(current_product)
            if row_index <= last_row:
                current_set = []
                current_product = 1
                for current_row_index in range(row_index, row_index+4):
                    current_num = grid[current_row_index][row_index]
                    current_set.append(current_num)
                    current_product *= current_num
                current_sets.append(current_set)
                current_products.append(current_product)
            if num_index >= first_index and row_index <= last_row:
                current_set = []
                current_product = 1
                for current_num_index, current_row_index in zip(range(num_index, num_index-4, -1), range(row_index, row_index+4)):
                    current_num = grid[current_row_index][current_num_index]
                    current_set.append(current_num)
                    current_product *= current_num
                current_sets.append(current_set)
                current_products.append(current_product)
            if num_index <= last_index and row_index <= last_row:
                current_set = []
                current_product = 1
                for current_num_index, current_row_index in zip(range(num_index, num_index+4), range(row_index, row_index+4)):
                    current_num = grid[current_row_index][current_num_index]
                    current_set.append(current_num)
                    current_product *= current_num
                current_sets.append(current_set)
                current_products.append(current_product)
            for product_index in range(len(current_products)):
                product = current_products[product_index]
                if product > largest_product:
                    largest_product = product
                    largest_set = current_sets[product_index]
    print largest_set
    return largest_product

def find_largest_set():
    sets = []
    with open('11.txt') as f:
        for line in f.readlines():
            a_set = []
            for num in line.strip().split():
                a_set.append(int(num))
            sets.append(a_set)
    return _find_largest_set(sets)

if __name__ == '__main__':
    print find_largest_set()

