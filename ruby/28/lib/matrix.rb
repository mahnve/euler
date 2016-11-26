class Matrix

  def initialize size
    @size = size
    @array = Array.new(@size, Array.new(@size))
    setup_matrix
  end

  def to_a
    @array
  end

  def setup_matrix
    setone
    # start_stepping
  end

  def setone
    @array[@size/2][@size/2] = 1
  end


end
