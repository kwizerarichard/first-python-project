# reading data in a text file using python

#read_file = open("paths to the file/file_name", "pass in what you need to do eg read(r), write(w)", append(a))
read_file = open("C:/Users/Richard/Desktop/karifa.txt","r")
read_data = read_file.read()
print(read_data)

# Writing to a file

richie =  open("C:/Users/Richard/Documents/James.txt","w")
richie.write("We have had our mentoship training")
richie.write("\n Added New Append Text")

