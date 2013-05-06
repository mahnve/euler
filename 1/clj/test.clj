(defn multipleOf? [divisor nominator] (= 0 (rem nominator divisor)))

(defn multipleOfThreeOrFive? [x] (or (multipleOf? 3 x) (multipleOf? 5 x)))

(defn sum [x] (reduce + x))

(defn sumMultiples [x] (sum (filter multipleOfThreeOrFive? (range x))))

(print (sumMultiples 1000))
