from distutils.log import error
from pathlib import Path
import sys

log_folder_path = sys.argv[1]
p= Path(log_folder_path)
errors = []
total_count = 0

def analyze_file(path):
    error_messages = []
    num_errors = 0
    with open(path, mode = 'r') as logfile:
        for line in logfile:
            line = line.strip()
            if 'ERROR' in line:
                error_messages.append(line)
                num_errors+=1
    logfile.close()
    return num_errors, '\n'.join(error_messages)

for path in p.rglob('*.log'):
    numErrors, msgs = analyze_file(path)
    total_count+=numErrors
    errors.append(msgs)

errors = ''.join(errors)

print(f'Total number of errors: {total_count}')
print(f'Here are the errors:\n{errors}')
    
