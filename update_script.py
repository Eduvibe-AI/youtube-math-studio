import re

# Read current html
with open('rpm_pro_geometry_56_59.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect where the `questions` array is defined and replace it with the expanded 42-question set
print("Length of current html:", len(content))
