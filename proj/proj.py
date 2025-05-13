print("Hello Linux!\n")

file_path="proj/hello_linux.txt"
with open(file_path, "r") as f:
     content = list(filter(None, f.read().split('\n')))
     
     headers=list() #headers
     commands=list() # command list
     
     count=0  # command count
     
     for i in range(0,len(content)):
          word = content[i].split(' ') 
           
          count=count+1 
               
          w = word[0].split('.')          
          if(w[0].isdigit()):
               headers.append(word[1])
               
               commands.append(count-1)
               count=0
     
     commands.append(count-2) #add command count to header: headers[i] <=> commands[i+1]
      
     for i in range(0,len(headers)):
           print(headers[i]," ",commands[i+1])
     
     