import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove transition and transform-style from .timeline-item
content = re.sub(r'\s*transition:\s*all 0\.3s ease;', '', content)
content = re.sub(r'\s*transform-style:\s*preserve-3d;', '', content)

# Remove the hover effect for .timeline-item
content = re.sub(r'\.timeline-item:hover\s*\{[^}]*\}', '', content)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
