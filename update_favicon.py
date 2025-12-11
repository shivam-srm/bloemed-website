import os
import glob

# Directory containing HTML files
directory = r'c:\Users\shiva\Downloads\website Bloemed'

# Get all HTML files
html_files = glob.glob(os.path.join(directory, '*.html'))

# Old and new favicon
old_favicon = 'img/favicon.ico'
new_favicon = 'image/IMG-20240508-WA0000.jpg'

# Counter for files updated
files_updated = 0

for file_path in html_files:
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if old favicon exists
        if old_favicon in content:
            # Replace the favicon
            updated_content = content.replace(
                f'<link href="{old_favicon}" rel="icon">',
                f'<link href="{new_favicon}" rel="icon" type="image/jpeg">'
            )
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            files_updated += 1
            print(f"✓ Updated favicon in: {os.path.basename(file_path)}")
    
    except Exception as e:
        print(f"✗ Error updating {os.path.basename(file_path)}: {str(e)}")

print(f"\n✅ Total files updated: {files_updated}")
print(f"✅ New favicon: {new_favicon}")
