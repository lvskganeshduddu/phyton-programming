print("Enter '.5' for exit.");
ch = input("Enter any character: ");
if ch == '.5':
    exit();
else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    	print(ch, "is an alphabet.");
    else:
    	print(ch, "is not an alphabet.");
