<?php
//Forma de sacar extensiones
$archivo = "leonpurpura.mp3"; 
$trozos = explode(".", $archivo); 
$extension = end($trozos); 
echo '<br>';
print $extension;  
echo '</br>';

//Recorrer archivos 
chdir('fotos');
$directorio = getcwd();
$gestor_dir = opendir($directorio);
while (false !== ($nombre_fichero = readdir($gestor_dir))) {
    $ficheros[] = $nombre_fichero;
}
 
sort($ficheros);
echo '<br>';
print $ficheros[2];
echo '</br>';

//comprobar extension de un array 
$bucle = count($ficheros);
$i = 0;
while ($i < $bucle){
	$comprobar = $ficheros[$i];
	$trozo = explode (".", $comprobar);
	$extensio = end($trozo);
	
	if ($extensio == "jpg"){
		$validas[] = $ficheros[$i];
	}else if ($extensio == "gif"){
		$validas[] = $ficheros[$i];
	}else if ($extensio == "bmp"){
		$validas[] = $ficheros[$i];
	}else if ($extensio == "png"){
		$validas[] = $ficheros[$i];
	}
	$i++;
	$comprobar = "";
}
echo '<br>';
print_r($validas);
echo '</br>';
?>

