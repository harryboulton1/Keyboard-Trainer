def define_coordinates(height, width):
    width = w = width
    height = h = height

    d = h/2
    l = w*0.078

    ex1_coords = ((w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                  (w*0.398, h*0.6-d, w*0.398+l, h*0.6-d+l),
                  (w*0.502, h*0.6-d, w*0.502+l, h*0.6-d+l),
                  (w*0.605, h*0.6-d, w*0.605+l, h*0.6-d+l),
                  (w*0.71, h*0.6-d, w*0.71+l, h*0.6-d+l),
                  (w*0.815, h*0.6-d, w*0.815+l, h*0.6-d+l),
                  (w*0.292, h*0.9-d-l, w*0.292+l, h*0.9-d),
                  (w*0.398, h*0.9-d-l, w*0.398+l, h*0.9-d),
                  (w*0.502, h*0.9-d-l, w*0.502+l, h*0.9-d),
                  (w*0.605, h*0.9-d-l, w*0.605+l, h*0.9-d),
                  (w*0.71, h*0.9-d-l, w*0.71+l, h*0.9-d),
                  (w*0.815, h*0.9-d-l, w*0.815+l, h*0.9-d))

    ex2_coords = ((w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                  (w*0.398, h*0.6-d, w*0.398+l, h*0.6-d+l),
                  (w*0.502, h*0.6-d, w*0.502+l, h*0.6-d+l),
                  (w*0.605, h*0.6-d, w*0.605+l, h*0.6-d+l),
                  (w*0.71, h*0.6-d, w*0.71+l, h*0.6-d+l),
                  (w*0.815, h*0.6-d, w*0.815+l, h*0.6-d+l),
                  (w*0.292, h*0.9-d-l, w*0.292+l, h*0.9-d),
                  (w*0.398, h*0.9-d-l, w*0.398+l, h*0.9-d),
                  (w*0.502, h*0.9-d-l, w*0.502+l, h*0.9-d),
                  (w*0.605, h*0.9-d-l, w*0.605+l, h*0.9-d),
                  (w*0.71, h*0.9-d-l, w*0.71+l, h*0.9-d),
                  (w*0.815, h*0.9-d-l, w*0.815+l, h*0.9-d))

    coords = (ex1_coords, ex2_coords)
    return coords
    
