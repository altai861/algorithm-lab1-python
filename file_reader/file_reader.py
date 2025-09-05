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
    try:
        print(read_file("lab2.txt"))
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")

    print("Program has ended")

if __name__ == "__main__":
    main()
    