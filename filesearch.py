import os;
import time;

directory = raw_input('Enter your directory: ');
search_file = raw_input("\nEnter the file name: ");

def traverse(search_file, directory):
	count = 0;
	found = False;
	print "\n";
	for root, dirs, filenames in os.walk(directory):
		
		count += len(dirs);
		print "\r[*] Searching through " + str(count) + " Directories",
		time.sleep(0.00000001);

		for file in filenames:
			if file.endswith(search_file):
				print "\n\n[*] File has been found! [*]\n";
				print "\t[*] File Name: '%s' [*]\n" % file;
				print "\t[*] Located: " + os.path.join(root, file) + "\n";
				found = True;

	if found == False:
		print "\n[*] The File does not exist [*]\n";

	print "\n";

	

traverse(search_file, directory);


