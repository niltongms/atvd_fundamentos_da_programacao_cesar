

horas = float(input("Digite as horas: "))
convert = input("Digite M se deseja converter para minutos ou S para segundos: ")
def convert_min(h):
   return h * 60

def convert_seg(h):
    return h*3600


if convert == 'M':
    convert_min
    print(f"{horas:.0f}h equivalem a {convert_min(horas):.0f}min")
elif convert == 'S':
    convert_seg
    print(f"{horas:.0f}h equivalem a {convert_seg(horas):.0f}seg")
else:
    print("Escolha uma das opções válidas")



    


