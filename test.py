def testMethod(textString):
    def internalMethod(textString2):
        print("Internal string: " + textString2)
    print("You said: " + textString);
    internalMethod(textString2=textString);

print("Hello");
testMethod("Laurenz:");
testMethod("Hello world");