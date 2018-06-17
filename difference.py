#difference between %r and %s
#first example
s='spam'
print(repr(s)) #with quotes
print(str(s))  #without quotes

#second example
x="example"
print "My %r" % x #with quotes
print "My %s" % x #without quotes

# Third Example.
x = 'xxx'
withR = ("Prints with quotes: %r" %x)
withS = ("Prints without quotes: %s" %x)
print(withR)
# Prints with quotes: 'xxx'
print(withS)
# Prints without quotes: xxx
