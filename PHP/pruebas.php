<?php
//Forma de sacar extensiones
$archivo = "leonpurpura.mp3"; 
$trozos = explode(".", $archivo); 
$extension = end($trozos); 
print $extension . "\n";  

//Recorrer archivos 
chdir('fotos');
$directorio = getcwd();
$gestor_dir = opendir($directorio);
while (false !== ($nombre_fichero = readdir($gestor_dir))) {
    $ficheros[] = $nombre_fichero;
}
 
sort($ficheros);
 
print_r($ficheros);
?>

