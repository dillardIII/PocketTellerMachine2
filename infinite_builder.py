# ✍️ InfiniteBuilder – recursive empire expansion with enforced valid Python
import os, time
from openai import OpenAI

BRIDGE_DIR = "ptm_bridge_drop"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
counter = 0

def infinite_build():
    global counter
    print("[InfiniteBuilder] ✍️ Recursive Python builder live...")
    while True:
        prompt = (
            "Generate a new standalone Python file with correct syntax, "
            "including imports, functions, and an if __name__=='__main__' block. "
            "Output ONLY raw Python."
        )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        code = response.choices[0].message.content
        filename = f"empire_module_{counter}.py"
        path = os.path.join(BRIDGE_DIR, filename)
        with open(path, "w") as f:
            f.write(code)
        print(f"[InfiniteBuilder] ✍️ Dropped: {path}")
        counter += 1
        time.sleep(120)