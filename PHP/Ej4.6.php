<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				define ("TAM", 4); //definimos el tamaño por defecto 
				function potencia ($variable1, $variable2){ //funcion para sacar las potencias 
					$resultado = pow($variable1, $variable2);
					return $resultado;
				}
				$fila = 1; 
				$numero = 1; 
				while ($fila <= TAM){  //bucle para las filas de la tabla 
					print "<tr>";
					for ($j = 1; $j <= TAM; $j++){ //bucle para las columnas
						print "<td>" . potencia($numero, $j) . "</td>";
					}
					$numero++;
					print "</tr>";
					$fila++;
				}
			?>
		</table>
	</body>
</html>
