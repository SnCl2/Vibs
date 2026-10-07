import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace nav links in the template
content = content.replace('href="#home"', 'href="index.html"')
content = content.replace('href="#astro"', 'href="astro.html"')
content = content.replace('href="#vastu"', 'href="vastu.html"')
content = content.replace('href="#contact"', 'href="index.html#contact"')

# Define regex patterns for sections
astro_pattern = re.compile(r'(<section id="astro".*?</section>)', re.DOTALL)
vastu_pattern = re.compile(r'(<section id="vastu".*?</section>)', re.DOTALL)
qual_pattern = re.compile(r'(<section id="qualification".*?</section>)', re.DOTALL)

# Create astro.html (remove vastu and qual)
astro_content = vastu_pattern.sub('', content)
astro_content = qual_pattern.sub('', astro_content)
with open('astro.html', 'w', encoding='utf-8') as f:
    f.write(astro_content)

# Create vastu.html (remove astro and qual)
vastu_content = astro_pattern.sub('', content)
vastu_content = qual_pattern.sub('', vastu_content)
with open('vastu.html', 'w', encoding='utf-8') as f:
    f.write(vastu_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
