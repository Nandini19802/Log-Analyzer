import re

# Function to analyze log files
def analyze_log(log_file_path):
    log_data = {}
    
    # Define patterns for log events you want to track
    error_pattern = re.compile(r'ERROR:')
    warning_pattern = re.compile(r'WARNING:')
    
    # Open and read the log file
    with open(log_file_path, 'r') as file:
        for line in file:
            if error_pattern.search(line):
                log_data['ERROR'] = log_data.get('ERROR', 0) + 1
            elif warning_pattern.search(line):
                log_data['WARNING'] = log_data.get('WARNING', 0) + 1
    
    return log_data

if __name__ == "__main__":
    log_file = "sample.log"  # Replace with the path to your log file
    result = analyze_log(log_file)
    
    print("Log Analysis Results:")
    print("Number of Errors:", result.get('ERROR', 0))
    print("Number of Warnings:", result.get('WARNING', 0))
