import subprocess
import sys

def validate_code():
    try:
        # Run the Databricks CLI command to submit the job (replace with your actual command)
        result = subprocess.run(
            ["databricks", "jobs", "run-now", "--job-id", "your-job-id"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # Check the output of the job
        if result.returncode != 0:
            print(f"Validation failed: {result.stderr}")
            return False
        else:
            print("Validation succeeded")
            return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    if validate_code():
        sys.exit(0)  # Proceed with commit
    else:
        sys.exit(1)  # Block commit

if __name__ == "__main__":
    main()