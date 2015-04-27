#!/usr/bin/perl

use IO::Socket; #additional header for sockets handling

my $BUFF = 1024;

#Port to connect to
my $port = 20911;

#Create socket
my $socket = new IO::Socket::INET(  
		PeerAddr => "localhost",
        PeerPort => $port, 
        Proto => 'tcp') || die "Error creating socket: $!";


my $song = LoadSong("Lyrics.txt");
my @lyrics = @$song;
my $lines = scalar(@lyrics);
my $line = 0;
my $text;

#Get shit from server
my $loop = 1;
while($loop){

	$socket->recv($text,$BUFF);
	print $text;
	
	if($text =~ m/GLaDOS/){
		$loop = 0;
	}
}

print "\n";

#Get/Send shit to server
while($line <= $lines) {

	#Send my line
	$text = $lyrics[$line];
	print "Client: $text ($line/$lines)\n";
	$socket->send($text."\n");
	
	#Get server's line
	$socket->recv($text,$BUFF);
	print "Server: $text\n";
	
	#Increment lyrics by 2
	$line += 2;	
}

$socket->send("?\n");

#Print FLAG?!@
$socket->recv($text,$BUFF);
print $text;
$socket->recv($text,$BUFF);
print $text;

$socket->send("?\n");

close $server;







sub LoadSong {
	my $file = shift;
	open FILE, $file;
	my @song;
	my $count = 0;
	while(my $line = <FILE>){

		chomp($line);
		$song[$count++] = $line;
	}
	close FILE;
	return \@song;
}
