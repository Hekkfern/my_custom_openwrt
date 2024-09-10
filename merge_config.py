#!/usr/bin/env python3

import argparse

def parse_config(file_path):
    config = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            if line.startswith('#'):
                # Check if it's in the form "# CONFIG_X is not set"
                if 'is not set' in line:
                    key = line.split()[1]
                    config[key] = 'n'
            else:
                key, value = map(str.strip, line.split('=', 1))
                config[key] = value
    return config

def write_config(config, output_file):
    with open(output_file, 'w') as f:
        for key, value in config.items():
            if value == 'n':
                f.write(f"# {key} is not set\n")
            else:
                f.write(f"{key}={value}\n")

def merge_configs(full_config, changes_config):
    # Apply changes from the second config
    for key, value in changes_config.items():
        if value == 'n':
            # Set the value as commented out (not set)
            full_config[key] = 'n'
        elif value == 'y':
            # Set the value as enabled
            full_config[key] = 'y'
    return full_config

def main():
    parser = argparse.ArgumentParser(description='Merge two OpenWRT configurations.')
    parser.add_argument('full_config', help='Path to the full configuration file.')
    parser.add_argument('changes_config', help='Path to the configuration file with changes.')
    parser.add_argument('output_file', help='Path to save the merged configuration file.')

    args = parser.parse_args()

    # Parse the full config and the changes config
    full_config = parse_config(args.full_config)
    changes_config = parse_config(args.changes_config)

    # Merge configurations
    merged_config = merge_configs(full_config, changes_config)

    # Write the merged configuration to the output file
    write_config(merged_config, args.output_file)

if __name__ == '__main__':
    main()
