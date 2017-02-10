<html>
<head meta chrset=utf-8/>
<title>EUROCONVERSOR 1.0</title>
<body>
<p>
	<?php
		$dolares= $_POST['entrada']; //obtenemos el valor que hemos puesto.
		echo "Euros: ".$dolares."€\n"; 
		echo "<br>";
		echo "\nDolares: ".$dolares*1.08."$";
		echo "</br>";
	?>
</p>
</body>
</html>
