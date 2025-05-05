class stringFunctions:

      #CASE SENSITIVE

    def m1(self):
        s1="abcd"
        s2="My Name Is Sanket"
        s3="ABCD"
        s4="I Love My COuntry"
        s5="my rank is 5950"
        s6="12345678"

        print(len(s1))          #To findout lenght of String/ If You Use Count then it will give Index
        print(s2[3])            #
        print(s2[3:8])          #3-8  #s1[startIndex:endIndex+1]
        print("----------------------------------------------------------------------------")

        print(s4.find("o"))     #returns index of 1st occurrence chars
        print(s2.find("e"))
        print(s2.index("Name"))  #Alternate Way to find Index
        print(s2.index("N"))
        print("----------------------------------------------------------------------------")


        print(s1.rfind("c"))       # returns index of last occurrence chars
        print(s4.rfind("y"))
        print(s6.rindex("7"))
        print(s2.rindex("e"))
        print("----------------------------------------------------------------------------")

        print(s1.upper())
        s1=s1.upper()              #Re-initialization
        print(s1)
        s3=s3.lower()
        print(s3)

        print(s1==s3)                      #compare data & case
        print(s1.__eq__(s3))               #Alternate way
        print(s1.lower()==s3.lower())       #compare only data
        print("----------------------------------------------------------------------------")

        print(s4.__contains__("My"))
        print(s4.startswith("My"))
        print(s1+s3)

        print(s2.strip)        #.strip(), .lstrip(), and .rstrip() are string methods in Python used to remove whitespace or specific characters from a string.
        print(s2.lstrip())
        print(s2.rstrip())
        print("----------------------------------------------------------------------------")





str=stringFunctions()
str.m1()