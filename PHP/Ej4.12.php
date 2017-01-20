<?php
	$v[1]=10; 
	$v[30]=5;
	$v['e']=100;
	$v['hola']=45;
	foreach($v as $indice => $valor){ //coge cada variable y convierte v en indice
	echo "<p>";
	echo $indice." = ".$valor;
	echo"</p>";
	}
?>  
