#Method-1
def get_unique_filenames_per_row(file_content):
    result = []
    for line in file_content.split('\n'):
        filenames = line.split('|')
        filenames_without_extension = []
        for filename in filenames:
            filename_without_extension = filename.split('.')[0]
            filenames_without_extension.add(filename_without_extension)
        unique_filenames = [filename for filename in filenames if filenames_without_extension.count(filename.split('.')[0]) == 1]
        result.append('|'.join(unique_filenames))
    return '\n'.join(result)

# Example usage
file_content = """foo.mp3|bar.txt|baz.mp3
wub.mp3|wub.mp3|wub.mp3|wub.txt|wub.png
quux.mp3|quux.txt|thud.mp3"""
print(get_unique_filenames_per_row(file_content))
