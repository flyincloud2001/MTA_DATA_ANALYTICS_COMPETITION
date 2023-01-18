import worldcup
years = [2006, 2010,  2014, 2018]

countries = {"AF":"Afghanistan",
"AX":"Aland Islands",
"AL":"Albania",
"DZ":"Algeria",
"AS":"American Samoa",
"AD":"Andorra",
"AO":"Angola",
"AI":"Anguilla",
"AQ":"Antarctica",
"AG":"Antigua and Barbuda",
"AR":"Argentina",
"AM":"Armenia",
"AW":"Aruba",
"AU":"Australia",
"AT":"Austria",
"AZ":"Azerbaijan",
"BS":"Bahamas",
"BH":"Bahrain",
"BD":"Bangladesh",
"BB":"Barbados",
"BY":"Belarus",
"BE":"Belgium",
"BZ":"Belize",
"BJ":"Benin",
"BM":"Bermuda",
"BT":"Bhutan",
"BO":"Bolivia, Plurinational State of",
"BQ":"Bonaire, Sint Eustatius and Saba",
"BA":"Bosnia and Herzegovina",
"BW":"Botswana",
"BV":"Bouvet Island",
"BR":"Brazil",
"IO":"British Indian Ocean Territory",
"BN":"Brunei Darussalam",
"BG":"Bulgaria",
"BF":"Burkina Faso",
"BI":"Burundi",
"KH":"Cambodia",
"CM":"Cameroon",
"CA":"Canada",
"CV":"Cape Verde",
"KY":"Cayman Islands",
"CF":"Central African Republic",
"TD":"Chad",
"CL":"Chile",
"CN":"China",
"CX":"Christmas Island",
"CC":"Cocos (Keeling) Islands",
"CO":"Colombia",
"KM":"Comoros",
"CG":"Congo",
"CD":"Congo, The Democratic Republic of the",
"CK":"Cook Islands",
"CR":"Costa Rica",
"CI":"Côte d'Ivoire",
"HR":"Croatia",
"CU":"Cuba",
"CW":"Curaçao",
"CY":"Cyprus",
"CZ":"Czech Republic",
"DK":"Denmark",
"DJ":"Djibouti",
"DM":"Dominica",
"DO":"Dominican Republic",
"EC":"Ecuador",
"EG":"Egypt",
"SV":"El Salvador",
"GQ":"Equatorial Guinea",
"ER":"Eritrea",
"EE":"Estonia",
"ET":"Ethiopia",
"FK":"Falkland Islands (Malvinas)",
"FO":"Faroe Islands",
"FJ":"Fiji",
"FI":"Finland",
"FR":"France",
"GF":"French Guiana",
"PF":"French Polynesia",
"TF":"French Southern Territories",
"GA":"Gabon",
"GM":"Gambia",
"GE":"Georgia",
"DE":"Germany",
"GH":"Ghana",
"GI":"Gibraltar",
"GR":"Greece",
"GL":"Greenland",
"GD":"Grenada",
"GP":"Guadeloupe",
"GU":"Guam",
"GT":"Guatemala",
"GG":"Guernsey",
"GN":"Guinea",
"GW":"Guinea-Bissau",
"GY":"Guyana",
"HT":"Haiti",
"HM":"Heard Island and McDonald Islands",
"VA":"Holy See (Vatican City State)",
"HN":"Honduras",
"HK":"Hong Kong",
"HU":"Hungary",
"IS":"Iceland",
"IN":"India",
"ID":"Indonesia",
"IR":"Iran, Islamic Republic of",
"IQ":"Iraq",
"IE":"Ireland",
"IM":"Isle of Man",
"IL":"Israel",
"IT":"Italy",
"JM":"Jamaica",
"JP":"Japan",
"JE":"Jersey",
"JO":"Jordan",
"KZ":"Kazakhstan",
"KE":"Kenya",
"KI":"Kiribati",
"KP":"Korea, Democratic People's Republic of",
"KR":"Korea, Republic of",
"KW":"Kuwait",
"KG":"Kyrgyzstan",
"LA":"Lao People's Democratic Republic",
"LV":"Latvia",
"LB":"Lebanon",
"LS":"Lesotho",
"LR":"Liberia",
"LY":"Libya",
"LI":"Liechtenstein",
"LT":"Lithuania",
"LU":"Luxembourg",
"MO":"Macao",
"MK":"Macedonia, Republic of",
"MG":"Madagascar",
"MW":"Malawi",
"MY":"Malaysia",
"MV":"Maldives",
"ML":"Mali",
"MT":"Malta",
"MH":"Marshall Islands",
"MQ":"Martinique",
"MR":"Mauritania",
"MU":"Mauritius",
"YT":"Mayotte",
"MX":"Mexico",
"FM":"Micronesia, Federated States of",
"MD":"Moldova, Republic of",
"MC":"Monaco",
"MN":"Mongolia",
"ME":"Montenegro",
"MS":"Montserrat",
"MA":"Morocco",
"MZ":"Mozambique",
"MM":"Myanmar",
"NA":"Namibia",
"NR":"Nauru",
"NP":"Nepal",
"NL":"Netherlands",
"NC":"New Caledonia",
"NZ":"New Zealand",
"NI":"Nicaragua",
"NE":"Niger",
"NG":"Nigeria",
"NU":"Niue",
"NF":"Norfolk Island",
"MP":"Northern Mariana Islands",
"NO":"Norway",
"OM":"Oman",
"PK":"Pakistan",
"PW":"Palau",
"PS":"Palestinian Territory, Occupied",
"PA":"Panama",
"PG":"Papua New Guinea",
"PY":"Paraguay",
"PE":"Peru",
"PH":"Philippines",
"PN":"Pitcairn",
"PL":"Poland",
"PT":"Portugal",
"PR":"Puerto Rico",
"QA":"Qatar",
"RE":"Réunion",
"RO":"Romania",
"RU":"Russian Federation",
"RW":"Rwanda",
"BL":"Saint Barthélemy",
"SH":"Saint Helena, Ascension and Tristan da Cunha",
"KN":"Saint Kitts and Nevis",
"LC":"Saint Lucia",
"MF":"Saint Martin (French part)",
"PM":"Saint Pierre and Miquelon",
"VC":"Saint Vincent and the Grenadines",
"WS":"Samoa",
"SM":"San Marino",
"ST":"Sao Tome and Principe",
"SA":"Saudi Arabia",
"SN":"Senegal",
"RS":"Serbia",
"SC":"Seychelles",
"SL":"Sierra Leone",
"SG":"Singapore",
"SX":"Sint Maarten (Dutch part)",
"SK":"Slovakia",
"SI":"Slovenia",
"SB":"Solomon Islands",
"SO":"Somalia",
"ZA":"South Africa",
"GS":"South Georgia and the South Sandwich Islands",
"ES":"Spain",
"LK":"Sri Lanka",
"SD":"Sudan",
"SR":"Suriname",
"SS":"South Sudan",
"SJ":"Svalbard and Jan Mayen",
"SZ":"Swaziland",
"SE":"Sweden",
"CH":"Switzerland",
"SY":"Syrian Arab Republic",
"TW":"Taiwan, Province of China",
"TJ":"Tajikistan",
"TZ":"Tanzania, United Republic of",
"TH":"Thailand",
"TL":"Timor-Leste",
"TG":"Togo",
"TK":"Tokelau",
"TO":"Tonga",
"TT":"Trinidad and Tobago",
"TN":"Tunisia",
"TR":"Turkey",
"TM":"Turkmenistan",
"TC":"Turks and Caicos Islands",
"TV":"Tuvalu",
"UG":"Uganda",
"UA":"Ukraine",
"AE":"United Arab Emirates",
"GB":"United Kingdom",
"US":"United States",
"UM":"United States Minor Outlying Islands",
"UY":"Uruguay",
"UZ":"Uzbekistan",
"VU":"Vanuatu",
"VE":"Venezuela, Bolivarian Republic of",
"VN":"Viet Nam",
"VG":"Virgin Islands, British",
"VI":"Virgin Islands, U.S.",
"WF":"Wallis and Futuna",
"YE":"Yemen",
"ZM":"Zambia",
"ZW":"Zimbabwe"}
good = [184, 188, 187, 179, 183, 175, 188, 190, 186, 192, 187, 179, 183, 188, 187, 176, 177, 173, 180, 181, 183, 172, 174, 180, 170, 192, 190, 194, 189, 181, 176, 174, 184, 187, 190, 188, 178, 178, 178, 177, 188, 186, 180, 176, 173, 173, 184, 181, 183, 193, 184, 188, 180, 180, 188, 190, 187, 178, 184, 170, 179, 176, 189, 182, 171, 184, 176, 180, 178, 199, 189, 186, 186, 173, 181, 169, 193, 187, 183, 193, 197, 188, 190, 182, 194, 182, 173, 185, 186, 187, 190, 185, 180, 178, 193, 183, 199, 198, 190, 182, 185, 186, 182, 185, 193, 180, 186, 183, 181, 185, 172, 184, 182, 188, 177, 183, 175, 188, 186, 193, 172, 189, 174, 188, 176, 186, 184, 179, 181, 181, 180, 187, 180, 166, 180, 185, 175, 189, 176, 180, 182, 193, 191, 178, 178, 184, 180, 184, 195, 189, 180, 174, 173, 189, 173, 172, 178, 180, 191, 180, 171, 175, 171, 180, 169, 184, 183, 184, 180, 176, 175, 178, 178, 170, 177, 173, 173, 170, 171, 166, 185, 175, 170, 176, 183, 179, 181, 185, 191, 187, 186, 178, 174, 172, 185, 178, 182, 185, 183, 178, 181, 169, 178, 188, 181, 186, 185, 178, 186, 185, 178, 180, 178, 191, 183, 186, 176, 185, 175, 188, 182, 175, 177, 183, 175, 178, 178, 186, 179, 176, 177, 181, 190, 193, 186, 166, 180, 177, 190, 179, 180, 180, 180, 188, 179, 185, 184, 179, 189, 182, 174, 180, 188, 172, 187, 178, 181, 184, 193, 192, 191, 181, 192, 178, 191, 170, 184, 183, 186, 178, 188, 185, 190, 182, 177, 193, 171, 174, 188, 186, 179, 192, 179, 173, 173, 183, 182, 173, 175, 182, 180, 180, 174, 179, 175, 173, 183, 183, 191, 176, 192, 188, 188, 184, 176, 174, 187, 188, 176, 178, 186, 174, 171, 167, 172, 180, 187, 191, 181, 185, 185, 186, 191, 193, 188, 190, 186, 188, 191, 183, 170, 198, 192, 184, 189, 183, 180, 184, 187, 183, 176, 191, 180, 184, 176, 182, 186, 190, 180, 179, 175, 182, 188, 173, 185, 168, 177, 179, 165, 173, 185, 179, 185, 187, 171, 186, 172, 183, 189, 189, 195, 189, 193, 184, 185, 186, 184, 178, 189, 184, 176, 183, 165, 183, 189, 193, 193, 188, 177, 180, 180, 190, 179, 187, 182, 187, 188, 177, 170, 186, 178, 173, 175, 180, 170, 165, 183, 187, 188, 185, 190, 192, 192, 188, 182, 187, 182, 180, 187, 190, 187, 180, 180, 185, 184, 184, 175, 165, 189, 175, 178, 163, 185, 187, 170, 183, 189, 183, 176, 176, 183, 180, 179, 182, 178, 172, 175, 174, 178, 173, 173, 177, 170, 182, 165, 188, 185, 183, 180, 169, 187, 184, 191, 176, 185, 189, 180, 176, 177, 170, 173, 168, 175, 166, 178, 175, 175, 180, 185, 189, 180, 176, 169, 183, 188, 189, 185, 185, 178, 184, 188, 174, 173, 170, 178, 188, 175, 183, 180, 184, 186, 185, 171, 182, 190, 188, 190, 179, 176, 186, 195, 186, 177, 169, 173, 179, 182, 182, 184, 194, 188, 185, 171, 182, 190, 188, 190, 179, 176, 186, 195, 186, 177, 169, 173, 179, 182, 182, 184, 194, 188, 187, 187, 189, 187, 183, 187, 188, 178, 187, 185, 172, 180, 170, 172, 183, 170, 179, 177, 182, 191, 190, 180, 182, 178, 170, 189, 176, 182, 192, 188, 190, 194, 181, 184, 192, 171, 170, 180, 170, 183, 168, 173, 175, 186, 169, 188, 181, 188, 169, 185, 185, 183, 194, 187, 182, 183, 190, 182, 185, 191, 178, 183, 185, 179, 179, 179, 175, 183, 183, 172, 191, 193, 178, 196, 183, 193, 173, 178, 191, 188, 184, 180, 184, 180, 180, 173, 186, 183, 185, 184, 183, 183, 190, 180, 182, 181, 186, 186, 187, 177, 180, 185, 173, 196, 168, 177, 170, 177, 168, 183, 176, 183, 180, 186, 184]
good_countries = {"BR": "Brazil", "FR": "France", "SP": "Spain", "AR" : "Argentina"}
worldcup.datatocsv(worldcup.player(128113), "1.csv")
worldcup.datatocsv(worldcup.player(407775), "2.csv")
worldcup.datatocsv(worldcup.player(492), "3.csv")
worldcup.datatocsv(worldcup.player(127564), "4.csv")
worldcup.datatocsv(worldcup.player(184894), "5.csv")
worldcup.datatocsv(worldcup.player(66), "6.csv")
worldcup.datatocsv(worldcup.player(184813), "7.csv")
worldcup.datatocsv(worldcup.player(129501), "8.csv")
worldcup.datatocsv(worldcup.player(186320), "9.csv")
worldcup.datatocsv(worldcup.player(93948), "10.csv")
worldcup.datatocsv(worldcup.player(846), "11.csv")
worldcup.datatocsv(worldcup.player(184798), "12.csv")
worldcup.datatocsv(worldcup.player(186320), "13.csv")
worldcup.datatocsv(worldcup.player(185658), "14.csv")
worldcup.datatocsv(worldcup.player(1339), "15.csv")
worldcup.datatocsv(worldcup.player(1359), "16.csv")
new = open('new.csv', 'w')
for height in good:
    new.write(f'player, {height}\n')
new.close()
total = 0
num = 0

heights = open('2010 players.csv','w')
heights.write(f'{2010} best:, ')
for year in years:
    for country in good_countries.values():
        try:
            bestid = None
            bestgoals = 0
            squad = worldcup.squad(country, year)
            worldcup.datatocsv(squad, country + ".csv")
            squad = open(country + ".csv")
            firstline = squad.readline()
            firstlist = firstline.split(',')
            id = firstlist.index('player_id')
            goals = firstlist.index('goals')
            #player_list = []
            for player in squad:
                
                try:
                    # height = int(worldcup.player(player['player_id'])[0]['height'][0:3])
                    # total += height
                    # num += 1
                    # heights.write(f'{height}, ')
                    afile = open('afile.txt', 'w')
                   
                    
                    for line in squad:
                        lst = line.split(',')
                        if bestid == None or lst[goals] > bestgoals:
                            bestid = lst[id]
                            bestgoals = lst[goals]
                           
                        
                    
    
                except:
                    pass
            print( bestgoals)
        except:
            pass
            
#print (total/num)
heights.write(f'average height: {total/num}\n')
heights.close()
        
            