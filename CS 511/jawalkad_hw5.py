import re
import sys

def main(input_file, output_file):
    try: 
        input_f = open(input_file, 'r')
    except:
        print("Error, can't read input file")    
        return
    
    input_f_content = input_f.read()
    input_f.close()
    print("Input file:\n")
    print(input_f_content)
    print("\n")
    pattern = re.compile(r"\[.*?\]")
    iterator = pattern.finditer(str(input_f_content))

    for match in iterator:
        ans = input("Please provide a "+match.group(0)[1:-1] + ": \n\n")
        print("\n")
        input_f_content = input_f_content.replace(match.group(0), ans)
    
    
    open(output_file, 'w').close()
    output_f = open(output_file,"w+")
    output_f.write(input_f_content)
    print("Output file:\n")
    print(input_f_content)
    print("\n")
    output_f.close()

if __name__=="__main__":
    args = sys.argv
    if(len(args)<3):
        print("Please specify the path to input and output files for the program")
        print("Sample: python3 jawalkad_hw5.py input.txt output.txt")
    else:    
        main(args[1], args[2])