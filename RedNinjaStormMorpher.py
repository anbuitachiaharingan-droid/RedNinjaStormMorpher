def RedNinjaStormMorpher(i):
    G = (6.67 * (10**(-11))); mass_one = 1400; mass_two = 1500; r_squared = 6000;
    for i in range(10):
        print((-i)*((G * mass_one * mass_two)/((r_squared)**2)));
RedNinjaStormMorpher(10);