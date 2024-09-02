import os



def convert_name_to_uppercase(name):
    """Convert the name to uppercase."""
    
    return name.swapcase()

if __name__ == "__main__":
    # Load environment variables from the .env file
    
    # Fetch the name from the environment
    name = os.getenv('NAME')
    
    # Convert the name to uppercase
    uppercase_name = convert_name_to_uppercase(name)
    
    # Print the result
    print(f"Original Name: {name}")
    print(f"Uppercase Name: {uppercase_name}")
