#!/usr/bin/python3

from cmd import Cmd
import os, sys
import subprocess
import string

class MyPrompt(Cmd):

	# Function for program invocation
	def default(self, args):
		try:
			tokens = args.split()
			args = tokens[0]
			with open(args, 'rb') as file:
				script = file.read() # Reads contents of file
			if '&' in tokens: # Checks for background execution (ampersand)
				subprocess.Popen(script, shell=True, stdout=subprocess.PIPE)
				# Executes program in background
			else:
				subprocess.call(script, shell=True)
				# Executes program in foregound otherwise
		except:
			print('"{}" is not a valid command.'.format(args))

	def do_dir(self, args):
		path = '.' # Path default to current working directory (cwd)
		if args:			
			path = args # If argument present then path is the argument
		if '>' in args: # Checks for output redirection
			tokens = args.split()
			if len(tokens) == 3: # If path is specified
				path, redirect_token, file = tokens[0], tokens[1], tokens[2]
			elif len(tokens) == 2: # Else path is cwd
				path, redirect_token, file  = '.', tokens[0], tokens[1]

			if redirect_token == '>':
				sys.stdout = open(file, 'w') # Overwrites file
			elif redirect_token == '>>':
				sys.stdout = open(file, 'a') # Appends to file
		try:
			files = os.listdir(path)
			for f in files:
				if not f.startswith('.'): # Ensures that only directories are outputted
					full_path = os.path.join(path, f)
					print(full_path)
		except FileNotFoundError:
			print('Directory "{}" does not exist.'.format(args))
		except NotADirectoryError:
			print('Not a directory.')
		sys.stdout = sys.__stdout__ # Resets stdout to shell
		
	def do_cd(self, args):
		if '>' in args: # Checks for output redirection
			tokens = args.split()
			if len(tokens) == 3: # If path is specified
				args, redirect_token, file = tokens[0], tokens[1], tokens[2]
			else: # Else path is cwd
				args, redirect_token, file = False, tokens[0], tokens[1]

			if redirect_token == '>':
				sys.stdout = open(file, 'w') # Overwrites file
			elif redirect_token == '>>':
				sys.stdout = open(file, 'a') # Appends to file
		if args:
			try:
				os.chdir(args) # Changes cwd to specified path
			except FileNotFoundError:
				print('Directory "{}" does not exist.'.format(args))
			except NotADirectoryError:
				print('Not a directory.')
		else:
			print(os.getcwd()) # Outputs cwd if cd is called with an argument
		self.prompt = os.getcwd() + '>' # Updates the prompt to current working directory
		sys.stdout = sys.__stdout__ # Resets stdout to shell

	# Function to return a list of all directories in CWD (for autocomplete function)
	def get_contents(self, path):
		files = os.listdir(path)
		directories = []
		for name in files:
			full_path = os.path.join(path, name)
			if os.path.isdir(full_path):
				directories.append(full_path.strip(string.punctuation)) # Removes punctuation from path
		return directories # Returns a list of directories in the specified path

	# Autocompletion function for cd command
	def complete_cd(self, text, line, begidx, endidx):
		# Call get_contents function to create list of directories in CWD
		directories = self.get_contents('.')
		if not text: # If user input text not a directory return all directories as suggestions (double TAB)
			completions = directories
		else:
			completions = [d for d in directories if d.startswith(text)]
		return completions # Returns matches in cwd

	# Autocompletion function for dir command
	def complete_dir(self, text, line, begidx, endidx):
		# Call get_contents function to create list of directories in CWD
		directories = self.get_contents('.')
		if not text: # If user input text not a directory return all directories as suggestions
			completions = directories
		else:
			completions = [d for d in directories if d.startswith(text)]
		return completions # Returns matches in cwd

	# Function to clear the screen
	def do_clr(self, args):
		os.system('clear')

	# Function to list all environment strings
	def do_environ(self, args):
		if '>' in args: # Checks for output redirection
			tokens = args.split()
			redirect_token, file = tokens[0], tokens[1]
			if redirect_token == '>':
				sys.stdout = open(file, 'w')
			elif redirect_token == '>>':
				sys.stdout = open(file, 'a')
		print(os.environ)
		sys.stdout = sys.__stdout__ # Resets stdout to shell

	# Function to display string on standard outpute
	def do_echo(self, args):
		if '>' in args: # Checks for output redirection
			tokens = args.split()
			if len(tokens) == 2:
				args, redirect_token, file = False, tokens[0], tokens[1]
			else:
				args, redirect_token, file = ' '.join(tokens[:-2]), tokens[-2], tokens[-1]
			
			if redirect_token == '>':
				sys.stdout = open(file, 'w')
			elif redirect_token == '>>':
				sys.stdout = open(file, 'a')
		if args:
			print(' '.join(args.split())) # Removes spaces and tabs
		print()
		sys.stdout = sys.__stdout__ # Resets stdout to shell

	# Function to pause the shell
	def do_pause(self, args):
		wait = input("Press ENTER to continue.")

	# Function to exit the shell
	def do_quit(self, args):
		# Quits the program
		print('Quitting.')
		exit()

	# Function to open the manual in the shell
	def do_help(self, args):
		with open('readme', 'r') as file:
			try:
				line_number = 1
				for line in file:
					print(line.strip())
					if line_number % 20 == 0:
						input() # Enter must be pressed to display next five lines of manual
					line_number += 1
			except EOFError:
				self.do_quit('quit')

	do_readme = do_help
	do_EOF = do_quit # Allows Ctrl + D keyboard command to quit the shell

def main():
	if len(sys.argv) == 2: # Checks if the shell has been invoked with a batchfile
		try:
			with open(sys.argv[1], 'r') as file:
				prompt = MyPrompt()
				prompt.intro = 'Starting shell...'
				commands = file.readlines() # Commands in file are appended to list
				commands.append('quit') # "Quit" command is also appended to ensure the shell exits
				prompt.cmdqueue = commands
				prompt.cmdloop()
		except FileNotFoundError:
			print('File "{}" does not exist.'.format(sys.argv[1]))
	else: # If no arguments are present then the shell executes as normal
		prompt = MyPrompt()
		prompt.intro = 'Starting shell...'
		prompt.prompt = os.getcwd() + '>'
		prompt.cmdloop()

if __name__ == '__main__':
	main()
