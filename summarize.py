import os
import subprocess
import openai
import argparse

# Initialize the OpenAI API (make sure your API key is set)
openai.api_key = os.environ["OPENAI_API_KEY"]


def get_last_10_commits(model):
    try:
        # Run the git log command to get the last 10 commits
        result = subprocess.run(['git', 'log', '--oneline', '-n', '10'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)

        # Check if the command was successful
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return

        # Split the output into lines
        lines = result.stdout.strip().split('\n')

        # Process and summarize each commit
        for i, line in enumerate(lines):
            commit_hash, commit_message = line.split(' ', 1)

            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": f"Summarize the following Git commit message: {commit_message}"}]
            )

            # Let's get rid of linebreaks in the summary
            summary = response.choices[0].message.content.strip()
            summary = summary.replace('\r', '').replace('\n', '')

            print(f"{commit_hash}:")
            print(f"  Summary: {summary}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Summarize the last 10 Git commits using GPT.')
    parser.add_argument('--model', choices=['gpt-3.5-turbo', 'gpt-4'], default='gpt-3.5-turbo',
                        help='Choose the GPT model to use for completion.')

    args = parser.parse_args()
    get_last_10_commits(args.model)
