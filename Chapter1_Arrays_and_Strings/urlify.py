def convertSpaces(text: str) -> str:
    """Convert spaces to %20 in O(n) time."""
    return text.strip().replace(' ', '%20')

if __name__ == "__main__":
    text = input("Input a string: ")
    result = convertSpaces(text)
    print(result)