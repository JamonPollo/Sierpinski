<?php
// Funkcja do aktualizacji wartości zmiennej w skrypcie
function updateVariable() 

{
    if(isset($_POST['MAX_value']))
    {
        $MAX_value = $_POST['MAX_value'];
    }else $MAX_value =''; 

    if(isset($_POST['MAXX_value']))
    {
        $MAXX_value = $_POST['MAXX_value'];
    }else $MAXX_value =''; 

    if(isset($_POST['MAXN_value']))
    {
        $MAXN_value = $_POST['MAXN_value'];
    }else $MAXN_value =''; 

    $file_path = 'zadania/zadanie'.$_POST['numer_zadania'].'.py';

    // Odczytaj zawartość pliku
    $file_data = file($file_path);

    // Zmieniamy wartość zmiennej MAX w kodzie
    if (!empty($MAX_value)){
    foreach ($file_data as &$line) {
        if (strpos($line, 'MAX = ') !== false) {
            $line = "MAX = {$MAX_value}\n";
        }

    } }

    if (!empty($MAXX_value)){
    foreach ($file_data as &$line) {
        if (strpos($line, 'MAXX = ') !== false) {
            $line = "MAXX = {$MAXX_value}\n";
        }
    }}

    if (!empty($MAXN_value)){
    foreach ($file_data as &$line) {
        if (strpos($line, 'MAXN = ') !== false) {
            $line = "MAXN = {$MAXN_value}\n";
        }
    }}

    // Zapisz nowe dane do pliku
    file_put_contents($file_path, implode('', $file_data));
    return file_get_contents($file_path);
}

// Uruchom skrypt Pythona i zwróć wynik
function runScript() {
    $new_value = $_POST['new_value'];
    $command = "python zadania/zadanie".$_POST['numer_zadania'].".py $new_value";
    
    // Przechwytuj wynik z stdout
    ob_start();
    passthru($command);
    $output = ob_get_clean();
    
    return $output;
}

// Sprawdź, czy został przesłany formularz
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Zaktualizuj zmienną MAX w skrypcie
    $output = updateVariable();
} else {
    $output = '';
}
?>
<?php echo $output; ?>
