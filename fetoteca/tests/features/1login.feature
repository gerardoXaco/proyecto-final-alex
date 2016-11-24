Feature: Login de usuario
	Como usuario de la Fetoteca
	Quiero ingresar al Sistema de Foros
	Para poder comentar o crear un foro

	Scenario: Datos incorrectos
		Dado que ingreso mi usuario "fulanito" y contraseña "fulanito@123"
		Cuando presiono el boton Ingresar
		Entonces puedo ver de nuevo la pagina de login "Login"

	Scenario: Datos correctos
		Dado que ingreso mi usuario "fetoteca" y contraseña "fetoteca"
		Cuando presiono el boton Ingresar
		Entonces puedo ver el mensaje de bienvenida "foro"
