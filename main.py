import utm

def converter_geografico_para_utm(graus, minutos, segundos, direcao, longitude=False):
    # Converter graus, minutos e segundos para graus decimais
    decimal = graus + minutos/60 + segundos/3600
    if direcao == 'S' or direcao == 'W':
        decimal *= -1

    # Converter para UTM
    if longitude:
        easting, northing, zone_number, zone_letter = utm.from_latlon(0, decimal)
    else:
        easting, northing, zone_number, zone_letter = utm.from_latlon(decimal, 0)

    return easting, northing, zone_number, zone_letter

# Exemplo de uso da função
latitude_graus = 20
latitude_minutos = 30
latitude_segundos = 32
latitude_direcao = 'S'

longitude_graus = 54
longitude_minutos = 39
longitude_segundos = 48
longitude_direcao = 'W'
'''
easting, northing, zone_number, zone_letter = converter_geografico_para_utm(latitude_graus, latitude_minutos, latitude_segundos, latitude_direcao)
print(f"Latitude UTM: {easting}, {northing}, Zone: {zone_number}{zone_letter}")

easting, northing, zone_number, zone_letter = converter_geografico_para_utm(longitude_graus, longitude_minutos, longitude_segundos, longitude_direcao, longitude=True)
print(f"Longitude UTM: {easting}, {northing}, Zone: {zone_number}{zone_letter}")
'''
easting, northing, zone_number, zone_letter = converter_geografico_para_utm(latitude_graus, latitude_minutos, latitude_segundos, latitude_direcao)
print(f"Latitude UTM: {northing:.4f}")

easting, northing, zone_number, zone_letter = converter_geografico_para_utm(longitude_graus, longitude_minutos, longitude_segundos, longitude_direcao, longitude=True)
print(f"Longitude UTM: {easting:.4f}")
