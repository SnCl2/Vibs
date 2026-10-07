import re

files = ['index.html', 'vastu.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove data-tilt, data-tilt-scale, data-aos, and data-aos-delay from .timeline-item
    content = re.sub(r'(<div class="timeline-item")[^>]*>', r'\1>', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
