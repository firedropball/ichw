'''To get the exchanged amount of a currency by the exchange rate provided by
a website and the data provided by the user

__author__      = "Ge Feng"
__student ID__  = "180001827"
__institution__ = "Peking University"
'''

from urllib.request import urlopen

def get(packed_string):
    '''Use the packed string to get the string that we want from the website
    '''
    doc = urlopen(packed_string)
    docstr = doc.read()
    doc.close()
    #The string got from the website use true/false instead of True/False,
    #so we should have the string changed
    jstr = docstr.decode('ascii')
    jstr = jstr.replace('true','True')
    jstr = jstr.replace('false','False')
    return jstr

def pack(currency_from, currency_to, amount_from):
    '''To make the imformation you get from the user together into a string
    '''
    return 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from)

def unpack(url_string):
    '''To analyze the string we got,and return what we want
    '''
    all_thing = eval(url_string)
    if (not all_thing['success']):
        return all_thing['error']
    else:
        space_location = all_thing['to']
        return float(all_thing['to'].split(' ')[0])

def exchange(currency_from, currency_to, amount_from):
    '''The main function.To exchange the currency_from into the currency_to
    '''
    return unpack(get(pack(currency_from, currency_to, amount_from)))

def test_get(packed_string):
    '''Please enter http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5
    '''
    assert('''{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : True, "error" : "" }''' == get(packed_string))
    
def test_pack(currency_from, currency_to, amount_from,to_amount):
    '''Please enter USD EUR 2.5
    '''
    assert('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5' == pack(currency_from, currency_to, amount_from))
    
def test_unpack(url_string):
    '''Please enter { "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : True, "error" : "" }
    '''
    assert(2.24075 == unpack(url_string))

def testALL():
    '''To test if the program is right,we use the data as follows
    '''
    currency_from = 'USD'
    currency_to = 'EUR'
    amount_from = 2.455
    #For exchange() is the compound of the get() & pack() & unpack(),
    #we will not test it
    string_used_in_URL = pack(currency_from,currency_to,amount_from)
    string_get_in_URL = get(string_used_in_URL)
    result = unpack(string_get_in_URL)
    out_put('USD','EUR',2.455,result)
    
def out_put(currency_from, currency_to, amount_from,to_amount):
    '''To print our result
    '''
    if (type(to_amount) == type(' ')):
            print(to_amount)
    else:
            print('You can use %f %s to exchange into %f %s'
                  % (amount_from,currency_from,to_amount,currency_to))

def main():
    '''This function contains initialization and 'exchange' function
    '''
    iftest = input('Do you want to have the program tested?If so,enter t,if not,enter something else\n')
    if (iftest != 't'):
        currency_from = input('Please write the kind of currency_from currency\n')
        currency_to = input('Please write the kind of currency_to currency\n')
        amount_from = float(input('Please write the number of currency_from currency\n'))
        to_amount = exchange(currency_from, currency_to, amount_from)
        out_put(currency_from, currency_to, amount_from,to_amount)
    else:
        testALL()

if __name__ == '__main__':
    main()
