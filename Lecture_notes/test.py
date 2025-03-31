import glob

files = glob.glob("*.md")

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        title = file.replace(".md", "")
        front_matter = f"---\ntitle: {title}\n---\n\n"
        with open(file, "w", encoding="utf-8") as f:
            f.write(front_matter + content)

print("完了しました。")