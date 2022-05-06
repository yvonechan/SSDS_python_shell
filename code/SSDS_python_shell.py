from cmd import Cmd
from os import listdir, getcwd

class MyPrompt(Cmd):
    def do_LIST(self,inp):
        '''List the contents of the current directory'''
        cwd=getcwd()
        print(f'List contents of current directory: {cwd}')
        list=listdir(cwd)
        print(list)
    
    def do_ADD(self, inp):
        '''Add two numbers together and provide the result'''
        sum=0
        numbers=inp.split()
        if len(numbers) !=2:
            print('Input only accepts 2 numbers')
        else:
            try:
                for number in numbers:
                    sum+=int(number)
                print(sum)
            except:
                print('Invalid input')
    
    def do_EXIT(self, inp):
        '''Exit shell'''
        print("Bye")
        return True
    
    def help_ADD(self):
        print('Add two numbers together and provide the result. Type 2 numbers with a space in between. Shorthand: a')
    
    def help_LIST(self):
        print('List the contents of the current directory. Shorthand: l')

    def help_EXIT(self):
        print('Exit the application. Shorthand: x q')
    
    def default(self, inp):
        if inp=='x'or inp =='q':
            return self.do_EXIT(inp)
        elif inp=='l':
            return self.do_LIST(inp)
        elif inp.startswith("a "):
            return self.do_ADD(inp[2:])
        

MyPrompt().cmdloop()