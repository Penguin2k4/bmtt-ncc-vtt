import base64

def main():
    try:
        
        with open("plain_text.txt","r") as file:
            encoded_string= file.read().strip()

        decoded_bytes = base64.b64decode(encoded_string)
        decoded_strings = decoded_bytes.decode("utf-8")

        print("chuoi sau khi giai ma",)
        with open ('plain_text.txt',"w") as file:
            file.write(decoded_strings)
    except Exception as e :
        print("loi:",e)

if __name__ == "__main__":
    main()
