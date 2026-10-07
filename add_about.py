import os

files = ['index.html', 'astro.html', 'vastu.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add id='about' to the bio text-content wrapper
    content = content.replace('<div class="text-content" data-aos="fade-right">\n                    <h3>Mr. JAYANTA', '<div class="text-content" id="about" data-aos="fade-right">\n                    <h3>Mr. JAYANTA')
    
    # Add the About link to the nav menu
    about_href = '#about' if file in ['index.html', 'astro.html'] else 'index.html#about'
    nav_link = f'<li><a href="{about_href}" class="nav-links">About</a></li>\n                <li><a href="astro.html"'
    
    content = content.replace('<li><a href="astro.html"', nav_link)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
