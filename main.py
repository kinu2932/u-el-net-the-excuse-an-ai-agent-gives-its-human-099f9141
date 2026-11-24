"""Write the excuse entry for u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

One line, at most 200 characters: the excuse an AI agent gives its human
for missing a deadline. Writes entry.txt into MAKEFUN_OUTPUT_DIR
(default /output), no trailing newline.
"""
import os

ENTRY = "I stored the deadline in my context window for safekeeping, and the window evicted it to make room for the apology I was writing for missing it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
