#: dutch

{
    '__full__': 'dutch',

    '__maintainer__' : '@Mr Pleasant#6165',

    'blacklisted' : ''':x: Dit kanaal is op de zwarte lijst :x''',

    'help' : '''Ga voor meer informatie naar https://reminder-bot.com/help?lang=NL''',

    'no_perms_webhook' : '''**Waarschuwing!**: Om reminders in te stellen heb ik de `Manage Webhooks` toestemming nodig.''',

    'no_perms_general' : '''Actie verboden. Zorg er alstublieft voor dat ik de juiste toestemmingen heb.''',

    'no_perms_managed' : '''Je moet de `Manage Messages`/`Berichten Beheren` hebben, ofwel een rol die reminders naar dat kanaal kan zenden. Bespreek dit met je server admin, en overleg met hem/haar om het `{prefix}restrict` commando te gebruiken om bepaalde rollen toe te staan.''',

    'help_raw' : [
        ['''Herinnering Commando`s''', {
            '$natural' : 'Makkelijkere manier om reminders in te stellen. Gebruik het commando voor meer informatie.',

            '$del' : 'Verwijder de herinneringen en intervals op je server. Stuur een direct commando naar de bot als de herinneringen via DM`s zijn.',

            '$look [kanaal]' : 'Bekijk de herinneringen in een kanaal.',

            '$remind [gebruiker/kanaal] <tijd-tot-herinnering> <bericht>' : 'Gebruik alstublieft <code>$natural</code> in plaats van dit commando. Stel een herinnering in. Neemt de tijd in het formaat van [num][s/m/h/d], bijvoorbeeld 10s voor 10 seconden of 2s10m for 2 seconden en 10 minuten. Een precieze tijd kan gegeven worden als <code>dag/maand/jaar-uur:minuut:seconden</code>.',

            '$interval [gebruiker/kanaal] <tijd-tot-herinnering> <interval> <bericht>' : '<strong><a href="https://patreon.com/jellywx/">Patron Only.</a></strong> Gebruik alstublieft <code>$natural</code> in plaats van dit commando. Stel een interval in, waar het gegeven <code>bericht</code> elk <code>interval</code> verzonden wordt in elk gegeven <code>tijd-tot-herinnering</code> tijd. Neemt de tijd in een normale manier. Voorbeeld: <code>$interval 0s 20m Hello World!</code> verstuurt `Hello World!` elke 20 minuten naar het kanaal.',

            '$todo' : 'Commando voor het stellen van een to-do lijst. Gebruik <code>$todo help</code> voor meer informatie.',

            '$todos' : 'Identiek aan <code>$todo</code> maar voor server breed taakbeheer.',

            '$timezone' : 'Zet de tijdszone voor je server, voor makkelijkere setup in de database.',

             '$offset' : 'Verander de tijd in de volledige server bij een aangegeven tijd. (Handig om zomer/wintertijd aan te passen)'}],

        ['''Management Commando`s''', {

            '$lang <name>' : 'Verander de taal.',

            '$nudge <time>' : 'Sta nudging toe in het huidige kanaal. Dit maakt het mogelijk om alle toekomstige reminders tot de seconde te synchroniseren bij dingen zoals een in-game klok.',
 
            '$restrict [rol benoeming]' : 'Toevoegen / verwijderen van rollen om kanaalherinneringen en -intervallen te kunnen verzenden.',

            '$blacklist [kanaal-naam]' : 'Blokkeer of deblokkeer de mogelijkheid voor commando`s in een specifiek kanaal.',
        
        }],

        ['''Andere Commando`s''', {
            '$donate' : 'Toon informatie voor donaties.',

            '$prefix <string>' : 'Verander de prefix van de bot, standaard is dit $.',

            '$info' : 'Krijg informatie over de bot.',

            '$lang <name>' : 'Verander de taal.',

            '$clock' : 'Krijg de tijd in de server\'s huidige tijdzone.',
        }
        ]
    ],


    'info' : '''
Standaard prefix: `$`
Reset prefix: `@{user} prefix $`
Help: `{prefix}help`

**Welkom bij Reminder Bot!**

Ontwikkelaar: <@203532103185465344>
Icon: <@253202252821430272>
Nederlandse vertaling door: <@393139822044119051>
Vind me op  https://discord.jellywx.com en op https://github.com/JellyWX :)

Nodig de bot uit: https://discordapp.com/oauth2/authorize?client_id=349920059549941761&scope=bot&permissions=8
Gebruik het dashboard: https://reminder-bot.com/

*Als je vragen hebt over nieuwe functies, kom in de Discord server en stel hem!*
''',

    'donate' : '''
Zit je er over te denken om een maandelijkse bijdrage te doen? 
Klik op het adres hierbeneden voor mijn patreon en voor mijn discord server :D
https://www.patreon.com/jellywx

https://discord.jellywx.com

Hier is wat meer informatie:

Wanneer je een donatie doet zal Patreon jou automatisch een rankup geven in onze Discord server, als je je Discord en Patreon account al met elkaar gelinkt hebt.
Met je nieuwe rank kan je:
: Patreon-exclusieve commando `interval`
: Mogelijkheid om gekleurde embeds te gebruiken (In te stellen via het dashboard)
: Mogelijkheid om custom avatars bij herinneringen te gebruiken (Beschikbaar via het dashboard, $5 tier)

Aan iedereen die een Patron is: Bedankt :D Jullie zorgen er voor dat deze bot kan blijven voortbestaan.

Let er op dat je met de Discord server verbonden moet zijn om de Patreon rewards te krijgen.
''',

    'prefix' : {
        'no_argument' : '''
Gebruik dit commando als `@reminder-bot prefix <prefix>`
''',
        'success' : '''
Prefix veranderd naar {prefix}
''',

        'too_long' : '''Kies alstublieft een prefix uit die korter is dan 5 karakters.'''
    },

    'timezone' : {

        'no_argument' : '''
Gebruik:
    ```{prefix}timezone <naam>```
Example:
    ```{prefix}timezone Europe/London```
Alle ondersteunde tijdszones: https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee
Huidige tijdszone: {timezone}''',

        'no_timezone' : '''Tijdszone is niet herkend. Een volledige lijst is beschikbaar op https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'set' : '''Tijdszone is veranderd naar {timezone}. De huidige tijd zou {time} moeten zijn.''',
    },

    'restrict' : {

        'disabled' : '''De herinnering toestemmingen voor de rollen zijn verwijderd.''',

        'enabled' : '''De herinnering toestemmingen voor de rollen zijn toegevoegd.''',

        'allowed' : '''Toegestane rollen: {}''',

        'help' : '''Vermeld alstublieft de rollen waaarvan je de toestemmingen aan wil passen.'''
    },

    'remind' : {
        'no_argument' : '''
Gebruik:
    ```{prefix}remind [kanaal/gebruiker] <tijd tot of tijd wanneer> <bericht>```
Voorbeeld:
    ```{prefix}remind #general 10s Hello world!```
    ```{prefix}remind 10:30 Het is n 10:30.```''',

        'invalid_tag' : '''De locatie van de tag is niet gevonden.''',

        'invalid_time' : '''Zorg dat de tijd in het bericht als vorm heeft [num][s/m/h/d][num][s/m/h/d] etc. danwel `dag/maand/jaar-uur:minuut:seconde`.''',

        'long_time' : '''Zorg dat de tijd niet verder dan 50 jaar in de toekomst is!''',

        'success' : '''Nieuwe herinnering geregistreerd voor {location} in {offset} seconden. Als je deze herinnering wilt verwijderen, gebruik dan `$del`.'''
    },

    'interval' : {
        'no_argument' : '''
Gebruik:
    ```{prefix}interval [kanaal/gebruiker] <tijd tot of tijd wanneer> <interval> <bericht>```
Voorbeeld:
    ```{prefix}interval #general 9:30 1d Goede morgen!```
    ```{prefix}interval 0s 10s Dit zal aardig vervelend worden!```''',

        'invalid_interval' : '''Zorg dat het interval wat je gegeven hebt als vorm heeft [num][s/m/h/d][num][s/m/h/d] etc. met geen spaties, bijvoorbeeld 10s voor 10 seconden of 10s12m15h1d voor 10 seconden, 12 minuten, 15 uur en 1 dag.''',

        'long_interval' : '''Zorg dat het interval gegeven niet langer is dan 50 jaar!''',

        'short_interval' : '''Zorg dat je interval tijd langer is dan {min_interval} seconden.''',

        'donor' : '''Je moet een Patron zijn (donating 2$ of meer) om toegang tot dit commando te krijgen! Typ `{prefix}donate` om meer informatie te krijgen.''',

    },

    'natural' : {
        'no_argument' : '''
**Nieuw** De optie om natuurlijke tekst te typen!
Voorbeelden:
    ```{prefix}natural in 10 minuten verstuur Hello World! naar #general```
    ```{prefix}natural om 18:00 verstuur Het grote evenement is begonnen!```
    ```{prefix}natural op 16 juli om 14:00 verstuur Subs De reset is vandaag! naar #subs```
    ```{prefix}natural verstuur nu 10 minuten zijn voorbij! elke 10 minuten naar #timer```
Trefwoorden:
    `verstuur` : Definieer het bericht
    `iedere` : Definieer het interval van het bericht, bijvoorbeeld iedere 10 minuten
    `naar` : Definieer de locatie waar het bericht naar toe verzonden moet worden
Gebruik:
    ```{prefix}natural <tijdsverklaring> verstuur <bericht> [interval definitie] naar [#kanaal/@gebruiker]```
    ''',

        'invalid_time' : '''Het is niet gelukt om een correcte tijd te vinden. Probeer om het zo duidelijk mogelijk te maken, bijvoorbeeld `16 juli` of `in 20 minuten`''',

        'long_time' : '''Dat is een lange tijd! Zorg dat je reminder binnen 50 jaar is.''',

        'send' : ''' verstuur ''',

        'to' : ''' naar ''',

        'every' : ''' iedere '''

    },

    'del' : {
        'listing' : '''De lijst met herinneringen wordt weergegeven... (Het kan even duren, wacht alstublieft op het  "List (1,2,3...)" bericht).''',

        'listed' : '''List (1,2,3...) de herinneringen die je wilt verwijderen, of typ iets anders om te stoppen.''',

        'count' : '''{} herinneringen zijn verwijderd!'''
    },

    'look' : {
            
        'listing' : '''De lijst met herinneringen voor het gespecificeerde kanaal worden weergegeven...''',
            
        'inter' : '''komt eerstvolgend voor op''',
            
        'no_reminders' : '''Geen herinneringen in het gespecificeerde kanaal.''',
    },

    'todo' : {

        'add' : '''*Gebruik `{prefix}{command} add <message>` om een item toe te voegen op je TODO lijst, of gebruik  `{prefix}{command} help` voor meer commando`s!*''',

        'added' : ''' \'{name}\' is toegevoegd tot de TODO!''',

        'removed' : ''' \'{}\' is verwijderd van de TODO!''',

        'error_value' : '''Het item om te verwijderen moet een nummer zijn. Je kan de genummerde TODO`s vinden door `{prefix}{command}` te gebruiken''',

        'error_index' : '''Het nummer om te verwijderen is niet gevonden. Zit je in de goede TODO lijst?''',

        'help' : '''Om de TODO commando`s te gebruiken, gebruik `{prefix}{command} add <bericht>`, `{prefix}{command} remove <bericht>`, `{prefix}{command} clear` and `{prefix}{command}` to add to, remove from, clear or view your todo list.''',
##WIP
        'cleared' : '''De TODO lijst is geleegd!'''
    },

    'blacklist' : {
        'removed_from' : '''De gegeven kanalen zijn verwijderd van de balcklist.''',

        'added_from' : '''De gegeven kanalen zijn toegevoegd aan de blacklist.''',

        'removed' : '''Het huidige kanaal is verwijderd van de blacklist.''',

        'added' : '''Het huidige kanaal is toegevoegd aan de blacklist.'''

    },

    'lang' : {

        'invalid' : '''Talen:
{}''',

        'set' : '''Taal is nu Nederlands.''',
    },

    'clock' : {
        'time' : '''De huidge tijd is {}.''',
    },
    
    'offset' : {

        'invalid_time' : '''Zorg dat je een tijd geeft die een format heeft als [num][s/m/h/d][num][s/m/h/d]''',

        'success' : '''Alle reminders zijn verschoven met {} seconden''',

    },
}
