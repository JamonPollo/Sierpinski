<?php
// Funkcja do aktualizacji wartości zmiennej w skrypcie
function updateVariable() 

{
    $new_value = $_POST['new_value'];

    $file_path = 'zadania/zadanie'.$_POST['numer_zadania'].'.py';
return file_get_contents($file_path);
}
// Sprawdź, czy został przesłany formularz
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    // Uruchom skrypt i otrzymaj wynik
    $output = updateVariable();
} else {
    $output = '';
}
?>
<?php echo $output; ?>
