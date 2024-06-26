<?php header('Content-Type: text/plain; charset=utf-8');

function runScript() {
    
    $command = "C:/Users/xande/AppData/Local/Programs/Python/Python312/python.exe zadania/zadanie".$_POST['numer_zadania'].".py";
    //$command = "C:/Users/xande/AppData/Local/Programs/Python/Python312/python.exe -V ";
    // Przechwytuj wynik z stdout
    ob_start();
    passthru($command);
  
    
    $output = (ob_get_clean());

    return $output."";
}

// Sprawdź, czy został przesłany formularz
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    // Uruchom skrypt i otrzymaj wynik
    $output = runScript();
} else {
    $output = '';
}
?>
<?php echo $output; ?>
