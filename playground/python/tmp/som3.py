import requests


def google():
    filePath = "Cat03.jpeg"
    # domain = self.text
    searchUrl = "http://www.google.com/searchbyimage/upload"
    multipart = {
        "encoded_image": (filePath, open(filePath, "rb")),
        "image_content": "",
        # "q": f"site:{domain}",
    }
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers["Location"]
    print(fetchUrl)


google()
