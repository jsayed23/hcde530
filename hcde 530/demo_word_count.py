import csv

# Load survey responses from the CSV file so we can analyze response length
filename = "demo_responses.csv"

with open(filename, newline="", encoding="utf-8") as f:
    # DictReader allows us to access each column by name (participant_id, role, response)
    reader = csv.DictReader(f)
    responses = list(reader)


def count_words(response):
    """Return the number of words in a response string.

    This function is used to measure response length so we can
    compare how detailed different participants' answers are.
    """
    return len(response.split())


# Print a formatted table summarizing each participant's response length
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)

word_counts = []

for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]

    # Calculate word count using the helper function
    count = count_words(response)
    word_counts.append(count)

    # Shorten long responses so the table output stays readable
    preview = response[:60] + "..." if len(response) > 60 else response

    print(f"{participant:<6} {role:<22} {count:<6} {preview}")


# Print summary statistics to help quickly understand overall response length patterns
print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
print(f"  Shortest        : {min(word_counts)} words")
print(f"  Longest         : {max(word_counts)} words")
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
