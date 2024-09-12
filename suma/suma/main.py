import flet as ft

def mostrar_suma(numero1, numero2, resultado):
    numero1=float(numero1.value.strip())
    numero2=float(numero2.value.strip())
    resultado=numero1+numero2
        resultado.value=(f"El valor de la suma es: {resultado}"),
    
def limpiar(e):
    numero1.value = ""
    numero2.value = "" 
    resultado.value= "Resultado: "
    
    page.update()
    page.dialog=dialog
    page.dialog.open=True
    page.update()
    def close_dialog(page):
        page.dialog.open=False
    page.update()
    def main(page: ft.Page):
        page.title("Suma de dos números")
        page.bgcolor="red"
        text field=ft.TextFiel
    
ft.app(main)
