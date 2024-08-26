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
        elements = list(csv.reader([l.strip()]))[0]
        if len(elements) == 1:
            if len(output) != 0:
                output += "\n===========\n"
            output += elements[0]
            output += "\n"
            output += "===========\n"
        else:
            try:
                output += storyTemplate.format(href=elements[0],title=elements[1],summary=elements[2])
            except:
                print("Error" + str(elements))

with open('output.txt', 'w+') as f:
    f.write(output)

