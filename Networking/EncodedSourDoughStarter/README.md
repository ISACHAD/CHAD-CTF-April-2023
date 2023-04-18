Prompt 
	
	People who work in isolation often find it easier just to assume everyone around them is incompetent, so they'll apply their own fixes to something that can be handled at a much higher level.  
	
	And they'll often name things "similarily"  
	
	Can you decode the data and discover the flag?  
	
Solution 

	You need to interpret the data as a binary string
	then b64 decode it
	then interpret it as a json string 
	then b32 decode it 
	then interpret it as a list (json also works here)
	then b16 decode it 
	then interpret it as a json string 
	then find the flag (regexes will be annoying beccause of data that looks relatively similar
	
	    flag = {"flag":"CHAD{L4yersUp0nL4yers}"}