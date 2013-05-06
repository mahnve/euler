def multiple_of_3_or_5?(x)
  (x.remainder(3) == 0) || (x.remainder(5) == 0)
end

result = (1...1000).select{|x| multiple_of_3_or_5?(x)}.reduce(:+)

puts result
