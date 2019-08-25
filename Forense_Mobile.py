#!/bin/python3
from guizero import App, Text, TextBox, PushButton
import os

def backup_camera():
    os.system("./ADB_Backup")
    print("Backup Created")

def delete_backup():
    os.system('rm -r Backup')
    print("Backup Deleted")

def Analyse_Camera_Geolocation():
    os.system("./GeoPhoto")
    os.system("./Plot_Points")
    os.system("viking Backup/tmp/Viking.vik")
    print("Backup Analysed")

def Create_Report():
    os.system("./Create_Report")
    print("Report Created")

app = App(title="GSI - Forense em Smartphone", layout="grid", height=320, width=450)

backup = PushButton(app, command=backup_camera, text="ADB Backup Camera", grid=[1,1], height=8, width=25)
backup = PushButton(app, command=delete_backup, text="Deletar Backup anterior",grid=[2,1], height=8, width=25)
backup = PushButton(app, command=Analyse_Camera_Geolocation, text="Analisar Camera Geolocalizacao", grid=[2,2], height=8, width=25)
backup = PushButton(app, command=Create_Report, text="Criar Relatorio", grid=[1,2], height=8, width=25)

app.display()
