<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				define ("TAM", 10);
				$fila = 1; #variable para el numero de filas
				$numero = 1; #variable para imprimir números
				while ($fila <= TAM){ #bucle para las filas 
					print "<tr>";
					for ($j = 1; $j <= TAM; $j++){ #bucle para imprimir el numero del 1 al 100
						if ($j % 2 != 0)
							print "<td style = background-color:lightgrey;>" . $numero . "</td>";
						else
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
