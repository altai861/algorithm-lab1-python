import sys

def read_file(filepath):
    try: 
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: the file '{filepath}' was not found")
    except PermissionError:
        raise PermissionError(f"Error: You do not have permission to read '{filepath}'.")
    except Exception:
        raise Exception(f"Unexpected error occurred")

def main():
    if len(sys.argv) < 2:
        print("Хэрэглээ: python file_reader.py <filepath>")
        filepath = input("File path to read: ")
    else:
        filepath = sys.argv[1]

    try:
        print(read_file(filepath))
    except (FileNotFoundError, PermissionError) as e:
        print(f"Алдаа гарлаа: {e}")

if __name__ == "__main__":
    main()
