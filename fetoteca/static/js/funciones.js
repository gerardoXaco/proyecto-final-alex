function eliminarMentor(id) {
	//window.location='{% url "eliminar_mentor" pk=mentor.id %}'
	var form = document.forms[0];
	form.id_mentor.value=id;
	form.submit();

}