from app import get_unique_text, minimize_text, clean_and_filter_text

text = "This is an example text. Some words repeat words."

unique_text = get_unique_text(text)
clean_text = minimize_text(unique_text)
filtered_text = clean_and_filter_text(clean_text)

print(filtered_text)
