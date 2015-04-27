#!/usr/bin/perl
my $key = "a16f4a707613ddb35a0cd867d900e708";

#Create the file hash
my %files = (
	0 => 'Dtmf0.ogg',
	1 => 'Dtmf1.ogg',
	2 => 'Dtmf2.ogg',
	3 => 'Dtmf3.ogg',
	4 => 'Dtmf4.ogg',
	5 => 'Dtmf5.ogg',
	6 => 'Dtmf6.ogg',
	7 => 'Dtmf7.ogg',
	8 => 'Dtmf8.ogg',
	9 => 'Dtmf9.ogg',
	A => 'DtmfA.ogg',
	B => 'DtmfB.ogg',
	C => 'DtmfC.ogg',
	D => 'DtmfD.ogg',
	E => 'Dtmf-.ogg',
	F => 'DtmfStar.ogg',
);

#Open the binaries
while(my($k, $v)=each(%files)) {
	undef $/;
	open FILE, $v or warn "Can't open $v: $!";
	$files{$k} = <FILE>;
}

#Split the key and merge the files
$key=uc($key);
$key =~ s/[^\dA-F]//gi;
map((print $files{$_}), split(//, $key));
