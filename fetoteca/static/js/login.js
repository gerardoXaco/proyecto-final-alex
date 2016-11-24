function hacerlogin(){
	var user = $("#name").val();
	var pass = $("#pass").val();

	if(user!="" && pass!=""){
		var json={};

		json.user=user;
		json.pass=pass;
		
		$.ajax({
			url:'validarConexion.php',
			type:'POST',
			data: JSON.stringify(json), //objeto que mando
			dataType: 'json',
			contenType: 'application/json',
			success: function(mensaje){
				if (mensaje.status=="ok") {
					window.location="index.php";
				}
				else{
					$("#mensajeIndex").html(mensaje.respuesta);
				}
			},
			error: function(){

			}

		});
	}
	else{
		$("#mensajeIndex").html("Faltó agregar Usuario o Contraseña");
	}
	
}