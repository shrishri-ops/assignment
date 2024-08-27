"""
This script takes the config.init file directory path and get the output in string format
"""

import configparser
import os



def parse_config(config_file_path):
    """
    This function uses configparser module to read the config.init data file and parsed the data 
    in a variable data
    
    """
    config = configparser.ConfigParser()
    config_data = {}

    try:
        # Check if the file exists
        if not os.path.isfile(config_file_path):
            raise FileNotFoundError(f"The file '{config_file_path}' does not exist.")

        # Read the configuration file
        config.read(config_file_path)

        # Check if the file was successfully parsed
        if not config.sections():
            raise ValueError(f"The file '{config_file_path}' does not appear \
                             to be a valid configuration file or is empty.")

        # Extract sections and key-value pairs
        for section in config.sections():
            config_data[section] = dict(config.items(section))

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return config_data

# Example usage
if __name__ == "__main__":
    try:
        # Prompt the user to input the file path
        file_path = input("Please enter the path to the configuration file: ").strip()

        # Handle empty input
        if not file_path:
            raise ValueError("File path cannot be empty.")

        # Parse the config file using the function parse_config
        configuration_data = parse_config(file_path)

        # If config_data is empty, it indicates that an error occurred
        if configuration_data:
            print("Configuration Data:", configuration_data)
        else:
            print("No configuration data found.")

    except ValueError as input_err:
        print(input_err)
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
    except Exception as unexpected_err:
        print(f"An unexpected error occurred: {unexpected_err}")
