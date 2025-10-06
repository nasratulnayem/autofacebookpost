
import csv
import random
import os

# The list of image URLs you provided
image_urls = [
    "https://i.ibb.co/35yYt9Y5/5.png",
    "https://i.ibb.co/twFLZqgQ/6.png",
    "https://i.ibb.co/DH99GPF6/7.png",
    "https://i.ibb.co/mrPdtTLr/8.png",
    "https://i.ibb.co/knrTRfg/9.png",
    "https://i.ibb.co/HfqKkDwh/10.png",
    "https://i.ibb.co/0jG3qGz6/11.png",
    "https://i.ibb.co/gbgD3Z4T/12.png",
    "https://i.ibb.co/0yN0bJcD/13.png",
]

# The path to your CSV files. 
# On Linux, this should be '/home/black/black/codethumbnail/final_csvs'
# If you are running this on Windows, you might need to adjust the path
# to something like '\\wsl.localhost\kali-linux\home\black\black\codethumbnail\final_csvs'
csv_dir = '/home/black/black/codethumbnail/final_csvs'

# Get a list of all CSV files in the directory
try:
    csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
except FileNotFoundError:
    print(f"Error: The directory '{csv_dir}' was not found.")
    print("Please make sure the path to your CSV files is correct.")
    exit()

print(f"Found {len(csv_files)} CSV files in '{csv_dir}'.")

# Process each CSV file
for filename in csv_files:
    filepath = os.path.join(csv_dir, filename)
    
    rows = []
    header = []
    image_col_index = -1
    
    try:
        # Read the original data
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            try:
                header = next(reader)
            except StopIteration:
                print(f"Skipping empty file: {filename}")
                continue

            # Find the column with image URLs. 
            # We will look for 'image_url' or 'image'.
            try:
                image_col_index = header.index('image_url')
            except ValueError:
                try:
                    image_col_index = header.index('image')
                except ValueError:
                    print(f"Warning: Could not find 'image_url' or 'image' column in {filename}. Skipping this file.")
                    continue
            
            # Read the rest of the rows and update the image URL
            for row in reader:
                if row and len(row) > image_col_index:
                    row[image_col_index] = random.choice(image_urls)
                rows.append(row)

    except Exception as e:
        print(f"An error occurred while processing {filename}: {e}")
        continue

    # Write the modified data back to the file
    if image_col_index != -1:
        try:
            with open(filepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)
                writer.writerows(rows)
            print(f"Successfully updated {filename}")
        except Exception as e:
            print(f"An error occurred while writing to {filename}: {e}")

print("\nFinished processing all CSV files.")
