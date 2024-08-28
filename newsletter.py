import argparse
import csv

parser = argparse.ArgumentParser()

# -f file.csv
parser.add_argument("-f", "--file", help="File name. Custom format format")

args = parser.parse_args()

if not args.file:
    raise Exception('No file provided')

storyTemplate = """<div style="margin-bottom: 12px;">
    <a href="{href}" style="color: black; font-weight: bold;">{title}</a><br/>
    <span style="margin-bottom: 8px">{summary}</span>
</div>
"""

output = ""

with open(args.file, 'r') as f:
    lines = [line.rstrip() for line in f]
    for l in lines:
        if len(l.strip()) < 1:
            continue
        elements = list(csv.reader([l.strip().replace("”", "\"").replace("“", "\"")]))[0]
        if len(elements) == 1:
            if len(output) != 0 and currentFile is not None:
                with open(f'pages/{currentFile}.html', 'w+') as f:
                    f.write(output)
                output = ""

            currentFile = elements[0].lower()
        else:
            if len(elements) != 3:
                print("Less than 3 in a line" + str(elements))
            try:
                output += storyTemplate.format(href=elements[0],title=elements[1],summary=elements[2])
            except:
                print("Error" + str(elements))

    if len(output) != 0 and currentFile is not None:
        with open(f'pages/{currentFile}.html', 'w+') as f:
            f.write(output)

