import os
files = ['index.html', 'astro.html', 'vastu.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('href="style.css?v=2"', 'href="style.css?v=3"')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
