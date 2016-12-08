﻿/**
 * @license Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.plugins.setLang( 'a11yhelp', 'nl', {
	title: 'Toegankelijkheidsinstructies',
	contents: 'Help-inhoud. Druk op ESC om dit dialoog te sluiten.',
	legend: [
		{
		name: 'Algemeen',
		items: [
			{
			name: 'Werkbalk tekstverwerker',
			legend: 'Druk op ${toolbarFocus} om naar de werkbalk te navigeren. Om te schakelen naar de volgende en vorige werkbalkgroep, gebruik TAB en SHIFT+TAB. Om te schakelen naar de volgende en vorige werkbalkknop, gebruik de PIJL RECHTS en PIJL LINKS. Druk op SPATIE of ENTER om een werkbalkknop te activeren.'
		},

			{
			name: 'Dialoog tekstverwerker',
			legend:
				'Inside a dialog, press TAB to navigate to the next dialog element, press SHIFT+TAB to move to the previous dialog element, press ENTER to submit the dialog, press ESC to cancel the dialog. When a dialog has multiple tabs, the tab list can be reached either with ALT+F10 or with TAB as part of the dialog tabbing order. With tab list focused, move to the next and previous tab with RIGHT and LEFT ARROW, respectively.'  // MISSING
		},

			{
			name: 'Contextmenu tekstverwerker',
			legend: 'Druk op ${contextMenu} of APPLICATION KEY om het contextmenu te openen. Schakel naar de volgende menuoptie met TAB of PIJL OMLAAG. Schakel naar de vorige menuoptie met SHIFT+TAB of PIJL OMHOOG. Druk op SPATIE of ENTER om een menuoptie te selecteren. Op een submenu van de huidige optie met SPATIE, ENTER of PIJL RECHTS. Ga terug naar de bovenliggende menuoptie met ESC of PIJL LINKS. Sluit het contextmenu met ESC.'
		},

			{
			name: 'Keuzelijst tekstverwerker',
			legend: 'In een keuzelijst, schakel naar het volgende item met TAB of PIJL OMLAAG. Schakel naar het vorige item met SHIFT+TAB of PIJL OMHOOG. Druk op SPATIE of ENTER om het item te selecteren. Druk op ESC om de keuzelijst te sluiten.'
		},

			{
			name: 'Elementenpad werkbalk tekstverwerker',
			legend: 'Druk op ${elementsPathFocus} om naar het elementenpad te navigeren. Om te schakelen naar het volgende element, gebruik TAB of PIJL RECHTS. Om te schakelen naar het vorige element, gebruik SHIFT+TAB or PIJL LINKS. Druk op SPATIE of ENTER om een element te selecteren in de tekstverwerker.'
		}
		]
	},
		{
		name: 'Opdrachten',
		items: [
			{
			name: 'Ongedaan maken opdracht',
			legend: 'Druk op ${undo}'
		},
			{
			name: 'Opnieuw uitvoeren opdracht',
			legend: 'Druk op ${redo}'
		},
			{
			name: 'Vetgedrukt opdracht',
			legend: 'Druk op ${bold}'
		},
			{
			name: 'Cursief opdracht',
			legend: 'Druk op ${italic}'
		},
			{
			name: 'Onderstrepen opdracht',
			legend: 'Druk op ${underline}'
		},
			{
			name: 'Link opdracht',
			legend: 'Druk op ${link}'
		},
			{
			name: 'Werkbalk inklappen opdracht',
			legend: 'Druk op ${toolbarCollapse}'
		},
			{
			name: 'Ga naar vorige focus spatie commando',
			legend: 'Druk ${accessPreviousSpace} om toegang te verkrijgen tot de dichtstbijzijnde onbereikbare focus spatie voor de caret, bijvoorbeeld: twee aangrenzende HR elementen. Herhaal de toetscombinatie om de verste focus spatie te bereiken.'
		},
			{
			name: 'Ga naar volgende focus spatie commando',
			legend: 'Druk ${accessNextSpace} om toegang te verkrijgen tot de dichtstbijzijnde onbereikbare focus spatie na de caret, bijvoorbeeld: twee aangrenzende HR elementen. Herhaal de toetscombinatie om de verste focus spatie te bereiken.'
		},
			{
			name: 'Toegankelijkheidshulp',
			legend: 'Druk op ${a11yHelp}'
		}
		]
	}
	],
	tab: 'Tab',
	pause: 'Pause',
	capslock: 'Caps Lock',
	escape: 'Escape',
	pageUp: 'Page Up',
	pageDown: 'Page Down',
	leftArrow: 'Pijl naar links',
	upArrow: 'Pijl omhoog',
	rightArrow: 'Pijl naar rechts',
	downArrow: 'Pijl naar beneden',
	insert: 'Invoegen',
	leftWindowKey: 'Linker Windows-toets',
	rightWindowKey: 'Rechter Windows-toets',
	selectKey: 'Selecteer toets',
	numpad0: 'Numpad 0',
	numpad1: 'Numpad 1',
	numpad2: 'Numpad 2',
	numpad3: 'Numpad 3',
	numpad4: 'Numpad 4',
	numpad5: 'Numpad 5',
	numpad6: 'Numpad 6',
	numpad7: 'Numpad 7',
	numpad8: 'Numpad 8',
	numpad9: 'Numpad 9',
	multiply: 'Vermenigvuldigen',
	add: 'Toevoegen',
	subtract: 'Aftrekken',
	decimalPoint: 'Decimaalteken',
	divide: 'Delen',
	f1: 'F1',
	f2: 'F2',
	f3: 'F3',
	f4: 'F4',
	f5: 'F5',
	f6: 'F6',
	f7: 'F7',
	f8: 'F8',
	f9: 'F9',
	f10: 'F10',
	f11: 'F11',
	f12: 'F12',
	numLock: 'Num Lock',
	scrollLock: 'Scroll Lock',
	semiColon: 'Puntkomma',
	equalSign: 'Is gelijk-teken',
	comma: 'Komma',
	dash: 'Koppelteken',
	period: 'Punt',
	forwardSlash: 'Slash',
	graveAccent: 'Accent grave',
	openBracket: 'Vierkant haakje openen',
	backSlash: 'Backslash',
	closeBracket: 'Vierkant haakje sluiten',
	singleQuote: 'Apostrof'
} );
