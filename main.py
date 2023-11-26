from search_engine import *
from file_parsers import *


if __name__ == "__main__":
    pdf_data = parse_pdf_directory('documents/')
    reverse_index = build_reverse_index(pdf_data)
    user_query = input("Enter your search query: ")

    search_results = search(user_query, reverse_index)

    if search_results:
        print("Matching documents:")
        for filename in search_results:
            print(filename)
    else:
        print("No matching documents found.")

    # Display or use search results as needed