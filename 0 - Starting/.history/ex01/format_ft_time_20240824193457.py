import time
from datetime import datetime

# Get the current time in seconds since the Unix epoch
current_seconds = time.time()

# Format the seconds with a comma separator
formatted_seconds = f"{current_seconds:,.4f}"

# Convert the seconds to scientific notation
scientific_seconds = f"{current_seconds:.5e}"

# Format the current date
current_date = datetime.now().strftime("%b %d %Y")

# Print the formatted output
print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_seconds} in scientific notation")
print(current_date)
print("$>")
