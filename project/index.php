<?php
	$a =1;
    $b =6;
    echo '<pre>';

    // Outputs all the result of shellcommand "ls", and returns
    // the last output line into $last_line. Stores the return value
    // of the shell command in $retval.
    $cmd = './test'." ".$a." ".$b; 
    $last_line = system($cmd, $retval);
    // Printing additional info
    echo '
    </pre>
    <hr />Last line of the output: ' . $last_line . '
    <hr />Return value: ' . $retval;
    
?>