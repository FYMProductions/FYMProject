#!/usr/bin/perl
$_ = "%snippet:,getdate%";
m/(\S+) (\S+) (\S+)(.*)/;
$_ = ucfirst($1) . " $2 " . ucfirst($3) . "$4";
print "$_\n";
