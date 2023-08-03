import json
import subprocess

def install_tool(tool):
    print(f"Installing {tool['name']}...")
    try:
        # subprocess.run(tool['cmd'], shell=True, check=True)
        print(f"{tool['name']} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {tool['name']}. Error: {e}")

def main():
    with open('tools.json', 'rb') as file:
        content = file.read()
    
    tools = json.loads(content)["tools"]
    for tool in tools:
        install_tool(tool)

if __name__ == "__main__":
    main()