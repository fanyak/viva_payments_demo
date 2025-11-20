import re

# Read the entire file
with open('page.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all <script>...</script> tags including their content
# Using DOTALL flag to match newlines
content = re.sub(r'<script[^>]*>.*?</script>', '',
                 content, flags=re.DOTALL | re.IGNORECASE)

# Remove inline event handler attributes (onclick, onload, onmouseover, etc.)
# Match any attribute starting with 'on' followed by event name
content = re.sub(r'\s+on\w+\s*=\s*["\']([^"\']*)["\']', '', content)
content = re.sub(r'\s+on\w+\s*=\s*[^\s>]+', '', content)

# Write the cleaned content to a new file
with open('page_cleaned.html', 'w', encoding='utf-8') as f:
    f.write(content)

original_lines = len(open('page.html', 'r', encoding='utf-8').readlines())
cleaned_lines = len(content.splitlines())

print('✓ Cleaned HTML file created: page_cleaned.html')
print(f'Original file: {original_lines} lines')
print(f'Cleaned file: {cleaned_lines} lines')
print(f'Removed approximately {original_lines - cleaned_lines} lines')
