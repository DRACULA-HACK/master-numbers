import zipfile
import os

# Unzip the masterhackzz-temp-num.py file
with zipfile.ZipFile('masterhackzz-temp-num.zip', 'r') as zip_ref:
    zip_ref.extractall('masterhackzz-temp-num')

# Change directory to masterhackzz-temp-num
os.chdir('masterhackzz-temp-num/py-temp-num')

# Install required packages from requirements.txt
os.system('pip install -r requirements.txt')

# Run the de.py file
os.system('python de.py')
