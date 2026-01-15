nombre = input('Introduce tu nombre: ')
edad = input('Introduce tu edad: ')
direccion = input('Introduce tu direccion: ')
telefono = input('Introduce tu telefono: ')

lista = {'nombre': nombre,
         'edad': edad,
         'direccion': direccion,
         'telefono': telefono}
print(lista['nombre'], ' tiene ', lista['edad'], ' años, vive en', lista['direccion'], ' y su teléfono es', lista['telefono'])
