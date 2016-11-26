require 'minitest/spec'
require 'minitest/autorun'
# require 'purdytest'
require_relative '../lib/matrix'


describe '1x1' do
  before do
    @matrix = Matrix.new(1)
  end

  it 'should look like this' do
    assert_equal [[1]], @matrix.to_a
  end

  it 'should have 1 in the middle' do
    assert_equal 1, @matrix.to_a[0][0]
  end

end

describe '3x3' do
  before do
    @matrix = Matrix.new(3)
  end
  it 'should have 1 in the middle' do
    assert_equal 1, @matrix.to_a[1][1]
  end

  
  it 'should look like this' do 
    assert_equal [[7, 8, 9],
                  [6, 1, 2],
                  [5, 4, 3]], @matrix.to_a
  end
end
# describe '5x5' do
# 
#   before do
#     @matrix = Matrix.new(5)
#   end
# 
#   it 'should look like this' do
# 
#     assert_equal [[21,22,23,24,25],
#                   [20,7,8,9,10],
#                   [19,6,1,2,11],
#                   [18,5,4,3,12],
#                   [17,16,15,14,13]], @matrix.to_a
# 
#   end
# 
# end
