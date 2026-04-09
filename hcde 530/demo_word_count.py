import csv


# Load the CSV file
filename = "demo_responses.csv"
responses = []

with open(filename, newline="", encoding="utf-8") as f:
# Open the CSV file and read it into a dictionary
    reader = csv.DictReader(f)
# Read the CSV file into a dictionary
    for row in reader:
        responses.append(row)

# Add the row to the list of responses  
# Define a function to count the number of words in a response
def count_words(response):
    """Count the number of words in a response string.

    Takes a string, splits it on whitespace, and returns the word count.
    Used to measure response length across all participants.
    """
    # Split the response into words and return the number of words
    # Return the number of words
    return len(response.split())


# Count words in each response and print a row-by-row summary
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)

# Print the header
# Create a list to store the word counts
word_counts = []

# Loop through the responses
for row in responses:
    # Get the participant ID and role from the row
    participant = row["participant_id"]
    role = row["role"]
    # Get the response from the row
    response = row["response"]
    # Call our function to count words in this response
    count = count_words(response)
    # Add the count to the list of word counts
    word_counts.append(count)
    if len(response) > 60:
        preview = response[:60] + "..."
    else:
        preview = response
    # Print the participant ID, role, word count, and response preview
    print(f"{participant:<6} {role:<22} {count:<6} {preview}")
# Print summary statistics
print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
print(f"  Shortest        : {min(word_counts)} words")
print(f"  Longest         : {max(word_counts)} words")
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
