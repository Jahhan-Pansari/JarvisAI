import webbrowser
import re
x = 10
while x == 10:
    query = input("What to search: ")
    replaced_query = re.sub(r'\s', '+', query)
    print(replaced_query)
    part_1 = "https://www.google.com/search?q="
    last_part = "&safe=active&ssui=on"
    url = part_1 + replaced_query + last_part
    webbrowser.open(url)
