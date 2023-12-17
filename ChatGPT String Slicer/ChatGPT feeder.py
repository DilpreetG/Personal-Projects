import os

def chatGPT_feeder_from_file(file_path):
    # Maximum character length per text file
    max_length = 4096
    
    # Read the input text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()
    
    # Split the input_text into chunks of max_length
    chunks = [input_text[i:i+max_length] for i in range(0, len(input_text), max_length)]
    
    # Create a directory to store the text files
    output_directory = 'chatGPT_feeder_output'
    os.makedirs(output_directory, exist_ok=True)
    
    # Write each chunk to a separate text file
    for i, chunk in enumerate(chunks):
        file_name = os.path.join(output_directory, f'chunk_{i+1}.txt')
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(chunk)

# Example usage:
file_path = 'ChatGPTfeeder.txt'
chatGPT_feeder_from_file(file_path)
