import json
import subprocess
import time

def install_tool(tool):
    print(f"Installing {tool['name']}...")
    try:
        subprocess.run(tool['cmd'], shell=True, check=True)
        print(f"{tool['name']} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {tool['name']}. Error: {e}")

def main():
    with open('tools.json', 'rb') as file:
        content = file.read()
    tools = json.loads(content)["tools"]
    for tool in tools:
        if(tool.get("enabled")):
            install_tool(tool)

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Installation process completed in {elapsed_time:.2f} seconds.")