import re

example_set = ['''<a><b><c></c></b></a>''',
 '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
 '''<foo><bar></bop></bar></foo>''',
 '''<foo><bar></bar></foo></foo>''',
 '''<foo><bar></foo></bar>''']

#Idea is to get all tags from the string <> and </> (using regex)
#Then to use a stack to push opening tags <> and pop when </> is encountered while interating over above list of tags
#While popping if tag and stack top don't match, break and mark as invalid
#Else if we have successfully iterated over list of tags, check if finally stack is empty
#If stack is non empty, tag_string is invalid else valid 

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, elem):    
        self.stack.append(elem)

    def pop(self):        
        if(len(self.stack)):
            elem = self.stack[-1]
            del self.stack[-1]
            return elem
        else: return -1

    def get_top(self):
        if(len(self.stack)):
            return self.stack[-1]
        else:
            return -1     
    
    def is_empty(self):
        return len(self.stack)==0

    def empty(self):       
        self.stack = []


def valid_html(test_strings):
    result    = []
    tag_match = "<(.+?)>"
    pattern   = re.compile(tag_match)
    stack = Stack()

    for example in test_strings:
        is_valid = False
        tags     = re.findall(pattern, str(example))

        i = 0
        while(i<len(tags)):
            tag = tags[i]
            if(tag[0]!='/'):
                stack.push(tag)
            else:
                top_elem = stack.get_top()
                if(top_elem != -1 and tag[1:]==top_elem):
                    stack.pop()
                else: 
                    break    
            i += 1        
        if(i==len(tags) and stack.is_empty()):
            is_valid = True
        stack.empty()    

        result.append((str(example), is_valid))
    return result

print(valid_html(example_set))    