# This is a developer oriented guide for teaching you
# how to create your own scripts using Echonify.

# More development resources https://github.com/Echonify

import sys, time

def println(text):
    print text
    sys.stdout.flush()

def python_guide():
    println('Good. You\'re good at Python.\n')
    println(('Using Python to develop Echonify Scripts is '
             'very simple. The simplest Echonify Script '
             'requires only one line, such as the following:\n'))
    println(('print \'This is an example of a simple Echonify '
             'Script\'\n'))
    println(('You may have realized that Echonify interacts with '
             'scripts using Standard Input and Output.'))
    println(('As a result, you can use raw_input and '
             'sys.stdin.readline to receive user input. And use '
             'the print function to display information to the '
             'end user.\n'))
    println(('In addition, in order for your print function to '
             'work, we recommend that you always call the '
             'sys.stdout.flush after the print function. Here '
             'are some advanced topics that you can browse '
             'through\n'))
    println('https://www.gnu.org/software/libc/manual/html_node/Buffering-Concepts.html\n')


def ruby_guide():
    println('Good. You\'re good at Ruby.\n')
    println(('Using Ruby to develop Echonify Scripts is '
             'very simple. The simplest Echonify Script '
             'requires only one line, such as the following:\n'))
    println(('puts \'This is an example of a simple Echonify '
             'Script\'\n'))
    println(('You may have realized that Echonify interacts with '
             'scripts using Standard Input and Output.'))
    println(('As a result, you can use the gets function to receive '
             'user input. And use the puts function to display '
             'information to the end user.\n'))
    println(('In addition, in order for your puts function to '
             'work, we recommend that you always call the '
             'STDOUT.flush after the print function. Here '
             'are some advanced topics that you can browse '
             'through\n'))
    println('https://www.gnu.org/software/libc/manual/html_node/Buffering-Concepts.html\n')

def sh_guide():
    println('Coming soon\n')

def show_language_menu():
    time.sleep(1)
    println('Perhaps you want to know other languages too.\n')
    println('1. Python')
    println('2. Ruby')
    println('3. Linux Shell\n')

if __name__ == '__main__':

    println('Welcome to use Echonify.\n')
    println(('If you happen to be a Python or Ruby language '
             'developer, or be familiar with the Linux shell '
             'scripts. Congratulations, you can read this '
             'tutorial and try writing scripts yourself. '
             'You\'ll find the joy of it.\n'))
    println(('First of all, what are your good programming '
             'languages?\n'))
    println('1. Python')
    println('2. Ruby')
    println('3. Linux Shell\n')

    while(True):
        index = raw_input()
        index = index.strip()
        if(index == '1'):
            python_guide()
            time.sleep(1)
            show_language_menu()
        elif(index == '2'):
            ruby_guide()
            show_language_menu()
        elif(index == '3'):
            sh_guide()
            show_language_menu()
        else:
            println('Unknown option')
