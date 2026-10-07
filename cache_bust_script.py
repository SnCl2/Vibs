import os
files = ['index.html', 'astro.html', 'vastu.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('src="script.js"', 'src="script.js?v=2"')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
