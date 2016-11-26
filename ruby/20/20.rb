TARGET = ARGV[0].to_i

fac = 1.upto(TARGET).reduce(:*)
facs = fac.to_s
facs.reduce(0) do |tempsum, index|
  tempsum += facs[index].to_i 
end

puts sum
