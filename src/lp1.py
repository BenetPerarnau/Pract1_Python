#!/usr/bin/env python

"""
If you dont put your personal data here, the submission will not be accepted
Group    : 411
Subgroup : 13
Name 1: Benet Perarnau Aguilar
NIU  1: 1423587
Name 2: Adonis Gonzalez Godi
NIU  2: 14
Remarks:
"""
from matplotlib.cbook import Null
from aepack import getword
from objc._objc import NULL

def stemWord(w):
    """Renders a word in to its generic form.
    
    This function is used preprocess words for NLP.
    It removes all trailing punctuation marks "';-?.,!:".
    It also removes the possessive "'s" from words.
    And it converts it to all lower case
    
    Args:
        w (str): A string containing the input word
    
    Returns:
        str a simpler version of the word
    """
    #Describe 
    #Parte el contenido de la variable w por el caracter ' 
    #i guarda la primera parte en la variable w
    w=w.split("'")[0]
    #Describe
    #Bucle que recorre caracter por caracter el String w
    #eliminando de su contenido todos los caracteres que sean
    #iguales a ;-?.,!: el resultado lo guarda en w
    w=[letter for letter in w if not (letter in ';-?.,!:')] 
    #Describe
    #Remplaza los caracteres que estan en minuscula de la
    #cadena w por sus homologos en mayuscula
    return ''.join(w).lower() 


class LanguageModel:
    """Class that contains the data needed for the analysis of text
    """
    @staticmethod
    def getWordFreq(txt):
        """Returns a dictionary where the keys are stemmed words and values
        are the number they occured in txt.
        
        As na example if txt == "The dog likes the cat!" the resulting 
        frequency dictionary should be {"the":2,"dog":1,"likes":1,"cat":1}
        
        Hints: 
            -Use split to break the text in to a list of words
            stem all words in the list
            -Make sure a dictionary element exists before operating on it.
        
        Args:
            txt (str): a string containing free text
            
        Returns:
            dict: A dictionary whith stemmed words (str) for keys and int 
            values containing the occurence count of these words.
        """
        
        txt=stemWord(txt)
        txt=txt.split();    
        dic={}
        for paraula in txt:
            aux=0
            for i in range(len(txt)):
                if paraula == txt[i]:
                    aux+=1
            dic[paraula]=aux       
        return dic

    @staticmethod
    def mergeWordFreqDict(frDict1,frDict2):
        """Takes two dictionaries containing word frequencies and returns a 
        single dictionary containing their sum.
        
        In essence this fuction takes the frequencies produced from two
        different strings with text and returns a dictionary with the 
        word frequencies of the concatenation of these two strings.
        
        Hints:
            -Dictionary .keys() returns a list so you might need to cast it 
            to a set, if you want to get the union.
            -It is better if you create a dictionary with 0 for all words in
            both dictionaries and then update the values
            -If frDict1=={"hello":1,"world":1} and frDict2=={"goodbye":1,"world":1},
            the result must be {"hello":1,"world":2,"goodbye":1}
            -The simplest solution involves 3 non nested for loops.
        
        Args:
            frDict1 (dict): a dictionary with stemmed words as keys and 
            positive integers as values.
            frDict2 (dict): a dictionary with stemmed words as keys and 
            positive integers as values.
        
        Returns:
            dict: a dictionary with stemmed words as keys and positive 
            integers as values.
        """
        #print "mergeWordFreqDict"
        #print 'frDic1 => '+str(frDict1)
        #print 'frDict2 => '+str(frDict2)
        if frDict1 == {} :
            return frDict2
        newDic={}
        for i in frDict1:
            aux=frDict1.get(i)
            for j in frDict2:
                if i==j:
          #          print frDict2.get(j)
                    aux+=frDict2.get(j)
           #         print aux
                elif newDic.get(j)==None:  
                    newDic[j]=frDict2.get(j)
            newDic[i]=aux
            
        
      #  print 'newDic'+str(newDic)       
        return newDic

    def __init__(self,txtList=[]):
        """LangueModel constructor
        
        Initialises the class members to valid values.
        __texts is a list with one or more strings with texts.
        __wordFreq is a dictionary with stemmed words for keys and the 
        count of the occurences of each word (int) as values.
        
        Args:
            txtList (list): A list of strings where each string will 
            contains some text.
        """
        self.__wordFreq={}#Describe
        self.__texts=[]#Describe
        if txtList.__class__ != [].__class__:
            raise Exception('txtList must be a list of strings')
        for txt in txtList:
            self.addText(txt)#Describe

    def addText(self,txt):
        """Adds a string containing text to the model
        
        This method just uses getWordFreq and mergeWordFreqDict static 
        methods on a specific instance of the class
        
        Args:
            txt (str): the string containing text to be added
        """
        #Describe
        #anade al array __texts la cadena de la variable txt
        self.__texts.append(txt)
        #Describe
        #obtenemos un diccionario a partir de la variable txt
        #el diccionario tiene como llave una palabra del texto
        #y como valor las veces que se encuentra en el texto
        newFreq=LanguageModel.getWordFreq(txt)
        #print 'newFreq => '+str(newFreq)
        #Describe
        #unifica el diccionario anterior con el que ya haya 
        #obteniendo un diccionario con todas la palabras y frequencias
        #de los distintos textos guardados en __texts
        self.__wordFreq=LanguageModel.mergeWordFreqDict(self.__wordFreq,newFreq)
        #print self.__wordFreq

    def addTextFile(self,fileName):
        """Ads text contained in a text-file
        
        Args:
            fileName (str): the absolute or relative path to a file 
            containing text.
        """
        self.addText(open(fileName).read())#Describe

    def wordCount(self):
        """Returns the total number of words found in self.__texts
        
        Hints:
        -The answer can be writen in a single line
        -The method values() of dict is the key to solving this question
        -The distionary __wordFreq contains how many times each word was 
        found in the texts

        Returns:
            int: the count of all the words
        """
        
        return sum(self.__wordFreq.values())
        
        

    def uniqueWordCount(self):
        """Returns the number of unique words found in self.__texts

        Unique word means that a word occuring twice or more times, counts 
        as one.

        Hints:
        -The answer can be writen in a single line
        -The method keys() of dict is the key to solving this question

        Returns:
            int: the count of unique words
        """
        
        return len(self.__wordFreq.keys())
        

    def getWordProbabillity(self,word):
        """Returns the probabillity of a word occuring according to the 
        model
        
        The probabillity of a word occuring is the number of times it has 
        occured divided by the count of all word occurences in __texts
        
        Args:
            word (str): an string with a word which is not necessarilly 
            stemmed.

        Returns:
            float: a float between 0 and 1 that contains the probabillity
        """
        stemmedWord=stemWord(word)#Describe
        if stemmedWord in self.__wordFreq.keys():#Describe
            return self.__wordFreq[stemmedWord]/float(self.wordCount())#Describe
        else:
            return 0#Describe

    def __str__(self):
        """Generate a string description of the Language Model
        
        Hints:
        -The result must be constructed with string concatenation
        -Cast an integer to a string before concatening it.
        -Use the already availabe methods to obtain information
        -lm=LanguageModel(['hello world','Goodbye World!'])
        lm.__str__() will return
        "LanguageModel\n\t#texts:2\n\t#words:4\n\t#unique words:3\n"
        -self.__texts, is a list containing all texts the LanguageModel has 
        seen.

        Returns:
            string: A descriptionof the language model spanning 4 lines.
        """
        s="LanguageModel\n"
        s+="\t#texts: "+str(len(self.__texts))+"\n"
        s+="\t#words: "+str(self.wordCount())+"\n"
        s+="\t#unique words:"+str(self.uniqueWordCount())+"\n"
        return s
        
        

    def __repr__(self):
        """Generate a string description of the Language Model that allows 
        to reconstruct it
        
        Returns:
            string: A python expression that invockes the constructor of the
            class so that if executed a deep copy of the LangueageModel is 
            obtained.
        """
        res=str(self.__class__)+'('+self.__texts.__repr__()+')'
        return res

    def getWordsByProbabillity(self):
        """Produces a list containing all stemmed words from the language 
        model sorted from the most probable to the least probable
        
        Hints:
        -function reversed returns a list with reverse order of the input 
        list
        -function sorted returns a list with the elements of the input sorted
        in ascending order.
        -A list of tuples is sorted by the first element of each tuple

        Returns:
            list: a list of strings (not tuples!)
        """
        
        return self.__wordFreq.keys()
    

def isPalindrome(sentence):
    """Tells us whether a string is a palindrome.
    
    Pallindromes are sentences whos characters read in both directions are 
    the same. Testing for pallindromes ignores spaces and puntuation marks
    as if they did not exist.
    
    Hits:
    -A list can be indexed form the end with negative values. 
    -The first character in a string is at position 0
    If a=[1,"b",3,4] Then a[-1] is 4, a[-2] is 3, etc.
    -The expression a[len(a)-1]==a[-1] is always True if a is not empty
    -You will need to use .split() and .join methods of the str type
    
    Args:
        sentence (str): A string with one or more words assumed to have no 
        possessive (stemWord can help).
    
    Returns:
        bool: The return value. True if the sentence was a palindrome, False
        otherwise.
    """
    sentence=stemWord(sentence)
    sentence=sentence.replace(" ","")   
    aux=len(sentence)-1
    i=0
    
    while(aux>=(len(sentence))/2):
        if(sentence[i]==sentence[aux]):
            i+=1
            aux+=-1
        else:
            return False
    
    return True


    

if __name__ == '__main__':
    #Everything here is ignored by joc-de-proves
    #You can debug your program by testing your functions and classes here
   
    #Test 1
    print "\nInicio test 1"
    print "------------------------------------------"
    txt="house's"
    print "text antes stemWord => "+txt
    print "text despues stemWord => "+stemWord(txt)
    
    #Test 2
    print "\nInicio test 2"
    print "------------------------------------------"
    txt="The dog likes the cat!"
    print "text => "+txt
    print "Diccionario generado => "+str(LanguageModel.getWordFreq(txt))
    
    #Test 3
    print "\nInicio test 3"
    print "------------------------------------------"
    frDict1={"hello":1,"world":1}
    frDict2={"goodbye":1,"world":1}
    print "Diccionario 1 => "+str(frDict1)
    print "Diccionario 2 => "+str(frDict2)
    print "Diccionario 3 (Dic1+Dic2) => "+str(LanguageModel.mergeWordFreqDict(frDict1, frDict2))
    
    #Test 4
    print "\nInicio test 4"
    print "------------------------------------------"
    txt=["The dog likes the cat!","Hola mundo, hola mundo"]
    print "text => "+str(txt)
    t=LanguageModel(txt)
    print "text tiene "+str(t.wordCount())+" palabra/s"
    
    #Test 5
    print "\nInicio test 5"
    print "------------------------------------------"
    print "text => "+str(txt)
    print "text tiene "+str(t.uniqueWordCount())+" palabra/s diferente/s"
    
    #Test 6
    print "\nInicio test 6"
    print "------------------------------------------"
    txt=["hello world","Goodbye World!"]
    t=LanguageModel(txt)
    print "text => "+str(txt)
    print t.__str__()
    
    #Test 7
    print "\nInicio test 7"
    print "------------------------------------------"
    print "text => "+str(txt)
    print "lista de mas a menos probable => "+str(t.getWordsByProbabillity())
    
    #Test 8
    print "\nInicio test 8"
    print "------------------------------------------"
    text="1 2 3   21  !"
    text2="abccba"
    text3="abcdecba"
    print "El texto "+text+" es polindromo? "+str(isPalindrome(text))
    print "El texto "+text2+" es polindromo? "+str(isPalindrome(text2))
    print "El texto "+text3+" es polindromo? "+str(isPalindrome(text3))
