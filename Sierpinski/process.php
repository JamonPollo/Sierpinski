<?php
// Funkcja do aktualizacji wartości zmiennej w skrypcie
function updateVariable($new_value) {
    $file_path = 'zadanie1.py';

    // Odczytaj zawartość pliku
    $file_data = file($file_path);

    // Zmieniamy wartość zmiennej MAX w kodzie
    foreach ($file_data as &$line) {
        if (strpos($line, 'MAX = ') !== false) {
            $line = "MAX = {$new_value}\n";
        }
    }

    // Zapisz nowe dane do pliku
    file_put_contents($file_path, implode('', $file_data));
}

// Uruchom skrypt Pythona i zwróć wynik
function runScript() {
    $new_value = $_POST['new_value'];
    $file_path = 'zadanie1.py';

    // Utwórz polecenie do wykonania
    $command = "python $file_path $new_value";

    // Wykonaj polecenie i przechwytuj wynik
    $output = shell_exec($command);

    // Zwróć wynik jako pojedynczy ciąg znaków
    return $output;
}

// Sprawdź, czy został przesłany formularz
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Zaktualizuj zmienną MAX w skrypcie
    updateVariable($_POST['new_value']);

    // Uruchom skrypt i otrzymaj wynik
    $output = runScript();
} else {
    $output = '';
}
?>

<!DOCTYPE html>
<html>
<body>
    <form method="POST">
        <label for="new_value">Nowa wartość dla MAX:</label><br>
        <input type="number" id="new_value" name="new_value" min="1"><br>
        <input type="submit" value="Zmień i uruchom skrypt">
    </form>
    <p>Wynik:</p>
    <pre><?php echo $output; ?></pre>
</body>
</html>
