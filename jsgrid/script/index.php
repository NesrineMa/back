<?php
header('Access-Control-Allow-Origin: *');

exec("python AEI.py ", $output , $re);

var_dump($output);
  if ($re == 1) {
    return TRUE;
} else {
    return FALSE;
}   



?>  