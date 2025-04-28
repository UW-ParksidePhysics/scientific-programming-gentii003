# compare_list_and_dictionary.py

def compare_snippets():
    code_snippets = {
        "working_dictionary": {
            "snippet": """numbers = {}
numbers[0] = -5
numbers[1] = 10.5""",
            "explanation": "This works because dictionaries allow adding new keys dynamically without needing the keys to exist beforehand.",
            "fixed_snippet": """numbers = {}
numbers[0] = -5
numbers[1] = 10.5"""
        },
        "broken_list": {
            "snippet": """other_numbers = []
other_numbers[0] = -5
other_numbers[1] = 10.5""",
            "explanation": "This fails because lists require that indexes already exist. You can't assign to an index that doesn't exist yet.",
            "fixed_snippet": """other_numbers = [0, 0]
other_numbers[0] = -5
other_numbers[1] = 10.5"""
        }
    }

    # Loop over dictionary to print everything
    for key, value in code_snippets.items():
        print(f"--- {key} ---")
        print("Original Code Snippet:\n")
        print(value['snippet'])
        print("\nExplanation:\n")
        print(value['explanation'])
        print("\nFixed Code Snippet:\n")
        print(value['fixed_snippet'])
        print("\n" + "="*50 + "\n")

if __name__ == '__main__':
    compare_snippets()
