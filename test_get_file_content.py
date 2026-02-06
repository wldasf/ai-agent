from functions.get_file_content import get_file_content

def main():
    print("Testing lorem.txt")
    result = get_file_content("calculator", "lorem.txt")
    print(f"Length: {len(result)}")
    print(result)

    print("\nTesting main.py:")
    result = get_file_content("calculator", "main.py")
    print(result)

    print("\nTesting pkg/calculator.py")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    print("\nTesting /bin/cat")
    result = get_file_content("calculator", "/bin/cat")
    print(result)

    print("\nTesting pkg/does_not_exist.py")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)

main()