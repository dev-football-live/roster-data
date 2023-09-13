import os

data_path = "../raw-data"
file_list = os.listdir(data_path)

def sanity():
    invalid_formats = []

    for filename in file_list:
        with open(f"{data_path}/{filename}", 'rb') as f:
            data = f.read().decode('latin-1')

        if not data.startswith('No'):
            invalid_formats.append(filename)
        else:
            assert data.startswith("No.,Player,Age")
        
    invalid_formats.sort()
    return invalid_formats

invalid_formats = sanity()
print(f"{len(invalid_formats)} files without matching format")
print(invalid_formats)
input('Continue...')


for filename in invalid_formats:
    with open(f"{data_path}/{filename}", 'rb') as f:
        data = f.read().decode('latin-1')
        start_index = data.index("No.,Player,Age")

        data = data[start_index:]
    
    with open(f"{data_path}/{filename}", 'w') as f:
        f.write(data)
       
invalid_formats = sanity()
print(f"{len(invalid_formats)} files without matching format")