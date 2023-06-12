def divide_keyspace(start, end, num_ranges):
    # Convert start and end keyspaces from hexadecimal to integer
    start_int = int(start, 16)
    end_int = int(end, 16)

    # Calculate the range size
    range_size = (end_int - start_int) // num_ranges

    ranges = []
    current = start_int

    # Divide the keyspace into equal ranges
    for i in range(num_ranges):
        # Calculate the end value for the current range
        range_end = current + range_size - 1

        # Convert the start and end values to hexadecimal strings
        start_hex = hex(current)[2:]
        end_hex = hex(range_end)[2:]

        # Append the range to the list
        ranges.append(f"{start_hex}:{end_hex}")

        # Update the current value for the next iteration
        current = range_end + 1

    return ranges


# Get user inputs
start_range = input("Enter the starting keyspace range: ")
end_range = input("Enter the ending keyspace range: ")
num_ranges = int(input("Enter the number of equal divided ranges: "))

# Divide the keyspace
ranges = divide_keyspace(start_range, end_range, num_ranges)

# Write the ranges to a text file
with open("keyspace_ranges.txt", "w") as file:
    file.write("\n".join(ranges))

print("Key space ranges have been written to 'keyspace_ranges.txt'.")
