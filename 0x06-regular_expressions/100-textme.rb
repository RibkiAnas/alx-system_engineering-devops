#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?|\b*?)\] \[to:(.\d*?|\b*?)\] \[flags:(.\d*?|\b*?)\]/).join(',')
