<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				$fila = 1; #variable para el numero de filas
				$numero = 1; #variable para imprimir números
				while ($fila <= 10){ #bucle para las filas 
					print "<tr>";
					for ($j = 1; $j <= 10; $j++){ #bucle para imprimir el numero del 1 al 100
						print "<td>" . $numero . "</td>";
						$numero++;
					}
					print "</tr>";
					$fila++;
				}
			?>
		</table>
	</body>
</html>
