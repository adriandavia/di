<?php
	$numero = 1;
	$cont = 0;
	while ($cont < 10){ #bucle para sacar los 10 primeros pares
		if ($numero % 2 == 0){ #comprobamos si son pares y añadimos 
			$array[$cont] = $numero;
			print "<br>".$array[$cont]."</br>";
			$cont++; #controla en que parte del bucle nos encontramos
		}
		$numero++;
	}
?>

