import requests
import re


def return_data_dict():

    url_2000_latest = 'https://raw.githubusercontent.com/kamyu104/LeetCode-Solutions/master/README.md'
    url_0001_1000 = 'https://raw.githubusercontent.com/kamyu104/LeetCode-Solutions/master/0001-1000.md'
    url_1001_2000 = 'https://raw.githubusercontent.com/kamyu104/LeetCode-Solutions/master/1001-2000.md'

    all_url = [url_0001_1000,url_1001_2000,url_2000_latest]

    unprocessed_lines =[]
    

    for url in all_url:
        response = requests.get(url)
        readme_content = response.text
        pattern = re.compile(r'^\d+\s*\|.*$', re.MULTILINE)

        # Find all matches in the content
        matches = pattern.findall(readme_content)

        # Display the matched lines
        for line in matches:
            unprocessed_lines.append(line)
    # print(len(unprocessed_lines))

    processed_dict = []
    # Regex pattern to extract the required fields

    pattern = r'^\s*(\d+)\s*\|\s*\[(.*?)\]\((.*?)\)\s*\|.*?\|\s*([^|]+)\|\s*([^|]+)'
    for line in unprocessed_lines:
        match = re.match(pattern, line)
        if match:
            number = match.group(1)
            name = match.group(2)
            link = match.group(3)
            time_complexity = match.group(4).replace('<br>', ' ').replace('_O(', 'O(').replace(')_', ')').strip()
            space_complexity = match.group(5).replace('<br>', ' ').replace('_O(', 'O(').replace(')_', ')').strip()

            # Create a dictionary for the current line
            data_dict = {
                'Number': number,
                'Name': name,
                'Link': link,
                'Time Complexity': time_complexity,
                'Space Complexity': space_complexity
            }

            # Add the dictionary to the list
            processed_dict.append(data_dict)
    return processed_dict
