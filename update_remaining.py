import os

# List of remaining files to update
files_to_update = [
    'antiInfective.html',
    'bonehealth.html',
    'dermatology.html',
    'diabetology.html',
    'domesticnutraceuticals.html',
    'domesticpharmaceuticals.html',
    'gastroenterology.html',
    'hematology.html',
    'hepatology.html',
    'paediatrics.html',
    'painfever.html',
    'respiratory.html',
    'urology.html'
]

base_dir = r'c:\Users\shiva\Downloads\website Bloemed'

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace phone number
        content = content.replace('9451203118', '7985656616')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated: {filename}")
    except Exception as e:
        print(f"✗ Error with {filename}: {e}")

print("\n✅ All files updated!")
