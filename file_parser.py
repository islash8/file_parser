#==============================================================================#
# This part is specified for global variables and for importing section        #
# we are importing 2 modules, the system module for opening and closing files  #
# and read through them                                                        #
# and the second module is the re module which is responsible for regex        #
# handling for searching for patterns inside files                             #
#==============================================================================#
import sys
import re

#==============================================================================#


#==============================================================================#
#==============================================================================#
# Name       : text_section                                                    #
# Description: This function is used to handle the text section part in every  #
#              specified component, it searches for the text section entries   #
#              and returns their sizes, and also handles if there is no text   #
#              section entries                                                 #
# Inputs     : Component name which is specified through command line argument #
#              which is input by user (componentName)                          #
#              Contents of the read file is also sent cause we want to search  #
#              through it using regex (contents)                               #
#              The file we are going to write in the results (file)            #
# Outputs    : total size for the text section entries (rom1)                  #
#==============================================================================#
def text_section(componentName, contents, file):

    ### .text section in component

    # Search for specific pattern in the contents of file, and result every    #
    # entry of text section, this is done using regex                          #
    patterns=re.findall(r'([0-9a-fA-F]+[0-9a-fA-F])  (.text)            ('+sys.argv[2]+'\_[\w]+.o)', contents)
    rom1 = 0

    # If any entries found, print them, else, output 0 Bytes in output file    #
    if patterns:

        # Print any entry Found                                                #
        print (patterns)

        # Handle exception if there is less than 2 entries from text section   #
        try:

            # Calculates if there are 2 entries of text section                #
            size = int(patterns[0][0], 16)+int(patterns[1][0], 16)

        # Handle if there is an out of array index error                       #
        except IndexError:

            # Calculate on the only entry found                                #
            size = int(patterns[0][0], 16)

        # Save the size of the text section into rom1, to be passed later for  #
        # outer functions                                                      #
        rom1 = size

        # Dispaly size into terminal for user                                  #
        print (size)

        # Output those result to the output file we created earlier            #
        file.write("Size of .text section in RAMTEST component is =  %d Bytes\n" %size)

    else:
        # Output 0 Bytes into the output file, and this will be handled from   #
        # Parsing functions                                                    #
        file.write("Size of .text section in RAMTEST component is =  0 Bytes\n")

    # Return result of size                                                    #
    return rom1
#==============================================================================#

#==============================================================================#
#==============================================================================#
# Name       : rodata_section                                                  #
# Description: This function is used to handle the rodata section part in every#
#              specified component, it searches for the rodata section entries #
#              and returns their sizes, and also handles if there is no rodata #
#              section entries                                                 #
# Inputs     : Component name which is specified through command line argument #
#              which is input by user (componentName)                          #
#              Contents of the read file is also sent cause we want to search  #
#              through it using regex (contents)                               #
#              The file we are going to write in the results (file)            #
# Outputs    : total size for the rodata section entries (rom2)                #
#==============================================================================#
def rodata_section(componentName, contents, file):

    ### .rodata section in component

    # Search for specific pattern in the contents of file, and result every    #
    # entry of rodata section, this is done using regex                        #
    patterns=re.findall(r'([0-9a-fA-F]+[0-9a-fA-F])  (.rodata)          ('+sys.argv[2]+'_[\w]+.o)', contents)
    rom2 = 0

    # If any entries found, print them, else, output 0 Bytes in output file    #
    if patterns:

        # Print any entry Found                                                #
        print (patterns)

        # Handle exception if there is less than 2 entries from rodata section #
        try:

            # Calculates if there are 2 entries of rodata section              #
            size = int(patterns[0][0], 16)+int(patterns[1][0], 16)

        # Handle if there is an out of array index error                       #
        except IndexError:

            # Calculate on the only entry found                                #
            size = int(patterns[0][0], 16)

        # Save the size of the rodata section into rom2, to be passed later    #
        # for outer functions                                                  #
        rom2 = size

        # Dispaly size into terminal for user                                  #
        print (size)

        # Output those result to the output file we created earlier            #
        file.write("Size of .rodata section in RAMTEST component is = %d Bytes\n\n" %size)

    else:

        # Output 0 Bytes into the output file, and this will be handled from   #
        # Parsing functions                                                    #
        file.write("Size of .rodata section in RAMTEST component is = 0 Bytes\n\n")

    # Return result of size                                                    #
    return rom2
#==============================================================================#

#==============================================================================#
#==============================================================================#
# Name       : data_section                                                    #
# Description: This function is used to handle the data section part in every  #
#              specified component, it searches for the data section entries   #
#              and returns their sizes, and also handles if there is no data   #
#              section entries                                                 #
# Inputs     : Component name which is specified through command line argument #
#              which is input by user (componentName)                          #
#              Contents of the read file is also sent cause we want to search  #
#              through it using regex (contents)                               #
#              The file we are going to write in the results (file)            #
# Outputs    : total size for the rodata section entries (ram1)                #
#==============================================================================#
def data_section(componentName, contents, file):

    ### .data section in component

    # Search for specific pattern in the contents of file, and result every    #
    # entry of data section, this is done using regex                          #
    patterns=re.findall(r'([0-9a-fA-F]+[0-9a-fA-F])  (.data)            ('+sys.argv[2]+'_[\w]+.o)', contents)
    ram1 = 0

    # If any entries found, print them, else, output 0 Bytes in output file    #
    if patterns:

        # Print any entry Found                                                #
        print (patterns)

        # Handle exception if there is less than 2 entries from data section   #
        try:

            # Calculates if there are 2 entries of data section                #
            size = int(patterns[0][0], 16)+int(patterns[1][0], 16)

        # Handle if there is an out of array index error                       #
        except IndexError:

            # Calculate on the only entry found                                #
            size = int(patterns[0][0], 16)

        # Save the size of the data section into ram1, to be passed later      #
        # for outer functions                                                  #
        ram1 = size

        # Dispaly size into terminal for user                                  #
        print (size)

        # Output those result to the output file we created earlier            #
        file.write("Size of .data section in RAMTEST component is = %d Bytes\n" %size)

    else:

        # Output 0 Bytes into the output file, and this will be handled from   #
        # Parsing functions                                                    #
        file.write("Size of .data section in RAMTEST component is = 0 Bytes\n")

    # Return result of size                                                    #
    return ram1
#==============================================================================#

#==============================================================================#
#==============================================================================#
# Name       : bss_section                                                     #
# Description: This function is used to handle the bss section part in every   #
#              specified component, it searches for the bss section entries    #
#              and returns their sizes, and also handles if there is no bss    #
#              section entries                                                 #
# Inputs     : Component name which is specified through command line argument #
#              which is input by user (componentName)                          #
#              Contents of the read file is also sent cause we want to search  #
#              through it using regex (contents)                               #
#              The file we are going to write in the results (file)            #
# Outputs    : total size for the rodata section entries (ram2)                #
#==============================================================================#
def bss_section(componentName, contents, file):

    ### .bss section in component

    # Search for specific pattern in the contents of file, and result every    #
    # entry of bss section, this is done using regex                           #
    patterns=re.findall(r'([0-9a-fA-F]+[0-9a-fA-F])  (.bss)             ('+sys.argv[2]+'_[\w]+.o)', contents)
    ram2 = 0

    # If any entries found, print them, else, output 0 Bytes in output file    #
    if patterns:

        # Print any entry Found                                                #
        print (patterns)

        # Handle exception if there is less than 2 entries from bss section    #
        try:

            # Calculates if there are 2 entries of bss section                 #
            size = int(patterns[0][0], 16)+int(patterns[1][0], 16)

        # Handle if there is an out of array index error                       #
        except IndexError:

            # Calculate on the only entry found                                #
            size = int(patterns[0][0], 16)

        # Save the size of the bss section into ram2, to be passed later       #
        # for outer functions                                                  #
        ram2 = size

        # Dispaly size into terminal for user                                  #
        print (size)

        # Output those result to the output file we created earlier            #
        file.write("Size of .bss section in RAMTEST component is = %d Bytes\n\n" %size)

    else:

        # Output 0 Bytes into the output file, and this will be handled from   #
        # Parsing functions                                                    #
        file.write("Size of .bss section in RAMTEST component is = 0 Bytes\n\n")

    # Return result of size                                                    #
    return ram2

#==============================================================================#


#==============================================================================#
#==============================================================================#
# Name       : parse                                                           #
# Description: This function opens the file passed by command line argument,   #
#              if the file was found, it will open it and start searching for  #
#              the specified components, and invoking each section function to #
#              search for its section for the specific component, then it      #
#              calculates the total for RAM and ROM Size                       #
# Inputs     : NONE                                                            #
# Outputs    : NONE                                                            #
#==============================================================================#

def parse():

    # Handle exception raised if file specified by user is not found           #
    try:
        # Open file specified by user in read mode and read its content        #
        with open(sys.argv[1], 'r') as f:
            contents = f.read()

    # If file couldn't be found, raise an error and exit program execution     #
    except IOError:
        print ("File is not found")
        sys.exit()

    # Save component name as second argument from command line                 #
    componentName = sys.argv[2]

    # Open a new file to write the search results in it                        #
    file = open("testfile.txt","w")

    # Call a text_section function that handles searching for every occurance  #
    # of text section for specified component that was entered by user         #
    # we sould expect the result of total size of text entries                 #
    # from that component (rom1)                                               #
    rom1 = text_section(componentName, contents, file)

    # Call a rodata_section function that handles searching for every occurance#
    # of rodata section for specified component that was entered by user       #
    # we sould expect the result of total size of text entries                 #
    # from that component (rom2)                                               #
    rom2 = rodata_section(componentName, contents, file)

    # Call a data_section function that handles searching for every occurance  #
    # of data section for specified component that was entered by user         #
    # we sould expect the result of total size of text entries                 #
    # from that component (ram1)                                               #
    ram1 = data_section(componentName, contents, file)

    # Call a bss_section function that handles searching for every occurance   #
    # of bss section for specified component that was entered by user          #
    # we sould expect the result of total size of text entries                 #
    # from that component (ram2)                                               #
    ram2 = bss_section(componentName, contents, file)

    # Calculate the total ROM size from the return of both text section, and   #
    # rodata section                                                           #
    total_rom = rom1 + rom2

    # Calculate the total RAM size from the return of both data section, and   #
    # bss section                                                              #
    total_ram = ram1 + ram2

    # If the total sizes of both RAM components and ROM components are equal 0 #
    # Then those section couldn't be found for the module given by user        #
    if (total_ram == 0) and (total_rom == 0) :
        print("Found nothing!")

    # If the total sizes of both are not equal to zero, then print the total   #
    # sizes to the new files we created to display the result of the searching #
    else:
        file.write("-> Size of ROM in RAMTEST component is = %d bytes\n" %total_rom)
        file.write("-> Size of RAM in RAMTEST component is = %d bytes\n\n" %total_ram)
#==============================================================================#


#==============================================================================#
#==============================================================================#
# Name      : main                                                             #
# Descrition: This is the entry point for this python script, it only checks   #
#             for input validation that the user entered the correct number of #
#             inputs. (expected 3 Inputs, first one is the script name itself) #
#             second one is the name of the file we are going to read          #
#             third one is the name of the component/module we are looking for #
# Inputs    : NONE                                                             #
# Outputs   : NONE                                                             #
#==============================================================================#
def main():
    if len(sys.argv) == 2:
        print ("You must set argument!!")
        sys.exit()

    else:
        parse()
#==============================================================================#

#==============================================================================#
# boilerplate to invoke execution of main function                             #
if __name__ == '__main__':
    main()
#==============================================================================#
