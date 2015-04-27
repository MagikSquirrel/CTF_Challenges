#!/usr/bin/perl
use CGI qw(:standard);

$q = lc(param('q'));

#Log the IP and variables of the sender
$ip=$ENV{'REMOTE_ADDR'};
open FILE, ">>log.txt";
print FILE localtime()." [$ip]: submitted ($q)";

#Parse
$q =~ s/[^a-f\d]//g;

#Print the header so it renders properly in browsers
print header;

#Correct flag submission
if(	$q eq "12741c6728f4e584ac539e85f52deb21") {
	print FILE " - PASS\n";	
	print "FLAG: Dialing...\n";
	close FILE;
	exit(1);
}

#User is just wrong
else {
	print "We're sorry. If you'd like to make a call, please hang up and try again";
}

#Close file
print FILE " - FAIL\n";
close FILE;
