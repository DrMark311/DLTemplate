import os
import re
import shutil
import subprocess
import sys


def main():
    print("\n🚀 Welcome to the PyTorch Multiplatform Deep Learning Template!")
    project_name = input(
        "👉 Enter your new project name (e.g., my-awesome-project): "
    ).strip()

    if not project_name:
        print("❌ Error: Project name cannot be empty.")
        sys.exit(1)

    if not re.match(r"^[A-Za-z0-9_-]+$", project_name):
        print(
            "❌ Error: Project name can only contain letters, numbers, dashes, and underscores."
        )
        sys.exit(1)

    print(f"\n🔄 Updating pyproject.toml with name '{project_name}'...")

    try:
        with open("pyproject.toml", "r", encoding="utf-8") as f:
            content = f.read()

        # Replace the first instance of name = "..." (which is under [project])
        new_content = re.sub(
            r'name\s*=\s*"[^"]+"', f'name = "{project_name}"', content, count=1
        )

        with open("pyproject.toml", "w", encoding="utf-8") as f:
            f.write(new_content)

    except FileNotFoundError:
        print(
            "❌ Error: pyproject.toml not found. Make sure you are in the project root."
        )
        sys.exit(1)

    print("✅ pyproject.toml updated successfully!")

    # If the user ran this script using 'uv run', uv created a temporary .venv with the old name.
    # We delete it here so 'uv sync' can recreate it cleanly with the new correct name.
    if os.path.exists(".venv"):
        print("🧹 Cleaning up old virtual environment...")
        try:
            shutil.rmtree(".venv")
        except PermissionError:
            print("⚠️ Warning: Could not delete .venv automatically (might be in use).")

    print("\n📦 Running 'uv sync' to build your fresh environment...")
    try:
        subprocess.run(["uv", "sync"], check=True)
        print("\n🎉 Environment setup complete! Your VS Code is ready to go.")
        print("💡 You can now safely delete this 'init.py' file and start coding.")
    except subprocess.CalledProcessError:
        print("\n❌ Error: 'uv sync' failed. Check the error logs above.")
        sys.exit(1)
    except FileNotFoundError:
        print("\n❌ Error: 'uv' command not found. Please install uv first.")
        sys.exit(1)


if __name__ == "__main__":
    main()
