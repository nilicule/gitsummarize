# GitSummarize

This code fetches the last 10 commits of whatever repo is in the current directory and summarizes the commit using ChatGPT.

As an optional parameter the script lets you choose which model should be used for the summary.

## Installation & usage

```
export OPENAI_API_KEY="sk-YOURKEYGOESHERE"
python ~/Projects/gitsummarize/summarize.py --model gpt-4
```

