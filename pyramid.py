def pyramid_volume(base_length, base_width, pyramid_height):
  base_area = base_length * base_width
  volume = base_area * pyramid_height * (1/3)
  return volume


print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(4.5, 2.1, 3.0))
