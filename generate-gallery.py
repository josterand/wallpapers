import os
import urllib.parse

readme_file = "README.md"
image_folder = "Collection"
extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
columns = 3
github_repository = "josterand/wallpapers"
branch = "main"

def generate_readme():
    if not os.path.exists(image_folder):
        print(f"Folder '{image_folder}' not found.")
        return

    files = [f for f in os.listdir(image_folder) if f.lower().endswith(extensions)]
    files.sort()

    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write("# Josterand's Wallpaper Gallery\n")
        f.write(f"Total: {len(files)} wallpapers\n\n")

        if not files:
            f.write("_There are no wallpapers in this repository._")
            return

        f.write("<table>\n")
        for index, image in enumerate(files):
            image_path = f"{image_folder}/{image}"
            safe_path = urllib.parse.quote(image_path)
            raw_url_path = urllib.parse.quote(f"{image_folder}/{image}")
            raw_github_url = f"https://raw.githubusercontent.com/{github_repository}/{branch}/{raw_url_path}"
            encoded_url = urllib.parse.quote(raw_github_url, safe='')
            preview_url = f"https://images.weserv.nl/?url={encoded_url}&w=400&output=webp&q=50"

            if index % columns == 0:
                f.write("  <tr>\n")

            f.write(f'    <td align="center" width="{100//columns}%">\n')
            f.write(f'      <a href="{safe_path}"><img src="{preview_url}" width="100%" alt="{image}"></a><br>\n')
            f.write(f'      <sub>{image}</sub>\n')
            f.write("    </td>\n")

            if (index + 1) % columns == 0 or (index + 1) == len(files):
                f.write("  </tr>\n")
        f.write("</table>")

    print("README.md updated successfully!")

if __name__ == "__main__":
    generate_readme()
