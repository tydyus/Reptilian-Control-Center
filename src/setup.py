from cx_Freeze import setup, Executable


# On appelle la fonction setup

setup(

    name = "Reptilian_Control_Center",

    version = "0.1",

    description = "Controlé le monde depuis votre poste de controle. //JamVersion//ld38",

    executables = [Executable("main.py")],

)
