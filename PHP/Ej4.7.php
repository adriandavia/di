<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				chdir('fotos'); //cambiamos al directorio fotos
				define ("TAM", 4); //definimos el tamaño 
				$fila = 1; 
				$numero = 1; 
				while ($fila <= TAM){  //bucle para las filas
					print "<tr>";
					for ($j = 1; $j <= TAM; $j++){ //bucle para las columnas
						print "<td>" . '<img src="/PHP/fotos/'.$numero.'.jpg"/>' . "</td>";
						$numero++;
					}
					print "</tr>";
					$fila++;
				}
			?>
		</table>
	</body>
</html>
