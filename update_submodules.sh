#!/bin/bash

# Configuration: specify paths to your submodules
declare -a SUBMODULE_PATHS=("src/r4f_yolo" "src/r4f_realsense" "src/r4f_slam" "src/r4f_gnss" "src/r4f_synchronization")

# Commit message for submodule changes
SUBMODULE_COMMIT_MSG="Update submodule with latest changes"

# Commit message for main repository update
MAIN_REPO_COMMIT_MSG="Update submodules to latest commits"

# Loop through each submodule path
for submodule_path in "${SUBMODULE_PATHS[@]}"; do
  echo "Processing submodule at $submodule_path..."

  # Navigate to the submodule directory
  cd "$submodule_path" || exit 1

  # Check if there are changes to commit in the submodule
  if [[ -n $(git status --porcelain) ]]; then
    # Stage all changes, commit, and push to the submodule's remote repository
    git add .
    git commit -m "$SUBMODULE_COMMIT_MSG"
    git push origin main
    echo "Changes in $submodule_path committed and pushed."
  else
    echo "No changes to commit in $submodule_path."
  fi

  # Return to the main repository root
  cd - > /dev/null
done

# Now update the main repository to track the latest submodule commits
echo "Updating main repository to track latest submodule commits..."
cd ~/ros2_ws

# Stage submodule updates and commit
git add .gitmodules "${SUBMODULE_PATHS[@]}"
git commit -m "$MAIN_REPO_COMMIT_MSG"
git push origin main

echo "Main repository updated and pushed successfully."
