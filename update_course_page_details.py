import pywikibot


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
        # If such response in the form then only modify the page content
        if entry_data is not None:
            # Remove trailing newlines from 'content'
            modified_content = split_data[index].content.rstrip() + '\n\n'
            # print("Modified ", split_data[index].title, '\n\n')
            # Appending the new data
            for each_entry in entry_data:
                modified_entry = each_entry.replace('\n', '\n\n')
                modified_content = modified_content + modified_entry + '\n\n'
            modified_content = modified_content + '\n\n'
            # Modify the content under the respective section
            new_content[index][1] = modified_content
    new_text = header
    for item in new_content:
        section = "".join(item)
        new_text = new_text + section
    return new_text
