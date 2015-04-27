#!/usr/bin/perl
use Net::SMTP::TLS;
use CGI qw(:standard);

#Login credentials for the gmail account
our $user = 'UserAccount@gmail.com';
our $pass = 'Password';

#Blockfile to prevent spamming
our $block_log = 'blockip.txt';
our $block_time = 60;

#Flag and email address
my $email = param("email");
my $subject = "CTF - Web Exploitation - 100pts";
my $flag = "CVE-1997-1740 Initech online banking sofware persistent XSRF transfers unathorized funds from user";

#Page response
my $text = "Successfully sent TPS Report in an e-mail to #, ".
		"please check your spam folder if it's not in your inbox.\n";




#Log the IP and variables of the sender
my $ip=$ENV{'REMOTE_ADDR'};
open LOG, ">>log.txt";
print LOG localtime()." [$ip]: sent to ($email)";

#Print the header so it renders properly in browsers
print header;

#Spam prevention, do nothing if it's us.
if($email eq "" || $email eq $user) {
	$text =~ s/\#/$user/;
	print $text;
	print LOG " - FAIL(direct)\n";
	exit(-1);
}
#Don't send if it's to Initech
elsif($email =~ m/Initech/i) {
	$text =~ s/\#/$email/;
	print $text;
	print LOG " - FAIL(web)\n";
	exit(-2);
}
elsif(my $diff = get_ip_block($ip)) {
	print "You must wait $diff seconds before submitting again.\n";
	print LOG " - FAIL(spam)\n";
	exit(-3);
}

#Send email
send_mail($email, $subject, $flag);
set_ip_block($ip);


#Give them the response
$text =~ s/\#/$email/;
print $text;
print LOG " - PASS\n";
close LOG;
exit(1);




#Sets an IP as blocked for 30 seconds so they can't resubmit
sub set_ip_block{
	my ($ip) = @_;

	open READIP, ">>$block_log";
	print READIP "$ip:".time()."\n";
	close READIP;
}

#Gets if an IP is blocked
sub get_ip_block{
	my ($ip) = @_;
	open (WRITEIP, "$block_log") or return 1;
	while(<WRITEIP>) {
		chomp;
		if($_ =~ m/^$ip\:(\d+)$/) {
			$time = $1;
			my $diff = (($1+$block_time)-time());
			if($diff >= 0) {
				return $diff;
			}
		}
	}
	close WRITEIP;
	return 0;
}

#Sends a GMAIL message to the destination
sub send_mail{

	#Get the vars
	my ($to, $subject, $body) = @_;

	my $mailer = new Net::SMTP::TLS('smtp.gmail.com',  
		Hello   => 'smtp.gmail.com',
		Port    => 587,
		User    => $user,
		Password=> $pass,
		#Debug 	=> 1,
		);

	#Set the to/from
	$mailer->mail($user);  
	$mailer->to($to);

	#Form up the email message
	$mailer->data();
	$mailer->datasend("From: " . $user . "\n");
	$mailer->datasend("To: " . $to . "\n");
	$mailer->datasend("Subject: " . $subject . "\n");
	$mailer->datasend("\n");
	$mailer->datasend($body . "\n");
	$mailer->dataend();
}
