print("""
||""\\\  \\\  //        //"\\\    ||  // ||""\\\     //"\\\    ||""\\\  ||\\\   //||
||__//   \\\//        //   \\\   ||_//  ||__//    //   \\\   ||__//  || \\\_// ||
||  \\\    ||        //=====\\\  ||`\\\  ||""\\\   //=====\\\  ||""\\\  ||       ||
||__//    ||       //       \\\ ||  \\\ ||   \\\ //       \\\ ||   \\\ ||       ||
""")
print("Welcome!")
man="""
EXIT:	Closes the window
       
CROSS:	Gives the cross product of two vectors the first vector is taken as a and the second is b.
		 
DOT:	Gives the dot product of two vectors.

MOD:	Gives the Module of a vector.

	Note: While inputing the vector's leave a space between two vector components
	      (example: # 1 -2 3) here '1','-2','3' are rectangular components of the vector 'a' along x,y and z axis respectively.
 """
while True:
	exit=input("\n\n\n \t\tpress ENTER to continue or type 'exit' to CLOSE, or 'man' to see MANUAL  # ")
	exit=exit.lower()
	if exit=="man":
		print(man)
	else:
		print("\n\n\t\t\t\t\tNo Input, Retry")
	if exit=="exit":
		break
	if exit=="cross" :
		a,b,c=input("enter first vector: ").split()
		a,b,c=int(a),int(b),int(c)
		l,m,n=input("enter second vector: ").split()
		l,m,n=int(l),int(m),int(n)
		print(f'the cross of vectors is: {a*m}ќ, {-(a*n)}ĵ, {-(b*l)}ќ, {b*n}î, {c*l}ĵ, {-(c*m)}î')
		print(f'the vector becomes: {(b*n)+(-(c*m))}î {(c*l)+(-(a*n))}ĵ {(a*m)+(-(b*l))}ќ')
		if exit=="exit":
			break
	elif exit =="dot":
		a,b,c=input("enter first vector: ").split()
		a,b,c=int(a),int(b),int(c)
		l,m,n=input("enter second vector: ").split()
		l,m,n=int(l),int(m),int(n)
		print(f"the dot product of vectors is {(a*l)+(b*m)+(c*n)}")
	elif exit =="mod":
		a,b,c=input('Enter the Vecotr: ').split()
		a,b,c=int(a),int(b),int(c)
		print(f"Mod of the vector {a,b,c} is √{(a**2)+(b**2)+(c**2)}")


