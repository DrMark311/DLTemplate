import os
import re
import subprocess
import sys

# Force UTF-8 encoding for standard output to avoid UnicodeEncodeError on Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
    except OSError:
        pass


def main():
    print("\n🚀 Welcome to the PyTorch Multiplatform Deep Learning Template!")
    project_name = input(
        "👉 Enter your new project name (e.g., my-awesome-project): "
    ).strip()

    if not project_name:
        print("⏭️ No name provided. Keeping the current project name.")
    else:
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

    print("\n📦 Running 'uv sync' to build your fresh environment...")
    try:
        subprocess.run(["uv", "sync"], check=True)

        # uv normalizes the project name to lowercase when creating the venv.
        # We update the prompt name in pyvenv.cfg here to preserve the exact casing the user provided.
        if project_name:
            pyvenv_path = os.path.join(".venv", "pyvenv.cfg")
            if os.path.exists(pyvenv_path):
                try:
                    with open(pyvenv_path, "r", encoding="utf-8") as f:
                        cfg_content = f.read()

                    cfg_content = re.sub(
                        r"^prompt\s*=.*$",
                        f"prompt = {project_name}",
                        cfg_content,
                        flags=re.MULTILINE,
                    )

                    with open(pyvenv_path, "w", encoding="utf-8") as f:
                        f.write(cfg_content)
                except OSError as e:
                    print(
                        f"⚠️ Warning: Could not update pyvenv.cfg prompt automatically: {e}"
                    )

        print("\n🎉 Environment setup complete! Your VS Code is ready to go.")

        print("\n🗑️ Auto-deleting init.py to prevent accidental reruns...")
        try:
            os.remove(__file__)
            print("✅ init.py deleted successfully.")
        except OSError as e:
            print(
                f"⚠️ Could not delete init.py automatically: {e}. Please delete it manually."
            )
    except subprocess.CalledProcessError:
        print("\n❌ Error: 'uv sync' failed. Check the error logs above.")
        sys.exit(1)
    except FileNotFoundError:
        print("\n❌ Error: 'uv' command not found. Please install uv first.")
        sys.exit(1)


if __name__ == "__main__":
    main()
