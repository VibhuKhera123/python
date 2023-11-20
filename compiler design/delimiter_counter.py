def count_delimiters(input_string, delimiters):
    delimiter_counts = {}

    for char in input_string:
        if char in delimiters:
            if char in delimiter_counts:
                delimiter_counts[char] += 1
            else:
                delimiter_counts[char] = 1

    return delimiter_counts

def main():
    # Set of delimiters
    delimiter_set = set([';', ',', ':', '|', '-','(',')','!','$'])

    # Get user input
    input_string = input("Enter a string: ")

    # Call the count_delimiters function
    result = count_delimiters(input_string, delimiter_set)

    # Display the result
    print("Delimiter counts:")
    for delimiter, count in result.items():
        print(f"{delimiter}: {count}")

if __name__ == "__main__":
    main()
