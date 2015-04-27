#!/usr/bin/perl
use IO::Socket;
die "Usage ./server.pl port" unless scalar(@ARGV == 1);
$k="CVE-2001-43895 Torrenting in cerebral cortex using Zion mainframe results in error \"Woah, I know kung-fu\"";
$s=IO::Socket::INET->new(LocalPort => $ARGV[0], Proto => "udp") 
	or die "Couldn't be a udp server on port $ARGV[0]: $@\n";
while($c=$s->recv($d, 1)) {
	$s->send("$k\n");
}
