#!/usr/bin/python
#-*- coding: utf8 -*-
'''
TEST EUROPEEN - AFFICHAGE DE TEXTE  ACCENTUE de la classe Python 
  LcdMatrix servant à gérer le backpack Adafruit USB+Série LCD 
  disponible chez MCHobby.be

Fiche produit:
---> http://shop.mchobby.be/product.php?id_product=475
Voir notre tutoriel:
---> http://wiki.mchobby.be/index.php?title=LCD-USB-TTL

MCHobby investit du temps et des ressources pour écrire de la 
documentation, du code et des exemples. 
Aidez nous à en produire plus en achetant vos produits chez MCHobby

Basé sur les travaux de Limor Freid qui se trouve ici:
https://github.com/adafruit/Adafruit-USB-Serial-RGB-Character-Backpack

BSD license - identique à celle d'AdaFruit
------------------------------------------------------------------------
History:
  02 aug 2014 - Dominique - Version 0.1
'''

from lcdmtrx import *
import sys
import time

PORT_SERIE = '/dev/ttyACM0' #identification du port série sur lequel le LCD USB est connecté

LCD_COLS = 16 # Taille du LCD 16 caractères x 2 lignes
LCD_ROWS = 2

def do_lcd_european_test():
	#lcd = LcdMatrix( PORT_SERIE )
	lcd = EuropeLcdMatrix( PORT_SERIE )
	
	# === CREATION ET STOCKAGE CARACTERES EUROPEENs ====================
	BANK = 4 # Bank dans laquelle il faut stocker les caractères Europeen.
	lcd.save_european_charset_to_bank( BANK )
	lcd.load_custom_char_from_bank( BANK ) 
	
	# === AFFICHAGE AVEC CARACTERE EUROPEEN ============================
	# Initialiser la taille du LCD (et sauver dans l'EEPROM)
	lcd.set_lcd_size( LCD_COLS, LCD_ROWS )
	lcd.clear_screen()
	
	# === PREPARATION LCD ==============================================
	# Activer/désactiver le rétro-éclairage
	lcd.activate_lcd( True );
	
	# Constrat par défaut
	lcd.contrast()

	# Luminosité max + couleur RGB
	lcd.brightness( 255 )
	
	# Couleur RBG 
	lcd.color( 10, 240, 10 )
    	
    # Auto Scroll 
	lcd.autoscroll( True )

	# === AFFICHAGE AVEC CARACTERE EUROPEEN ============================
	lcd.clear_screen()
	lcd.write( chr( CHAR_EGRAVE ) ) # è
	lcd.write( chr( CHAR_EACUTE ) ) # é
	lcd.write( chr( CHAR_ECIRC  ) ) # ê
	lcd.write( chr( CHAR_CEDIL  ) ) # ç
	lcd.write( chr( CHAR_AGRAVE ) ) # à
	lcd.write( chr( CHAR_EURO   ) ) # € 
	time.sleep(2)
	
	# === Affichage d'un chaine avec caractères Européen ===============
	# Ecrire une chaine de caractère en faisant une translation des 
	# caractères spéciaux. 
	# Attention: la bank des caractères spéciaux doit être définie et 
	#            chargée en mémoire
	lcd.clear_screen()
	lcd.write_european( u'La fête à\rFrançoise,' )
	time.sleep(2)
	lcd.write_european( u'\rc\'est celle que' )
	time.sleep(2)
	lcd.write_european( u'\rje préfère :-)' )
	time.sleep(3)
	
	# === Afficher un total ============================================
	lcd.clear_screen()
	montant = 153.2 
	lcd.write_european( u'Montant:\r%.2f €' % (montant) )
	time.sleep( 3 )
	
	# === Fin ===
	lcd.clear_screen()
	lcd.write( 'Voila...\rc\'est fini!' )
	
if __name__ == '__main__':
	do_lcd_european_test()
