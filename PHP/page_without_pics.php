<?php
//Lataa www sivu ilman kuvia

//file komento noutaa tiedoston http-osoitteesta PHP:n taulukoksi
$sivun_sisalto_taulukko = file($url);
//tavallinen merkkijono
$sivun_sisalto = join('', $sivun_sisalto_taulukko);
//korvataan sivulla olevat kaikki <IMG merkkijonot <MIG merkkijonolla
$sivun_sisalto = str_replace("<IMG","<MIG",$sivun_sisalto);
//sama <img
$sivun_sisalto = str_replace("<img","<MIG",$sivun_sisalto);

print "$sivun_sisalto";
//calling: http://......php?url=http://www.google.com
?>