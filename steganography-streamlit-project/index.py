import stegano
from PIL import Image
from pystegano import lsb
import base64
pikachu=Image.open("predicted (4).png")
data=stegano.red.reveal("predicted (5).png")
print(data)



# pikachu=Image.open("pikachu.jpg")
# pikachu.save("pikachu.png")
# with open("pikachu.png", "rb") as f:
#         file_bytes = f.read()
# encoded_data = base64.b64encode(file_bytes).decode()

# lsb.encode("ash.png", encoded_data)
