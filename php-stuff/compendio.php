<?php
    $image = $_REQUEST["image"];
    echo $image;
    $a = 2;
    $b = 5;
    $cmd = './tess3'." "."uploads/".$image;
    //$cmd = './tstr'." "."uploads/".$image;
    echo "<br>0".$cmd;
    //$cmd = './test'." ".$a." ".$b;
    $out = system($cmd, $retval);
    
    echo "<br>1".$retval;

    echo "<br>2".$out;
?>