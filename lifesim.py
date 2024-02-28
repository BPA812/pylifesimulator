import random
#The following work is a life simulator made by Github user BPA812
print("Welcome to PyLife, to start please answer the questions below.")
d1 = 'N'
prefixes = ['Tok','Del','Shang','São','Mexico','Cai','Mum','Bei','Dh','Os','New York','Kara','Buenos','Chong','Istan']
suffixes = ['yo','hi','hai',' Paulo',' City','ro','bai','jing','aka','chi',' Aires','qing','bul']
prefixes2 = ['Chi','Ind','United','Indon','Paki','Nige','Bra','Bangla','Rus','Mex','Jap','Philipp','Ethio','Egy','Viet']
suffixes2 = ['na','ia',' States','esia','stan','ria','zil','desh','sia','ico','an','ines','pia','pt','nam']
prefixes3 = ['Ala','Al','Am','But','Cala','Col','Contra','Del','El','Fres','Gl','Hum','Imp','In','Ke','Ki','La','Las','Los','Mad','Ma','Mari','Mendo','Mer','Mo','Mo','Mont','Na','Nev','Ora','Pla','Plu','River','Sacra','San','San','San','San','San','San','San','Santa','Santa','Santa','Sha','Sier','Sisk','Sol','Son','Stani','Sut','Teh','Trin','Tul','Tuol','Ven','Yo','Yu']
suffixes3 = ['meda','pine','ador','te','veras','usa',' Costa',' Norte',' Dorado','no','enn','boldt','erial','yo','rn','ngs','ke','sen',' Angeles','era','rin','posa','cino','ced','doc','no','erey','pa','ada','nge','cer','mas','side','mento',' Benito',' Bernardino',' Diego',' Francisco',' Joaquin',' Luis Obispo',' Mateo',' Barbara',' Clara', ' Cruz','sta','ra','iyou','ano','oma','slaus','ter','ama','ity','are','umne','tura','lo','ba']
def generatecity():
    return prefixes[random.randint(0,len(prefixes) - 1)] + suffixes[random.randint(0,len(suffixes))]
def generatecountry():
    return prefixes2[random.randint(0,len(prefixes) - 1)] + suffixes2[random.randint(0,len(suffixes))]
def generatecounty():
    return prefixes3[random.randint(0,len(prefixes) - 1)] + suffixes3[random.randint(0,len(suffixes))]
countries = [generatecountry()]
def generatecountries(x):
    for i in range(x):
        countries.append(generatecountry()) 
generatecountries(10)
#Make Character
while d1 == 'N':
    fname = input("Character First Name:")
    lname = input("Character Last Name:")
    gender = input("Character Gender:")
    d1 = input("Is this your chosen character info? (Y/N)")
    print(countries)
    countryOC = input("Please choose a country from the list above: (Full Country Name)")
print(generatecity())
print(generatecountry())
print(generatecounty())