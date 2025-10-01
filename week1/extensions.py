def main():
    file = input("File name: ").lower().strip()

    if "." in file:
        ext = file.rsplit(".", 1)[1]
    else:
        ext = ""
        
    result = check_ext(ext)
    print (result)

def check_ext(ext):
    if (ext == "jpg" or ext == "jpeg"):
        return "image/jpeg"
    elif (ext == "gif"):
        return "image/gif"
    elif (ext == "png"):
        return "image/png"
    elif (ext == "pdf"):
        return "application/pdf"
    elif (ext == "txt"):
        return "text/plain"
    elif (ext == "zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()