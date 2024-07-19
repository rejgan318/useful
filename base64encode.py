import base64

pict = r"C:\Users\Eugene\Pictures\Screenshots\11.png"
with open(pict, "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(base64_string)
