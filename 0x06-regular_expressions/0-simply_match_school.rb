#!/usr/bin/env ruby

input = ARGV[0]
matches = input.scan(/School/)
output = matches.empty? ? "" : matches.join + "$"
puts output
