#!/bin/bash

# Create or overwrite the file list
echo "Repository file list:" > repository_files.txt
echo "Generated on $(date)" >> repository_files.txt
echo "-------------------" >> repository_files.txt

# Find all files, excluding patterns from .gitignore and temporary files
find . -type f \
    ! -path "./.git/*" \
    ! -path "./repository_files.txt" \
    ! -path "**/__pycache__/*" \
    ! -path "**/*.pyc" \
    ! -path "**/*.pyo" \
    ! -path "**/*.pyd" \
    ! -path "**/*.so" \
    ! -path "**/build/*" \
    ! -path "**/dist/*" \
    ! -path "**/*.egg-info/*" \
    ! -path "**/downloads/*" \
    ! -path "**/.eggs/*" \
    ! -path "**/.env" \
    ! -path "**/.env.local" \
    ! -path "**/.env.*.local" \
    ! -path "**/.idea/*" \
    ! -path "**/.vscode/*" \
    ! -path "**/*.swp" \
    ! -path "**/*.swo" \
    ! -name ".DS_Store" \
    ! -name "poetry.lock" \
    -print0 | while IFS= read -r -d '' file; do
    echo "$file" >> repository_files.txt
    
    # Add file contents for Python files (optional)
    if [[ "$file" == *.py ]]; then
        echo "  Content of $file:" >> repository_files.txt
        echo "  -------------------" >> repository_files.txt
        cat "$file" | sed 's/^/  /' >> repository_files.txt
        echo "" >> repository_files.txt
    fi
done