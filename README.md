# danish_insulter
generates Danish insults

IaaS (Insults as a Service): [edderma.me](https://eddarma.me)
<br><br>

* [Insult](https://edderma.me/nederen) : `GET /nederen`
- `alliteration=true`
    - tries to use alliterations were possible
- `unique=true`
    - keeps insults unique to `id` param until the shortest word list is exhausted
- `id=uuid`
    - requests without `id` generate new uuid to log insults to
- `nolog=true`
    - does not log insult - cannot used together with `unique`

<br><br>
Example response
```json
{
    "error":null,
    "id":"4cfc42d8-284d-11ed-8b66-a7f2b74297e1",
    "insult":"du er kraftpetervæltemig frastødende, din groteske skidespræller"
}
```


Below list of insults has been created with `python insulter.py --log log.txt --unique` which uses each word exactly once until the shortest wordlist has been exhausted.<br>
The insulter always uses `amplifier.txt` to make sure that no two words with the same amplifier are used within one insult.

- du er kraftstejlme ful, din tumpede afskum
- du er edderrøveme uappetitlig, din forpulede klodsmajor
- du er edderfandme forbistret, din desperate kvælstofbacille
- du er fandenpuleme kreperlig, din harmdirrende knoldvækst
- du er kraftpeterpuleme uformelig, din rasende fedthalefår
- du er satanraspemig frastødende, din lunatiske lommemussolini
- du er denondelynemig rædderlig, din pløkåndssvage lurendrejer
- du er edderfandenfiseme vammel, din forbaskede svumpukkel
- du er fandenfløjtemig ikke fem potter pis værd, din sindssyge åndspygmæ
- du er edderhakkemig klam, din interplanetariske mandagsdessertør
- du er sørenjenseme grim, din debile glatnakke
- du er edderknasemig utiltalende, din vanvittige skruebrækker
- du er edderbrandbrølemig ildelugtende, din hysteriske trillebørsspekulant
- du er fandensparkemefløjtende modbydelig, din djævleblændte trompetsnegl
- du er skampetervæltemig grim som arvesynden, din balstyriske fedtemikkel
- du er edderbuttfuckemig elendig, din kvajede kanalje
- du er fandenpikeme nedrig, din kugleskøre jubeltorsk
- du er edderbukme underlødig, din furiøse paphoved
- du er eddersateme rædselsfuld, din splittertossede bøllefrø
- du er kraftedme tudegrim, din groteske hulepindsvin
- du er dælendytme ulækker, din deliriske torskehoved
- du er kraftpetervæltemig håbløs, din stiktossede pismyre
- du er saftsuseedderpeterhamresparkemig forfærdelig, din evnesvage kakerlak
- du er fandengalemig uæstetisk, din åndssløve stymper

The following list has been created with the `--alliteration` flag enabled:

- du er fandenfløjtemig forbistret, din pivhamrende paphoved
- du er fandeme forfærdelig, din interplanetariske båtnakke
- du er fandensparkemefløjtende uæstetisk, din lunatiske lurendrejer
- du er kraftpetervæltemig klam, din forpulede fedtemikkel
- du er saftsuseedderpeterhamresparkemig skummel, din åndssløve mandagsdessertør
- du er fandenpuleme fæl, din latterlige lommemussolini
- du er fandenpikeme forpjusket, din kugleskøre klodsmajor
- du er edderfandme elendig, din stjernetossede skidespræller
- du er skampetervæltemig styg, din desperate edderfugl
- du er eddermukme ulækker, din vanvittige vatnisse
- du er kraftknusme kreperlig, din barokke bøllefrø
- du er fandengalemig frastødende, din tumpede trillebørsspekulant
- du er eddersateme uappetitlig, din groteske glatnakke
- du er satanraspemig rædderlig, din åndssvage pikansjos
- du er eddermame muggen, din deliriske tyndskidspresser
- du er edderrøveme gyselig, din stiktossede spritbilist
- du er edderknasemig grim som arvesynden, din debile knoldvækst
- du er krafthelvede utiltalende, din djævleblændte pismyre
- du er edderbuttfuckemig ildelugtende, din pissehamrende pikhoved
- du er edderbrandbrølemig jordslået, din rivende røvbanan
- du er edderhakkemig grim som bare fanden, din mystiske møgfisse
- du er kraftpeterpuleme uformelig, din abstruse trompetsnegl
- du er satanraspemig skummel, din rekordagtige røvbanan


The insult wordlist is heavily inspired by the excellent musings of Captain Haddock.<br>
All wordlists have been made possible by the awesome feature "ord i nærheden" in the essential online dictionary [ordnet](https://ordnet.dk/).
