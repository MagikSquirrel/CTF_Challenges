#!/usr/bin/perl -w

#Usage: $0 [DTMF tones]
#i.e. dtmf.pl 18005551212

use strict;
use Audio::Wav;

my $volume = 7500;
my $sample_rate = 22050;
my $bits_sample = 16; #my sblive needs 16 
my $num_channels = 1;
my $pi = 4 * atan2 1, 1;
my $duration = 0.5 * $sample_rate;

my @tones;
my %dtmf = (
	'1' => [ 697, 1209 ],
	'2' => [ 697, 1336 ],
	'3' => [ 697, 1477 ],
	'A' => [ 697, 1633 ],
	'4' => [ 770, 1209 ],
	'5' => [ 770, 1336 ],
	'6' => [ 770, 1477 ],
	'B' => [ 770, 1633 ],
	'7' => [ 852, 1209 ],
	'8' => [ 852, 1336 ],
	'9' => [ 852, 1477 ],
	'C' => [ 852, 1633 ],
	'E' => [ 941, 1209 ], #Star *
	'0' => [ 941, 1336 ],
	'F' => [ 941, 1477 ], #Pound #
	'D' => [ 941, 1633 ],
	);

if (@ARGV > 0) {
	@tones = split'',uc($ARGV[0]);
} else {
	@tones = sort keys %dtmf;
}

my $wav = new Audio::Wav;
my $details = {
               'bits_sample'       => $bits_sample,
               'sample_rate'       => $sample_rate,
               'channels'          => $num_channels,
             };
my $write = $wav -> write('dtmf.wav', $details );

for my $tone (@tones) {
	my @hz = map { $pi * $_ } @{$dtmf{$tone}};
	add_tone(@hz);
}

$write -> finish();

sub add_tone {
	my (@hz) = @_;
	for my $pos ( 0 .. $duration ) {
		my $time = $pos / $sample_rate;
		my $val = $volume * sin($time * $hz[0]) + $volume * sin($time * $hz[1]);
		$write -> write( $val );
	}
}
