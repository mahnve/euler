def fibonaccis_upto(ceiling)
  fibs = [1,1]   
  while true
    new_number = (fibs[fibs.length - 1] + fibs[fibs.length - 2])
    if new_number < ceiling
      fibs << new_number 
    else
      break
    end
  end
  fibs
end


puts fibonaccis_upto(4000000).reduce(:+)
