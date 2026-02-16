#!/bin/bash
# Navigate to the repository
cd /home/ubuntu/machine-learning-daily

# Get current date
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Log the update
echo "Cognitive Echo Progress Update: $DATE" >> daily_log.txt

# Add all changes (documentation, code, etc.)
git add .

# Commit with a descriptive message
git commit -m "Cognitive Echo - Daily Progress: $DATE"

# Push to GitHub
git push origin main
