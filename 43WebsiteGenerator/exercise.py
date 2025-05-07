import os

sitename = input("Site name: ")
author = input("Author: ")
js = input("Do you want a folder for JavaScript? ").lower()
css = input("Do you want a folder for CSS? ").lower()

os.makedirs(sitename)

html_path = os.path.join(sitename, "index.html")
with open(html_path, "w") as f:
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write(f"<title>{sitename}</title>\n")
    f.write(f"<meta name=\"author\" content=\"{author}\">\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("</body>\n")
    f.write("</html>\n")

print(f"Created ./{sitename}")
print(f"Created ./{sitename}/index.html")

if js == "y":
    os.makedirs(os.path.join(sitename, "js"))
    print(f"Created ./{sitename}/js/")

if css == "y":
    os.makedirs(os.path.join(sitename, "css"))
    print(f"Created ./{sitename}/css/")
