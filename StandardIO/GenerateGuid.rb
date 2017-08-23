#!/usr/bin/ruby

require 'securerandom'

print "Type random text to continue.\n"
STDOUT.flush

while true do
  gets
  print "#{SecureRandom.uuid}\n"
  STDOUT.flush
end
