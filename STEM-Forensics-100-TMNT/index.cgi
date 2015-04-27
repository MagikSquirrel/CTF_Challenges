#!/usr/bin/perl
use CGI qw(:standard);

$d = lc(param('d'));
$l = lc(param('l'));
$m = lc(param('m'));
$r = lc(param('r'));

#Log the IP and variables of the sender
$ip=$ENV{'REMOTE_ADDR'};
open FILE, ">>log.txt";
print FILE localtime()." [$ip]: submitted ($d)($l)($m)($r)";

#Print the header so it renders properly in browsers
print header;

#Correct flag submission
if(	$d eq "cow" && $l eq "abu" && $m eq "nga" && $r eq "dude") {
	print FILE " - PASS\n";	
	print "CVE-1990-1603 Incorrectly handled Mutagen process splinters into 4 unknown turtle threads\n";
	close FILE;
	exit(1);
}

#User is trying to be naughty and overflow buffer
elsif(	length($d) + length ($l) + length ($m) + length ($r) > 13) {
	print "Bury my shell at wounded knee! Nouu buffering overflowzing. Try again.";
}

#User typed stupid submission of just names
elsif(	$d eq "d" && $l eq "l" && $m eq "m" && $r eq "r") {
	print "MY TOE! MY TOE! Sorry but just entering the names of the boxes isn't going to do much. Try again.";
}

elsif(	length($d) + length ($l) + length ($m) + length ($r) == 4) {
	print "Bummer dude! Might want to look closer at the hint that involves numbers. Try again.";
}

#User went directly to page, or passed no variables.
elsif(	$d eq "" && $l eq "" && $m eq "" && $r eq "") {
	print "Star base, where no turtle has gone before! Needs input. Try again.";
}

#User is just wrong
else {
	print "Oh!!! Shell shock! Try again.";
}

#Close file
print FILE " - FAIL\n";
close FILE;
