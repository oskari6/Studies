<html><head><title>Henkilötiedot</title></head>
<body>
    <h2>Henkilöt aakkosjärjestyksessä</h2>
<?php
//taulukkoon
$sivun_sisalto = file($url);
sort($sivun_sisalto);
//merkkijonoksi
$sivun_sisalto = join('<br \>', $sivun_sisalto);

print $sivun_sisalto;
//calling: http://......php?url=http://www.joku.fi/henkilöt.txt
?>

</body></html>