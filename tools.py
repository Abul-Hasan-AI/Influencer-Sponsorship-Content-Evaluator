import re

def topic_guidelines_extractor(brief_file_content):
    """ Function for extracting guidelines related to topic from brief"""    

    # with open(brief_file_path, 'r',encoding='utf-8') as file: 
    #     markdown_content = file.read()

    pattern = re.compile(r"Step 1: Choose your video topic(.*?)## \*\*Step 2", re.DOTALL)
    match = pattern.search(brief_file_content)

    if match:
        step_1_content = match.group(1).strip()
    return step_1_content

def script_guidelines_extractor(brief_file_content):

    pattern = re.compile(r"### Script(.*?)## \*\*Step 3", re.DOTALL)
    match = pattern.search(brief_file_content)

    if match:
        step_2_content = match.group(1).strip()
    return step_2_content
    pass