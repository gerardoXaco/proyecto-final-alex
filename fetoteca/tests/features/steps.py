# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

@step(u'Dado que ingreso mi usuario "([^"]*)" y contraseña "([^"]*)"')
def dado_que_ingreso_mi_usuario_group1_y_contrasena_group2(step, usuario, passwd):
    world.driver = webdriver.Chrome('chromedriver')
    world.driver.get('http://148.217.200.108/application/index.php?mod=usuarios&controlador=login')
    user= world.driver.find_element_by_name('username')
    contra = world.driver.find_element_by_name('password')

    user.send_keys(usuario)
    contra.send_keys(passwd)

@step(u'Cuando presiono el boton Ingresar')
def cuando_presiono_el_boton_ingresar(step):
    boton = world.driver.find_element_by_tag_name('button')
    boton.click()
    time.sleep(2)
@step(u'Entonces puedo ver el mensaje "([^"]*)"')
def entonces_puedo_ver_de_nuevo_la_pagina_de_login_group1(step, texto_esperado):
    texto = world.driver.find_element_by_tag_name('h1')
    assert texto.text == texto_esperado, \
    'El texto esperado '+texto_esperado+' no es igual a '+texto.text

@step(u'Entonces puedo ver el mensaje de bienvenida "([^"]*)"')
def entonces_puedo_ver_el_mensaje_de_bienvenida_group1(step, texto_esperado):
    texto = world.driver.find_element_by_tag_name('h1')
    assert texto.text == texto_esperado, \
    'El texto esperado '+texto_esperado+' no es igual a '+texto.text

   # boton = world.driver.find_element_by_class_name('dropdown-toggle').click()
    #logout = world.driver.find_element_by_partial_link_text('logout').click()


#Termina el feature de login
#----------------------
