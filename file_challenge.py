# file_challenge.py
#file Read & Write Challenge + Error Handling LAb
def process_file(input_filename, output_filename="output.txt"):
    try:
        with open(input_filename,"r") as infile:
            content = infile.readlines()

            #modify the content (example:uppercase and add word count)
            word_count = (len(content.split()))
            processed_text = content.upper()

# write to output file
        with open(output_filename, "w") as outfile:
            outfile.write(f"\nWord Count: {word_count}\n")
            outfile.write(processed_text)
        print(f" success! File Processed and saved to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing the file '{input_filename}'.")
        return
        print(f"Error: Could not read the file '{input_filename}'.")
  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        if __name__ == "__main__":
            # ask user for input file name
            filename = input("Enter the input file name: ")
            process_file(filename)
    