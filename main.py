import utm

def converter_geografico_para_utm(graus, minutos, segundos, direcao, longitude=False):
    # Converter graus, minutos e segundos para graus decimais
    decimal = graus + minutos/60 + segundos/3600
    if direcao == 'S' or direcao == 'W':
        decimal *= -1

    # Converter para UTM
    if longitude:
        easting, northing, _, _ = utm.from_latlon(0, decimal)
    else:
        easting, northing, _, _ = utm.from_latlon(decimal, 0)

    # Formatar as coordenadas UTM
    if longitude:
        coordenada = f"{easting:.3f}E"
    else:
        coordenada = f"{northing:.3f}N"

    return coordenada

# Exemplo de uso da função
latitude_graus = 20
latitude_minutos = 0
latitude_segundos = 0.0
latitude_direcao = 'S'

longitude_graus = 54
longitude_minutos = 0
longitude_segundos = 0.0
longitude_direcao = 'W'

longitude = converter_geografico_para_utm(longitude_graus, longitude_minutos, longitude_segundos, longitude_direcao, longitude=True)
print(f"Longitude UTM: {longitude}")

latitude = converter_geografico_para_utm(latitude_graus, latitude_minutos, latitude_segundos, latitude_direcao)
print(f"Latitude UTM: {latitude}")
