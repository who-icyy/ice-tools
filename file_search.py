import os
import argparse
from datetime import datetime

def search_files(directory, name=None, file_type=None, min_size=None, max_size=None, modified_after=None, modified_before=None):
    results = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            file_extension = os.path.splitext(file)[1][1:]  # Get file extension without dot

            # Filter by name
            if name and name not in file:
                continue

            # Filter by file type
            if file_type and file_extension != file_type:
                continue

            # Filter by size
            if min_size and file_size < min_size:
                continue
            if max_size and file_size > max_size:
                continue

            # Filter by modified date
            if modified_after and file_modified_time < modified_after:
                continue
            if modified_before and file_modified_time > modified_before:
                continue

            results.append((file_path, file_size, file_modified_time))

    return results

def main():
    parser = argparse.ArgumentParser(description="Search for files in a directory based on name, type, size, or modified date.")
    parser.add_argument("directory", help="The directory to search in.")
    parser.add_argument("--name", help="Search by file name.")
    parser.add_argument("--type", help="Search by file extension (e.g., 'txt').")
    parser.add_argument("--min-size", type=int, help="Minimum file size in bytes.")
    parser.add_argument("--max-size", type=int, help="Maximum file size in bytes.")
    parser.add_argument("--modified-after", type=lambda d: datetime.strptime(d, '%Y-%m-%d'), help="Modified after this date (YYYY-MM-DD).")
    parser.add_argument("--modified-before", type=lambda d: datetime.strptime(d, '%Y-%m-%d'), help="Modified before this date (YYYY-MM-DD).")

    args = parser.parse_args()

    # Call the search function with parsed arguments
    results = search_files(
        args.directory,
        name=args.name,
        file_type=args.type,
        min_size=args.min_size,
        max_size=args.max_size,
        modified_after=args.modified_after,
        modified_before=args.modified_before
    )

    # Display results in a tabular format
    print(f"{'File Path':<60} {'Size (Bytes)':<15} {'Modified Date'}")
    print("=" * 90)
    for file_path, file_size, file_modified_time in results:
        print(f"{file_path:<60} {file_size:<15} {file_modified_time}")

if __name__ == "__main__":
    main()
