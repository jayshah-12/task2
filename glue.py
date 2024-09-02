import argparse

def convert_name_to_uppercase(name):
    """Convert the name to uppercase."""
    return name.swapcase()

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert a name to uppercase.")
    parser.add_argument("--name", required=True, help="Name to be converted to uppercase")

    # Parse the arguments
    args = parser.parse_args()

    # Fetch the name from the arguments
    name = args.name

    # Convert the name to uppercase
    uppercase_name = convert_name_to_uppercase(name)
    
    # Print the result
    print(f"Original Name: {name}")
    print(f"Uppercase Name: {uppercase_name}")
