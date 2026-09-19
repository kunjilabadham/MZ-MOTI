#!/bin/bash
set -e

# Configuration (set these as environment variables in Kaggle Secrets)
# GITHUB_TOKEN="your_personal_access_token"
# GITHUB_USERNAME="your_username"
# REPO_NAME="shrinithi_infra_promo"
# GITHUB_EMAIL="your_email@example.com"

# Render the video
echo "Rendering Manim video..."
manim -pqh main.py ShrinithiInfraPromo

# Configure Git
git config --global user.email "$GITHUB_EMAIL"
git config --global user.name "$GITHUB_USERNAME"

# Stage the rendered video
# Manim outputs to media/videos/main/1080p60/
# We use -f to force add it in case media/ is in .gitignore (which it is, except for the mp4)
git add -f media/videos/main/1080p60/ShrinithiInfraPromo.mp4

# Commit and Push
echo "Committing to GitHub..."
git commit -m "Automated render from Kaggle [skip ci]" || echo "No changes to commit"

# Construct remote URL with token for authentication
REMOTE_URL="https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

echo "Pushing to remote..."
git push $REMOTE_URL main
echo "Push complete!"
