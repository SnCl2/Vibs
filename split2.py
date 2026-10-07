import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

astro_pattern = re.compile(r'(<section id="astro".*?</section>)', re.DOTALL)
vastu_pattern = re.compile(r'(<section id="vastu".*?</section>)', re.DOTALL)

content = astro_pattern.sub('', content)
content = vastu_pattern.sub('', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
