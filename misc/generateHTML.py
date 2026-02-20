import os
from bs4 import BeautifulSoup


source_files = [f.split('.')[0] for f in os.listdir('.') if f.endswith('.ipynb') and f.split('_')[0].isdigit()]
source_files.sort(key=lambda x: int(x.split('_')[0]))
for file in source_files:
    if not os.path.exists(f"HTML/{file}.html") or os.path.getmtime(f"{file}.ipynb") > os.path.getmtime(f"HTML/{file}.html"):
        os.system(f"jupyter nbconvert --output-dir='HTML' --to html {file}.ipynb")

output_doc = BeautifulSoup()
output_doc.append(output_doc.new_tag("html"))
output_doc.html.append(output_doc.new_tag("head"))
with open(f"HTML/{source_files[0]}.html", 'r') as html_file:
    output_doc.head.extend(BeautifulSoup(html_file.read(), "html.parser").head)
output_doc.html.append(output_doc.new_tag("body"))



for file in source_files:
    output_doc.body.append(output_doc.new_tag("div", id=file))
    with open(f"HTML/{file}.html", 'r') as html_file:
        output_doc.body.extend(BeautifulSoup(html_file.read(), "html.parser").body)
    

content = output_doc.find_all(["h1", "h2"])
nested_toc = {}
current_h1 = None
for tag in content:
    if tag.name == "h1":
        current_h1 = tag.get('id')
        nested_toc[current_h1] = []
    elif tag.name == "h2" and current_h1:
        nested_toc[current_h1].append(tag.get('id'))

toc = output_doc.new_tag("div", id="table-of-contents")
toc.append(output_doc.new_tag("h2"))
toc.h2.string = "Inhalt"

toc_list = output_doc.new_tag("ul")

for h1tag in nested_toc:
    toc_item = output_doc.new_tag("li")
    toc_link = output_doc.new_tag("a", href=f"#{h1tag}")
    toc_link.string = output_doc.find(id=h1tag).text.replace('¶', '')
    toc_item.append(toc_link)
    for h2tag in nested_toc[h1tag]:
        sub_item = output_doc.new_tag("ul")
        sub_li = output_doc.new_tag("li")
        sub_link = output_doc.new_tag("a", href=f"#{h2tag}")
        sub_link.string = output_doc.find(id=h2tag).text.replace('¶', '')
        sub_li.append(sub_link)
        sub_item.append(sub_li)
        toc_item.append(sub_item)   
    toc_list.append(toc_item)

toc.append(toc_list)
output_doc.body.insert(0, toc)


back_to_toc = output_doc.new_tag("a", href="#table-of-contents", id="back-to-toc")
back_to_toc.string = "↑ Inhalt"
back_to_toc['style'] = "position: fixed; top: 10px; left: 10px; background: white; padding: 5px; border: 1px solid black; text-decoration: none; z-index: 1000;"
output_doc.body.insert(0, back_to_toc)

output_doc.title.string = "EPROG"

with open('HTML/eprog.html', 'w') as merged_file:
    merged_file.write(str(output_doc))

