

class BinaryTranslator:

    def __init__(self):

        self.lexicons = {
            "a" : "01100001", "b" : "01100010", "c" : "01100011", "d": "01100100", "e": "01100101", "f": "01100110", "g" : "01100111"
            ,"h": "01101000", "i" : "01101001", "j": "01101010", "k": "01101011", "l": "01101100", "m": "01101101", "n": "01101110",
            "o":"01101111","p": "01110000", "q" : "01110001", "r": "01110010","s":"01110011","t": "01110100","u": "01110101",
            "v" : "01110110","w": "01110111", "x" : "01111000", "y" : "01111001", "z": "1111010", " ":""
        }

    def TranslatedText(self,input,i):
        return self.lexicons[input[i].lower()]

    def translate(self):

        user_input = input("Enter Text: ")

        print("Your text in binary is: ")
        for i in range(len(user_input)):

            print(self.TranslatedText(user_input,i))


translator = BinaryTranslator()
translator.translate()