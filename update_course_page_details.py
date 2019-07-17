import pywikibot

# Syntax for start and end of table in wiki
syntax_start = """{|class="wikitable"
|-
||"""
append_syntax = """
|-
||"""
end_syntax = """|}"""


def append_content_to_page(course_page_text, entry, formatted_contents):
    # Split into required parts
    # Tuple containing 'titles' and 'content' entities
    # this object belongs to the 'Section' class of pywikibot
    # See its docs about it
    total_data = pywikibot.textlib.extract_sections(course_page_text)
    header = total_data[0]
    split_data = total_data[1]
    # The object obtained above is immutable so cannot directly modify it
    new_content = []
    for item in split_data:
        group = []
        group.append(item.title)
        group.append(item.content)
        new_content.append(group)
    # for item in split_data:
    #     print(item.title, item.content)
    index = 2
    length = len(formatted_contents)
    for index in range(2, length):
        # First check if a response exists of a section
        entry_data = entry.get(formatted_contents[index])
        # If response for this section in the form then only modify
        # the content of that respective secion
        if entry_data is not None:
            # Making tabulation of Your Opinion
            # and How to Crack the Paper section
            modified_content = split_data[index].content
            # from now on modification will be done to
            # modified_content variable
            if (index == 3) or (index == 4):
                # check if the table already exists or not
                if syntax_start not in split_data[index].content:
                    modified_content = '\n\n' + syntax_start + split_data[index].content.lstrip()
                else:
                    modified_content = modified_content.rstrip() + '\n\n'
            # Remove trailing newlines from 'content'
            for each_entry in entry_data:
                modified_entry = each_entry.replace('\n', '\n\n')
                if (index == 3) or (index == 4):
                    # Data of sections Your Opinion and How to Crack the Paper
                    # to be added in table format
                    # check for end syntax
                    if end_syntax in modified_content:
                        # if end syntax is there remove it
                        modified_content = modified_content.replace(end_syntax, '')
                        modified_content = modified_content.rstrip()
                    # append the data
                    modified_content = modified_content + append_syntax + modified_entry
                else:
                    modified_content = modified_content + modified_entry + '\n\n'
            # Added end_syntax for table format of sections
            # How to Crack the paper and Your Opinion
            if (index == 3) or (index == 4):
                # add end_syntax
                modified_content = modified_content + '\n\n' + end_syntax
            modified_content = modified_content + '\n\n'
            # Modify the content under the respective section
            new_content[index][1] = modified_content
    new_text = header
    for item in new_content:
        section = "".join(item)
        new_text = new_text + section
    return new_text
