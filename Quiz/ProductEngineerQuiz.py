from cryptography.fernet import Fernet

class Quiz():
    def firstStepDecipherIntArray(self):
        intArray = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 100, 115, 119, 107, 102, 119, 50, 51, 119, 48, 101, 107, 101, 103, 101, 102, 103 ]
        charArray = [chr(i) for i in intArray]
        strFirstQuizLink = ''.join(charArray)
        print('First step in quiz:- ' + strFirstQuizLink)
        return charArray

    def secondStepDecryptKey(self):
        key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='
        # Oh no! The code is going over the edge! What are you going to do?
        message = b'gAAAAABcVuZEaCDhUbk8rnZzT303uOUk6gkr0qO-AxqRSBj18lRuuDTqyIbaU3_cddl9h26NEvTjocogy3iJnpzFvx4aS285kZdLmU7nn_V7d0SXV4uY8gL1khewiMUGQ_X4TmSjlRPqrWuIdcgoVmjP-wbzg4uwo1DRqXrJYFU8_X0HskviWXU='
        f = Fernet(key)
        retbytesArray = f.decrypt(message)    
        strSecondQuizLink = retbytesArray.decode()
        print('Decrypted Quiz second step :-' + strSecondQuizLink)
        return strSecondQuizLink

def main():
    quiz = Quiz()
    quiz.firstStepDecipherIntArray()
    quiz.secondStepDecryptKey()
    
if __name__ == "__main__":
    main()
