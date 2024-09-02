import os

def get_env_var(var_name):
    """Read the environment variable."""
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable {var_name} not found.")
    return value

def convert_name_to_uppercase(name):
    """Convert the name to uppercase."""
    return name.upper()

if __name__ == "__main__":
    # Load environment variables from the .env file
    from dotenv import load_dotenv
    load_dotenv(dotenv_path='secrets-output/name.env')
    
    # Fetch the name from the environment
    name = get_env_var('NAME')
    
    # Convert the name to uppercase
    uppercase_name = convert_name_to_uppercase(name)
    
    # Print the result
    print(f"Original Name: {name}")
    print(f"Uppercase Name: {uppercase_name}")
