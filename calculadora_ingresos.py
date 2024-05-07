horas_trabajadas=int(input('horas trabajadas a la semana: '))
tarifa_hora=float(input('tarifa hora: '))
if horas_trabajadas>40:
    horas_extra=horas_trabajadas-40
    nueva_tarifa=tarifa_hora*1.5
    horas_extra_tarifa=horas_extra*nueva_tarifa
    sueldo=horas_trabajadas*tarifa_hora+horas_extra_tarifa
    print('su ingreso semanadl',sueldo)
else:
    sueldo=horas_trabajadas*tarifa_hora
    print('su ingreso semanal',sueldo)
    
    
    