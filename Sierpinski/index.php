<?php
function updateVariable($new_value) {
    $file_path = 'zadanie1.py';
    $file_data = file_get_contents($file_path);
    
    $start_pos = strpos($file_data, 'MAX = ');
    if ($start_pos !== false) {
        $end_pos = strpos($file_data, "\n", $start_pos);
        $old_line = substr($file_data, $start_pos, $end_pos - $start_pos);
        $new_line = "MAX = {$new_value}";
        $file_data = str_replace($old_line, $new_line, $file_data);
        
        file_put_contents($file_path, $file_data);
    }
}

function runScript() {
    $command = "python zadanie1.py";
    ob_start();
    passthru($command);
    $output = ob_get_clean();
    
    return $output;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['new_value']) && !empty($_POST['new_value'])) {
        updateVariable($_POST['new_value']);
        $output = runScript();
    } else {
        $output = "Wartość nie może być pusta";
    }
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
