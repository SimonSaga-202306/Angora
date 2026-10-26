#!/usr/bin/perl
use strict;

our $autoadd_flag = 0; # only clear invalid user by default
our %validtbl;
our %sptbl;
our %encryptconftbl;
our %plainconftbl;
our %noconftbl;

sub log() {
    return;
    my $file = "/tmp/spsync.log";
    open F, '>>', $file or die $file . " open failed, $!.\n";
    print F "@_";
    close F;
}

sub dump_tbl() {
    my %tbl = @_;
	foreach my $key (keys %tbl){
		print "$key: $tbl{$key}\n";
	}
}

sub init_validtbl() { # abc:x:0:0:DKOS_abc:/home/abc:/usr/bin/imish
    my $file = "/etc/passwd";
	open F, '<', $file or die $file . " open failed, $!.\n";
	my @lines = <F>;
	close F;
	foreach (@lines) {
		chomp();
		if (/^([^:]+):[^:]+:([^:]+):([^:]+)/) {
            if ($2 == "0" && $3 == "0") {
    			$validtbl{$1} = 1;
            }
		}
	}
}

sub init_sptbl() { # abc:$1$nVoAA4a0$G/iaScm9mZ.urRHbDawgb/::0:99999:7:::
    init_validtbl();
    my $file = "/etc/shadow";
	open F, '<', $file or die $file . " open failed, $!.\n";
	my @lines = <F>;
	close F;
	foreach (@lines) {
		chomp();
		if (/^([^:]+):([^:]+)/) {
            if(exists($validtbl{$1})) { # ignore special accounts
    			$sptbl{$1} = $2;
            }
		}
	}
}

sub init_conftbl() { # username abc password 5 $1$nVoAA4a0$G/iaScm9mZ.urRHbDawgb/
    my $file = "/data/startup.conf";
	open F, '<', $file or die $file . " open failed, $!.\n";
	my @lines = <F>;
	close F;
	foreach (@lines) {
		chomp();
		if (/^\s*username\s+(\S+)\s+password\s+5\s+(\S+)$/) {
			$encryptconftbl{$1} = $2;
		} elsif (/^\s*username\s+(\S+)\s+password\s+(\S+)$/) {
			$plainconftbl{$1} = $2;
		} elsif (/^\s*no username\s+(\S+)$/) {
			$noconftbl{$1} = 1;
        } 
	}
    my $name="admin"; # add default account
    if(!exists($encryptconftbl{$name}) && !exists($plainconftbl{$name}) && !exists($noconftbl{$name})) {
        $plainconftbl{$name} = "admin";
    }
}

sub get_salt() {    # $1$nVoAA4a0$G/iaScm9mZ.urRHbDawgb/
    my ($spass) = @_; # cannot use my $spass=@_, this will cause $spass get a num of args?
    &log("get_salt spass=$spass\n");
    if ($spass=~/(\$.*\$.*\$).*/) { # $1$nVoAA4a0$G/iaScm9mZ.urRHbDawgb/
        return $1;
    }
    return "";
}
sub rand_salt() {
    return "\$1\$nVoAA4a0\$";
}
sub check_user() {
    my ($name, $pass, $encflag) = @_;
    if(!exists($sptbl{$name})) {
        return 0;
    }
    &log("name=$name, pass=$pass, encflag=$encflag, spass=$sptbl{$name}\n");
    if ($encflag) {
        return $sptbl{$name} eq $pass;
    } else {
        my $salt = &get_salt($sptbl{$name});
        my $spass = crypt($pass, $salt);
        &log("salt=$salt, spass=$spass\n");
        return $sptbl{$name} eq $spass;
    }
}
sub del_user() {
    my ($name) = @_;
    if(exists($sptbl{$name})) {
        system("userdel -f $name");
		&log("delete $name\n");
    }
}
sub add_user() {
    my ($name, $pass, $encflag) = @_;
    if (!$autoadd_flag) {
        &log("delay $name encflag $encflag\n");
        return;
    }
    if (!$encflag) {
        my $salt = rand_salt();
        $pass = crypt("$pass","$salt");
    }
    system("useradd -u 0 -o -g 0 -m -s /usr/bin/imish -c DKOS_$name -p '$pass' $name");
}

sub password_sync() { # from conf to etc
	foreach my $name (keys %noconftbl){
        &del_user($name);
	}
	foreach my $name (keys %plainconftbl){
        if (&check_user($name, $plainconftbl{$name}, 0)) {
            &log("ignore $name\n");
            next;
        }
        &del_user($name);
        &add_user($name, $plainconftbl{$name}, 0);
	}
	foreach my $name (keys %encryptconftbl){
        if (&check_user($name, $encryptconftbl{$name}, 1)) {
            &log("ignore $name\n");
            next;
        }
        &del_user($name);
        &add_user($name, $encryptconftbl{$name}, 1);
	}
	foreach my $name (keys %sptbl){ 
        if (exists($noconftbl{$name}) || exists($plainconftbl{$name}) || exists($encryptconftbl{$name})) { # already processed
            next;
        }
        if ($name eq "root") {
            &log("reserve $name\n");
            next;
        }
        system("userdel -f $name"); # delete invalid users
		&log("invalid $name\n");
	}
}

&log("ARGV: @ARGV\n");
if ($ARGV[0] eq "sync") {
    if ($ARGV[1] eq "autoadd") {
        $autoadd_flag = 1;
    }
    init_sptbl();
    init_conftbl();
    # &dump_tbl(%sptbl);
    password_sync();
} elsif ($ARGV[0] eq "check") {
    my $name = $ARGV[1];
    my $pass = $ARGV[2];
    my $encflag = $ARGV[3];
    if (!$name || !$pass) {
        die "invalid arguments! usage $0 check {username} {enc_pass|plain_pass}"
    }
    init_sptbl();
    if (&check_user($name, $pass, $encflag)) {
        print "true\n";
        exit 0;
    }
    die "false";
} else {
    die "invalid arguments! usage $0 {sync|check} ..."
}
