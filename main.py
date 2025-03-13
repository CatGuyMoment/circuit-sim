
PROBE_INTERFERENCE = 10**10

## what react does to a man... functional hell......

def resist(resistance):
    def constructor(voltage):
        return
    
    def get_resistance():
        return resistance
    
    return constructor, get_resistance

def air(distance):
    return resist( (1.5 * 10**13) * distance)

def wire(distance,resistivity,surface):
    return resist( resistivity *  distance / surface)



def amp_probe(tag=''):
    def constructor(voltage):
        print(f'AMPEGAGE {tag}:',voltage * PROBE_INTERFERENCE)
    
    def get_resistance():
        return 1/PROBE_INTERFERENCE

    return constructor, get_resistance


def volt_probe(tag=''):
    def constructor(voltage):
        print(f'VOLTAGE {tag}:', voltage)
    
    def get_resistance():
        return PROBE_INTERFERENCE

    return constructor, get_resistance  






def series(*components):
    def get_resistance():
        total_resistance = 0
        
        for _, get_c_resistance in components:
            total_resistance += get_c_resistance()
        return total_resistance
    
    def constructor(voltage):
        total_resistance = get_resistance()

        amps = voltage / total_resistance

        for component, get_c_resistance in components:
            local_voltage = amps * get_c_resistance()
            component(local_voltage)
    
    return constructor, get_resistance


def parallel(*components):
    def get_resistance():
        total_resistance = 0
        
        for _, get_c_resistance in components:
            total_resistance += 1/get_c_resistance()

        return 1/total_resistance

    def constructor(voltage):
        for component, _ in components:
            component(voltage)    

    return constructor, get_resistance


############# CIRCUIT #####################

series(
    parallel(
        resist(10),
        volt_probe('1')
    ),
    
    parallel(
        series(amp_probe('1'),resist(10)),
        resist(10),
        resist(10)
    )
)[0](9)

        