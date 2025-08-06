from markdown2 import markdown
from html2image import Html2Image
from datetime import datetime

hti = Html2Image(output_path='news')

def generate_images():
    date = datetime.now().strftime("%Y-%m-%d")
    with open(f"news/news_{date}.md", "r", encoding="utf-8") as f:
        md_content = f.read()
    html_content = markdown(md_content)
    hti.screenshot(html_str=html_content, save_as=f"carousel_{date}.png", size=(1080, 1080))

if __name__ == "__main__":
    generate_images()
