### Name
my_cmd - Python3 command-line interpreter  

### Description
my_cmd is a custom command-line interpreter (CLI) written in Python3.  
It includes a range of commands including cd (change directory), dir (list contents of directory), echo (to display text on standard output).  
It also includes features such as text autocompletion and background execution.  
Compatibility is not guaranteed on non-Linux based operating systems.  

### Invocation
The shell is run through the Linux terminal in the format:  
python3 my_shell.py [batchfile]  

Commands are executed by specifying the command and the output file (optional).  
See the output redirection section for more details on this.  
Example: cd [arg] [> file]  

### Commands

#### cd
	Changes the shell current working directory. To go back a directory use ..  
	Supports autocompletion (see autocompletion section for details).  
	Invocation: cd [directory]  

#### dir
	Display all files and directories in current working directory (default) or specified directory.  
	Supports autocompletion (see autocompletion section for details).  
	Invocation: dir [directory]  

#### echo
	Takes a line of text/a string as an argument and outputs the text to standard output (either the screen or a file). Multiple spaces/tabs are ignored.  
	Invocation: echo [string]  

### Environ
	Prints a list of all environment variables  
	Invocation: environ  

#### clr
	Clears the screen.  
	Invocation: clr  

#### pause
	Halt shell operation until ENTER is pressed.  
	Invocation: pause  

#### quit
	Exits the application.  
	Invocation: quit | EOF | Ctrl + D  

### Output redirection
By default standard output is displayed within the shell on the screen.  
Standard output can be redirected to a specified text file.  
There are two options for redirecting output.  
If the ">" symbol is used, the output file is created if it does not already exist.  
If it does exist than the existing contents (if any) are overwritten.  
Alternatively if the ">>" symbol is used, the output file is created if it does not already exist.  
If it does exist than the new output is appended to the existing contents (if any).  
Following completion of the requested command, standard output is automatically reset to the screen.  
Format: command [arg] > file OR command [arg] >> file  
Example: cd my_folder > output.txt  

### Command line input from a file
The shell supports reading commands from a text file.  
If the shell is started with a file as an argument then the instructions in that file will be executed consecutively.  
Format: my_cmd.py file  

### Text autocompletion
The cd and dir commands support autocompletion. If the first letter(s) of a directory are inputted, pressing the TAB key will autocomplete the directory name.  
If more than one directory matching the inputted letters exits, the TAB key must be pressed twice to display all matches.  
All folders in the current working directory can be display by pressing the TAB key twice, even without any inputted string.  

### Program invocation
Programs can be executed directly from the command line in this shell.  
Any command line input which is not a command is seen as program invocation.  
For example, a script file "hello.sh" with contents "echo "Hello World"" will output "Hello World" as a string on the command line.  
Format: program  

### Background execution
This shell supports background execution.  
If a program is to be executed in the background, the & character (ampersand) should be added at the end of the command line.  
The shell returns to the prompt after the program is launched.  
This feature allows the user to work in the foreground while other processes execute in the background.  
Unlike foreground processes, background processes do not have to wait for other background processes to finish executing.  
Many background processes can be executed simultaneously.  
Format: program &  
