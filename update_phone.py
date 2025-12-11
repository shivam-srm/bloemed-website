import os
import glob

# Directory containing HTML files
directory = r'c:\Users\shiva\Downloads\website Bloemed'

# Old and new phone numbers
old_number = '9451203118'
new_number = '7985656616'

# Get all HTML files
html_files = glob.glob(os.path.join(directory, '*.html'))

# Counter for files updated
files_updated = 0

for file_path in html_files:
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if old number exists
        if old_number in content:
            # Replace the phone number
            updated_content = content.replace(old_number, new_number)
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            files_updated += 1
            print(f"Updated: {os.path.basename(file_path)}")
    
    except Exception as e:
        print(f"Error updating {os.path.basename(file_path)}: {str(e)}")

print(f"\nTotal files updated: {files_updated}")
