# a program that tells the user the file type of a given file

filename = str(input("What's the Filename? ").lower())

# if gif, png, jpg, or jpeg, print "image/type"

if filename.endswith(".gif"):
    print("Your file type is: image/gif")
elif filename.endswith(".jpg"):
    print("Your file type is: image/jpg")
elif filename.endswith(".png"):
    print("Your file type is: image/png")
elif filename.endswith(".jpeg"):
    print("Your file type is: image/jpeg")

# if text, print "text/plain"

elif filename.endswith(".text"):
    print("Your file type is: text/plain")

# if pdf or zip, print "application/type"

elif filename.endswith(".pdf"):
    print("Your file type is: application/pdf")
elif filename.endswith(".zip"):
    print("Your file type is: application/zip")

# else, print "application/octect-stream"
else:
    print("Your file type is: default/application/octet-stream")