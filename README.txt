Classe Python pour gérer le backpack Adafruit USB+Série LCD disponible
chez MCHobby.be

Fiche produit:
---> http://shop.mchobby.be/product.php?id_product=475
Voir notre tutoriel:
---> http://wiki.mchobby.be/index.php?title=LCD-USB-TTL

Fichiers:
  * lcdmtrx.py
		contient la classe LcdMatrix et EuropeLcdMatrix
  * lcdmtrx-FullTest.py 
    	TEST COMPLET. 
    	Pensez à modifier la ligne PORT_SERIE = '/dev/ttyACM1' pour référencer le bon port USB
  * lcdmtrx-WriteTest.py
		TEST RESTREIND centré sur l'affichage de texte. 
		Pensez à modifier la ligne PORT_SERIE = '/dev/ttyACM1' pour référencer le bon port USB
  * lcdmtrx-EuropeanTest.py
        *** EXPERIMENTAL ***    
		Utilise la classe EuropeLcdMatrix pour définir un charset francophile supportant
 		les caractères éèàç€ et une methode write_european() permettant d'afficher du 
		texte avec accentués. Toutes les méthodes de la classe LcdMatrix restent utilisable

MCHobby investit du temps et des ressources pour écrire de la 
documentation, du code et des exemples. 
Aidez nous à en produire plus en achetant vos produits chez MCHobby

=============================================================================
= Basé sur les travaux de Limor Freid qui se trouve ici:                    =
= Based on the work of Limor Freid that can be find here:
= https://github.com/adafruit/Adafruit-USB-Serial-RGB-Character-Backpack    =
=                                                                           =
= BSD license - identique à celle d'AdaFruit / indentical to AdaFruit's one =
=============================================================================
