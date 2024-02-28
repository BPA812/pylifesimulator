import random
#The following work is a life simulator made by Github user BPA812
print("Welcome to PyLife, to start please answer the questions below.")
d1 = 'N'
#Data: Most Populated Cities - Wikipedia - 27/2/24
prefixes = ['Tok','Del','Shang','São','Mexico','Cai','Mum','Bei','Dh','Os','New York','Kara','Buenos','Chong','Istan']
suffixes = ['yo','hi','hai',' Paulo',' City','ro','bai','jing','aka','chi',' Aires','qing','bul']
#Data: Most Populated Countries - Wikipedia - 27/2/24:
prefixes2 = ['Chi','Ind','United','Indon','Paki','Nige','Bra','Bangla','Rus','Mex','Jap','Philipp','Ethio','Egy','Viet']
suffixes2 = ['na','ia',' States','esia','stan','ria','zil','desh','sia','ico','an','ines','pia','pt','nam']
#Data: Counties In California - Wikipedia - 27/2/24
prefixes3 = ['Ala','Al','Am','But','Cala','Col','Contra','Del','El','Fres','Gl','Hum','Imp','In','Ke','Ki','La','Las','Los','Mad','Ma','Mari','Mendo','Mer','Mo','Mo','Mont','Na','Nev','Ora','Pla','Plu','River','Sacra','San','San','San','San','San','San','San','Santa','Santa','Santa','Sha','Sier','Sisk','Sol','Son','Stani','Sut','Teh','Trin','Tul','Tuol','Ven','Yo','Yu']
suffixes3 = ['meda','pine','ador','te','veras','usa',' Costa',' Norte',' Dorado','no','enn','boldt','erial','yo','rn','ngs','ke','sen',' Angeles','era','rin','posa','cino','ced','doc','no','erey','pa','ada','nge','cer','mas','side','mento',' Benito',' Bernardino',' Diego',' Francisco',' Joaquin',' Luis Obispo',' Mateo',' Barbara',' Clara', ' Cruz','sta','ra','iyou','ano','oma','slaus','ter','ama','ity','are','umne','tura','lo','ba']
#Data: List of circulating currencies - Wikipedia - 28/2/24
currencies = ['Apsar','Ruble','Euro','Iek','Dinar','Kwanza','Dollar','Peso','Dram','Florin','Pound','Manat','Taka','Franc','Ngultrum','Rupee','Boliviano','Mark','Pula','Real','Lev','Riel','Escudo','Reniminbi','Colon','Guilder','Koruna','Krone','Nakfa','Lilangeni','Rand','Birr','Sterling','Krona','Dalasi','Lari','Cedi','Quetzal','Gourde','Lempira','Forint','Rupiah','Rial','New Shekel','Yen','Tenge','Shilling','Won','Som','Kip','Loti','Pataca','Ariary','Kwacha','Ringgit','Rufiyaa','Ouguiya','Togrog','Dirham','Metical','Kyat','Cordoba','Naira','Denar','Lira','Balboa','Kina','Guarani','Sol','Zloty','Riyal','Leu','Peseta','Tala','Dobra','Leone','Somoni','Baht','Pa\'anga','Manat','Hryvnia','Sum','Vatu','Bolivar','Dong','']

def generatecity():
    return prefixes[random.randint(0,len(prefixes) - 1)] + suffixes[random.randint(0,len(suffixes))]
def generatecountry():
    return prefixes2[random.randint(0,len(prefixes) - 1)] + suffixes2[random.randint(0,len(suffixes))]
def generatecounty():
    return prefixes3[random.randint(0,len(prefixes) - 1)] + suffixes3[random.randint(0,len(suffixes))]
countries = [generatecountry()]
def generatecountries(x):
        for i in range(x):
            var1 = generatecountry()
            while var1 in countries:
                var1 = generatecountry()
            countries.append(generatecountry())

generatecountries(10)
#Make Character
while d1 == 'N':
    fname = input("Character First Name:")
    lname = input("Character Last Name:")
    gender = input("Character Gender:")
    d1 = input("Is this your chosen character info? (Y/N)")
print('The following countries are countries that you can choose for your character to live in:')
for i in range(len(countries)):
    print('     ' + countries[i])
    countryOC = '     '
    while countryOC not in countries:
        countryOC = input("Please choose a country from the list above: (Full Country Name):")
        if countryOC not in countries:
            print('Sorry, the country name that you entered is invalid, please try again.')
money = 
print(generatecity())
print(generatecountry())
print(generatecounty())