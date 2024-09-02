from difflib import SequenceMatcher # compares sequence such as string and find the similarities

# create 2 text file as demo1 and demo2
#open the file  in the palg. as with open command and give any name as you wish using as operator
with open('demo1.txt','r') as one_file, open('demo2.txt','r') as two_file:
   
   # read the text file
    data_file1=one_file.read()
    data_file2=two_file.read()
    
    # to check the plagiarism ratio (the  obj is created with none which means no junk elements are ignored) then it compares the data_file1 and data_file2
    
    check=SequenceMatcher(None,data_file1,data_file2).ratio()
    # to print the count of plagiarized value use {what ever the name you gave}%
    print(f'The plagiarized content is {check}% ')
    # to enhance the count use {the_given _name *100:2f}%
    # which means multiplying the count with 100 and round of to two decimal
    print(f'The plagiarized content is {check*100}% ')
    print(f'The plagiarized content is {check*100:2}% ')
    print(f'The plagiarized content is {check*100:2f}% ')
    print(f'The plagiarized content is {check*100:.2f}%')
  