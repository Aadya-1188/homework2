

class Reverse:
    def __init__(self, s=""):  
        self.__s = s  
    def set_string(self, s):  
        self.__s = s

    def get_string(self): 
        return self.__s

    def reverse_words(self):  # method to reverse the string word by word
        words = self.__s.split()
        reversed_words = " ".join(reversed(words))
        return reversed_words

    def __str__(self):  
        return self.reverse_words()


# --- main part ---
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    obj = Reverse()          # create object
    obj.set_string(user_input)
    print("Reversed string word by word:", obj)
