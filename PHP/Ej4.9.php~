<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				function extension(){
					chdir('fotos');
					$directorio = getcwd();
					$gestor = opendir($directorio);
					define ("TAM", 4);
					$gestor_dir = opendir($directorio);
					while (false !== ($nombre_fichero = readdir($gestor_dir))) {
					    $ficheros[] = $nombre_fichero;
					}
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
					return $validas;
				}
				$valida = extension();
				$numero = 0;
				$bucle2 = count($valida);
				$fila = 1;
				while ($fila <= TAM){
					print "<tr>";
					for ($j = 1; $j <= TAM; $j++){ 
						print "<td>" . '<a href=/PHP/fotos/'.$valida[$numero].'><img src="/PHP/minifotos/MINI-'.$valida[$numero].'"/></a>' . "</td>";
						$numero++;
					}
					print "</tr>";
					$fila++;
				}
			?>
		</table>
	</body>
</html>
