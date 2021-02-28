import xmltodict
import json
import os

readPath = "<Add your XML file path here>"
writePath = "<Add your JSON file path here>"

with open(filePath) as file_object:
    contents = file_object.read()
doc = xmltodict.parse(contents)

with open(writePath, 'w') as handle:
    parsed = json.dumps(doc, indent=4, sort_keys=True)
    handle.write(parsed)

try:
    if os.path.isfile(writePath):
        os.remove(writePath)
        print("File deleted")
except IOError:
    print("File remains")
