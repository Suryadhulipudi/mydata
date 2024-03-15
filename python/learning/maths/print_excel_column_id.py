def print_excel_column_id(column_number):
    # Initialize an empty string to store the column ID
    column_id = ""

    # Iterate through the column number
    while column_number > 0:
        # Calculate the remainder when dividing by 26
        remainder = (column_number - 1) % 26

        # Convert the remainder to corresponding character and add to column ID
        column_id = chr(65 + remainder) + column_id

        # Update column number for the next iteration
        column_number = (column_number - 1) // 26

    return column_id

# Example usage
column_number = 702  # Change this to test different column numbers
print("Excel Column ID:", print_excel_column_id(column_number))
