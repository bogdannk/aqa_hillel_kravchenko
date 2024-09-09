from pathlib import Path
import csv
import json
import logging
import xml.etree.ElementTree as ET

# Paths to directory with my CSV files
base_path = Path('ideas_for_test/work_with_csv')
first_file = base_path / 'r-m-c.csv'
second_file = base_path / 'rmc.csv'
result_file = base_path / 'result_KRAVCHENKO.csv'


"""Delete duplicates from CSV file."""
def remove_duplicates_in_file(file_path):
    unique_rows = set()
    with file_path.open('r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            unique_rows.add(tuple(row))
    return unique_rows

"""Combine two CSV files and remove duplicates."""
def combine_and_remove_duplicates(first_file, second_file, result_file_with_out_duplicates):
    unique_rows = remove_duplicates_in_file(first_file)
    unique_rows.update(remove_duplicates_in_file(second_file))

    with result_file_with_out_duplicates.open('w', newline='') as result:
        writer = csv.writer(result)
        for row in unique_rows:
            writer.writerow(row)

"""Perform the task"""
combine_and_remove_duplicates(first_file, second_file, result_file)

"""FIRST SOLUTION"""

"""Path to directory with JSON and log file"""
jsons_directory = Path('ideas_for_test/work_with_json')
my_log_file = jsons_directory / 'json__KRAVCHENKO.log'

"""Creating and configurea logger"""
logger_for_json = logging.getLogger("My logger for JSON")
logger_for_json.setLevel(logging.ERROR)
file_handler = logging.FileHandler(my_log_file)
file_handler.setLevel(logging.ERROR)
logger_for_json.addHandler(file_handler)

"""Validate all JSON files in the directory and log errors."""
def validate_the_json_files(directory):
    for json_file in directory.iterdir():
        if json_file.suffix == '.json':
            try:
                with json_file.open('r') as file:
                    json.load(file)
            except json.JSONDecodeError as e:
                logger_for_json.error(f"The invalid JSON is located in the file {json_file.name}: {e}")

"""Perform the task"""
validate_the_json_files(jsons_directory)



"""SECOND SOLUTION"""

# """Path to directory with JSON and log file"""
# jsons_directory = Path('ideas_for_test/work_with_json')
# my_log_file = jsons_directory / 'json__KRAVCHENKO.log'
#
# """Creating and configuring a logger"""
# logging.basicConfig(filename=my_log_file, level=logging.ERROR)
# logger_for_json = logging.getLogger("My logger for JSON")
#
# """Validate all JSON files in the directory and logging errors."""
# def validate_the_json_files(directory):
#
#     for json_file in directory.iterdir():
#         if json_file.suffix == '.json':
#             try:
#                 with json_file.open('r') as file:
#                     json.load(file)
#             except json.JSONDecodeError as e:
#                 logger_for_json.error(f"The invalid JSON is located in the file {json_file.name}: {e}")
#
# """Perform the task"""
# validate_the_json_files(jsons_directory)





"""Path to directory with XML file"""
my_xml_file = Path('ideas_for_test/work_with_xml/groups.xml')

"""Configure logging to output to console"""
logging.basicConfig(level=logging.INFO)
logger_for_xml = logging.getLogger("My logger for XML")

"""Search for a specific group number in the XML and log the incoming value."""
def search_number_group_in_xml(xml_file, group_number):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number').text
        if number == group_number:
            incoming = group.find('timingExbytes/incoming').text
            logger_for_xml.info(f"Found incoming value for group {group_number}: {incoming}")
            return incoming
    logger_for_xml.info(f"Group number {group_number} doesn't exist in XML.")
    return None


"""Perform the task"""
search_number_group_in_xml(my_xml_file, '3')