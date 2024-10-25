import sys

def validate_commit_message(message):
    print(f"Validating commit message: '{message}'")  # Debugging line
    if len(message) < 15:
        print("Error: Commit message must be at least 15 characters long.")
        return False
    elif not any(word in message.lower() for word in ["fix", "feature", "update"]):
        print("Error: Commit message must contain at least one of the keywords: 'fix', 'feature', or 'update'.")
        return False
    return True

if __name__ == "__main__":
    commit_message_path = sys.argv[1]
    with open(commit_message_path, "r") as file:
        commit_message = file.read().strip()
    
    if not validate_commit_message(commit_message):
        sys.exit(1)  # Exit with error code to block the commit
