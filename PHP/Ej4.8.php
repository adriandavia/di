<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				chdir('fotos');
				$directorio = getcwd();
				$gestor = opendir($directorio);
				define ("TAM", 4);
				$n = 1; 
				$numero = 1; 
				$patron = "/^[[:digit:]]+$/";
				while (false !== ($nombre_fichero = readdir($gestor_dir))) {
					$ficheros[] = $nombre_fichero;
				}
				print_r($ficheros);
			?>
		</table>
	</body>
</html>
