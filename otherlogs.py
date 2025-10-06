import re

def extract_device_ids(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove all whitespace characters (including newlines)
    content = re.sub(r'\s', '', content)
    
    # Find all device IDs using regex pattern
    device_ids = re.findall(r'[0-9a-z]{56}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}', content, re.IGNORECASE)

    # Pattern 2: Device IDs ending with "none" (no hyphens)
    #device_ids = re.findall(r'[0-9a-z]+none', content, re.IGNORECASE)
    
    # Write device IDs to output file
    with open(output_file, 'w') as f:
        for device_id in device_ids:
            f.write(device_id + '\n')

# Usage
extract_device_ids('deviceIds.txt', 'output_device_ids.txt')

