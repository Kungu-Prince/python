def main():
    # i. Prompt the user to enter their birth year.
    birth_year = input("Enter your birth year: ")

    # ii. Calculate their age based on the entered birth year.
    current_year = 2024  # Assuming the current year is 2024
    try:
        birth_year = int(birth_year)
        age = current_year - birth_year
    except ValueError:
        print("Invalid input. Please enter a valid birth year.")
        return

    # iii. Ask the user to provide their height in meters.
    height = input("Enter your height in meters (e.g., 1.75): ")

    try:
        height = float(height)
    except ValueError:
        print("Invalid input. Please enter a valid height.")
        return

    # iv. Determine the data type of each input and display it.
        print(f"\nData types:")
    birth_year_type = type(birth_year).__name__
    print(f"Birth Year: {birth_year_type}")
    age_type = type(age).__name__
    print(f"Age: {age_type}")
    height_type = type(height).__name__
    print(f"Height: {height_type}")

    # v. Determine the size of each input and display it.
    print(f"\nObject sizes (in bytes):")
    birth_year_size = get_object_size(birth_year)
    print(f"Birth Year: {birth_year_size}")
    age_size = get_object_size(age)
    print(f"Age: {age_size}")
    height_size = get_object_size(height)
    print(f"Height: {height_size}")


def get_object_size(obj):
    """Getting the size of an object in bytes."""
    import sys
    return sys.getsizeof(obj)


if __name__ == "__main__":
    main()
