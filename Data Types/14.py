# 14. Write a Python function to create the HTML string with tags around the
# word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'


def converted_html_string(tag, string):
    html_string = f'<{tag}>{string}</{tag}>'
    return html_string


print(converted_html_string('b', 'Python Tutorial'))
