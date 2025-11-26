import streamlit as st
# import pystegano
import stegano
import base64
from PIL import Image
import os 
import numpy as np


def remove_steganography(input_png:str, output_png:str):
     img = Image.open(input_png)
     mode = img.mode




     if mode not in ("RGB", "RGBA", "L"):


        img = img.convert("RGBA")
        mode = img.mode

     arr = np.array(img, dtype=np.uint8)
     arr = arr & 254
     cleaned = Image.fromarray(arr, mode=mode)
     cleaned.save(output_png)
# st.html(""" <style>
#         .head{
#            postion:absolute;
#            top:0%;
#             left:0%
#         }
        
#         </style>
#         <header class="head"><h1> Welcome To PhotoShop App</h1></header>""")

st.title("Steganography  Webpage")
choices=[
    "Hide any Text",
    "Unhide the Text",
      "Remove Steganography Hidden Text"
]
choice=st.radio("What do you want to do ?",choices)
if choice== choices[0]:
    # st.html(f"<h2>your choice is :{choices[0]}</h2>")
    
    file=st.file_uploader("Give Your File",type=["jpg","png","jpeg"])
    text=st.text_input("Give the Text you want to check?",value=None)
    if (file and text):
        

    
        with open(file.name,"wb") as f:
            f.write(file.getbuffer())
        path=str(file.name).split(".")[0]+".png"
        if(str(file.name).__contains__("jpg") or str(file.name).__contains__("jpeg") ):
            
            File=Image.open(str(file.name))
            File.save(str(file.name).split(".")[0]+".png")
            os.remove(file.name)
        output=stegano.red.hide(path,text)
        saved="predicted.png"
        output.save(saved)
        with open(saved,"rb") as f:
            img_read=f.read()
        st.download_button(label="Download Your png File",data=img_read,file_name=saved,mime="image/png")
        os.remove(saved)
        os.remove(path)
            
# print("Hello")
        
    
elif choice==choices[1]:
    file = st.file_uploader("Upload Carrier PNG", type=["png","jpg","jpeg"])
    # secret = st.file_uploader("Upload Secret Image", type=["png"])
    # if st.button("Hide Image"):
    #     if carrier and secret:
    #          carrier_path = "carrier.png"
    #          secret_path = "secret.png"
    #          output_path = "output.png"
    #          with open(carrier_path, "wb") as f:
    #               f.write(carrier.getbuffer())
    #          with open(secret_path, "wb") as f:
    #               f.write(secret.getbuffer())
    #          with open(secret_path, "rb") as f:
    #               encoded = base64.b64encode(f.read()).decode()
    #               output_=stegano.lsb.hide(carrier_path,encoded)
    #               output_.save(output_path)

    #          with open(output_path, "rb") as f:
    #              st.download_button("Download Stegano Image", f.read(), "output.png", "image/png")
    #              os.remove(carrier_path)
    #              os.remove(secret_path)
    #              os.remove(output_path)
    # print("a")
    # print(bool( file.getbuffer()))
    
    if file:
            with open(file.name,"wb") as f:
                f.write(file.getbuffer())
            path=str(file.name).split(".")[0]+".png"
            

            if(str(file.name).__contains__("jpg") or str(file.name).__contains__("jpeg") ):
            
                 File=Image.open(str(file.name))
                 File.save(str(file.name).split(".")[0]+".png")
                 os.remove(file.name)
            
             
                #  file_=Image.open(path)
                #  text_lsb=stegano.lsb.reveal(path)
                #  print("rsb")
            text_rsb=stegano.red.reveal(path)
            print("lsb")
            if(text_rsb):
                     
                    st.text_area("Hidden Text Revealed:",text_rsb)
                    #  if text_lsb and (not text_rsb):
                    #      st.text_area("Hidden Text Revead:",text_lsb)
                    #  if (text_lsb and text_rsb):
                    #      st.text_area("Hidden Text  Found :",f"{text_lsb} {text_rsb}")
                    #  os.remove(str(file.name))

            else:
                st.write("No Hidden Text Found!")
                      
                     
                     


            #  except :
            #      st.toast("Error Ocurred!")



else:
    file=st.file_uploader("Give Your File",type=["jpg","png","jpeg"])
    if (file):
         try:
             with open(file.name,"wb") as f:
                     f.write(file.getbuffer())
                     path=str(file.name).split(".")[0]+".png"
                     if(str(file.name).__contains__("jpg") or str(file.name).__contains__("jpeg") ):
            
                         File=Image.open(str(file.name))
                         File.save(str(file.name).split(".")[0]+".png")
                         os.remove(file.name)
             output_path="output.png"
             remove_steganography(path,output_path)
             with open(output_path,"rb") as f:
                 img_read=f.read()
                 st.download_button(label="Download Your png File",data=img_read,file_name=output_path,mime="image/png")
                 os.remove(output_path )
                 os.remove(path)


         except Exception :
             st.toast("Error Ocurred!")
          


    # st.html(f"<h2>your choice is :{choices[1]}</h2>")
# st.sidebar.add_rows()
print(choice)


