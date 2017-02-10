<html>
<head ></head>
<title>EUROCONVERSOR 2.0</title>
<body>
<p>
    	<?php
    		
   		$euros=$_POST['entrada']; //obtenemos el valor introducido
		//comprobamos que "opcion" hemos seleccionado
   		if($_REQUEST['radio1']=="libras"){ 
			echo "Euros: ".$euros."€";
        		echo "<br>";
        		echo "Libras: ".$euros*0.850784."£";
			echo "</br>";    
    		}if($_REQUEST['radio1']=="dolares"){
        		echo "Euros: ".$euros."€";
			echo "<br>";
        		echo "Dolares: ".$euros*1.09."$";
			echo "</br>";  
    		}
    
    ?>
</p>
</body>
</html>
