TERRITORY_RECORDS_PER_PAGE = 50

COMPANY_OPTIONS = (('IC', 'Infonex Inc'),
                   ('IT', 'INX-Training'),
                   ('IU', 'Infonex (USA) Inc.'))

BILLING_CURRENCY = (('CAD', 'CAD'),
                    ('USD', 'USD'))

CONTACT_CHOICES = (
    ('Pitch', 'Sales Pitch (Phone)'),
    ('EPitch', 'Sales Pitch (Email)'),
    ('Followup', 'Follow-up Call'),
    ('Email', 'Follow-up Email'),
    ('Marketing', 'Marketing Email'),
    ('Registration', 'Delegate registration'),
    ('Speaker', 'Speaker confirmation'),
    ('Sponsor', 'Sponsor booking'),
    ('Research', 'PD Research Call')
)

GEO_CHOICES = (
    ('East', 'East'),
    ('West', 'West'),
    ('Maritimes/East', 'Maritimes'),
    ('USA', 'USA'),
    ('Other', 'Other Foreign'),
    ('Unknown', 'Unknown'),
)

CAT_CHOICES = (
    ('HR', 'HR'),
    ('FIN', 'FIN'),
    ('Industry', 'Industry'),
    ('Aboriginal', 'Aboriginal'),
    ('Gov', 'Gov'),
    ('USA', 'USA'),
    ('NA', 'None'),
)

DIV_CHOICES = (
    ('1', '1 - Misc'),
    ('2', '2 - Misc'),
    ('3', '3 - Misc'),
    ('4', '4 - Misc'),
    ('5', '5 - Misc'),
    ('6', '6 - Misc'),
    ('A1', '1 - Accounting'),
    ('A2', '2 - Accounting'),
    ('A3', '3 - Accounting'),
    ('Aboriginal', 'Aboriginal'),
    ('FED 1', 'FED 1'),
    ('FED 2', 'FED 2'),
    ('FED 3', 'FED 3'),
    ('FED 4', 'FED 4'),
    ('USA', 'USA'),
    ('NA', 'Not Determined'),
)

AC_DICT = {
    '201': 'NJ',
    '202': 'DC',
    '203': 'CT',
    '204': 'MB',
    '205': 'AL',
    '206': 'WA',
    '207': 'ME',
    '208': 'ID',
    '209': 'CA',
    '210': 'TX',
    '212': 'NY',
    '213': 'CA',
    '214': 'TX',
    '215': 'PA',
    '216': 'OH',
    '217': 'IL',
    '218': 'MN',
    '219': 'IN',
    '220': 'OH',
    '224': 'IL',
    '225': 'LA',
    '226': 'ON',
    '227': 'MD',
    '228': 'MS',
    '229': 'GA',
    '231': 'MI',
    '234': 'OH',
    '236': 'BC',
    '239': 'FL',
    '240': 'MD',
    '242': 'BAHAMAS',
    '246': 'BARBADOS',
    '248': 'MI',
    '249': 'ON',
    '250': 'BC',
    '251': 'AL',
    '252': 'NC',
    '253': 'WA',
    '254': 'TX',
    '256': 'AL',
    '260': 'IN',
    '262': 'WI',
    '264': 'ANGUILLA',
    '267': 'PA',
    '268': 'ANTIGUA/BARBUDA',
    '269': 'MI',
    '270': 'KY',
    '272': 'PA',
    '274': 'WI',
    '276': 'VA',
    '281': 'TX',
    '283': 'OH',
    '284': 'BRITISH VIRGIN ISLANDS',
    '289': 'ON',
    '301': 'MD',
    '302': 'DE',
    '303': 'CO',
    '304': 'WV',
    '305': 'FL',
    '306': 'SK',
    '307': 'WY',
    '308': 'NE',
    '309': 'IL',
    '310': 'CA',
    '312': 'IL',
    '313': 'MI',
    '314': 'MO',
    '315': 'NY',
    '316': 'KS',
    '317': 'IN',
    '318': 'LA',
    '319': 'IA',
    '320': 'MN',
    '321': 'FL',
    '323': 'CA',
    '325': 'TX',
    '327': 'AR',
    '330': 'OH',
    '331': 'IL',
    '332': 'NY',
    '334': 'AL',
    '336': 'NC',
    '337': 'LA',
    '339': 'MA',
    '340': 'US VIRGIN ISLANDS',
    '343': 'ON',
    '345': 'CAYMAN ISLANDS',
    '346': 'TX',
    '347': 'NY',
    '351': 'MA',
    '352': 'FL',
    '360': 'WA',
    '361': 'TX',
    '364': 'KY',
    '365': 'ON',
    '380': 'OH',
    '385': 'UT',
    '386': 'FL',
    '401': 'RI',
    '402': 'NE',
    '403': 'AB',
    '404': 'GA',
    '405': 'OK',
    '406': 'MT',
    '407': 'FL',
    '408': 'CA',
    '409': 'TX',
    '410': 'MD',
    '412': 'PA',
    '413': 'MA',
    '414': 'WI',
    '415': 'CA',
    '416': 'ON',
    '417': 'MO',
    '418': 'QC',
    '419': 'OH',
    '423': 'TN',
    '424': 'CA',
    '425': 'WA',
    '430': 'TX',
    '431': 'MB',
    '432': 'TX',
    '434': 'VA',
    '435': 'UT',
    '437': 'ON',
    '438': 'QC',
    '440': 'OH',
    '441': 'BERMUDA',
    '442': 'CA',
    '443': 'MD',
    '447': 'IL',
    '450': 'QC',
    '458': 'OR',
    '463': 'IN',
    '464': 'IL',
    '469': 'TX',
    '470': 'GA',
    '473': 'GRENADA',
    '475': 'CT',
    '478': 'GA',
    '479': 'AR',
    '480': 'AZ',
    '484': 'PA',
    '501': 'AR',
    '502': 'KY',
    '503': 'OR',
    '504': 'LA',
    '505': 'NM',
    '506': 'NB',
    '507': 'MN',
    '508': 'MA',
    '509': 'WA',
    '510': 'CA',
    '512': 'TX',
    '513': 'OH',
    '514': 'QC',
    '515': 'IA',
    '516': 'NY',
    '517': 'MI',
    '518': 'NY',
    '519': 'ON',
    '520': 'AZ',
    '530': 'CA',
    '531': 'NE',
    '534': 'WI',
    '539': 'OK',
    '540': 'VA',
    '541': 'OR',
    '548': 'ON',
    '551': 'NJ',
    '557': 'MO',
    '559': 'CA',
    '561': 'FL',
    '562': 'CA',
    '563': 'IA',
    '564': 'WA',
    '567': 'OH',
    '570': 'PA',
    '571': 'VA',
    '573': 'MO',
    '574': 'IN',
    '575': 'NM',
    '579': 'QC',
    '580': 'OK',
    '581': 'QC',
    '585': 'NY',
    '586': 'MI',
    '587': 'AB',
    '601': 'MS',
    '602': 'AZ',
    '603': 'NH',
    '604': 'BC',
    '605': 'SD',
    '606': 'KY',
    '607': 'NY',
    '608': 'WI',
    '609': 'NJ',
    '610': 'PA',
    '612': 'MN',
    '613': 'ON',
    '614': 'OH',
    '615': 'TN',
    '616': 'MI',
    '617': 'MA',
    '618': 'IL',
    '619': 'CA',
    '620': 'KS',
    '623': 'AZ',
    '626': 'CA',
    '628': 'CA',
    '629': 'TN',
    '630': 'IL',
    '631': 'NY',
    '636': 'MO',
    '639': 'SK',
    '641': 'IA',
    '646': 'NY',
    '647': 'ON',
    '649': 'TURKS & CAICOS',
    '650': 'CA',
    '651': 'MN',
    '657': 'CA',
    '658': 'JAMAICA',
    '659': 'AL',
    '660': 'MO',
    '661': 'CA',
    '662': 'MS',
    '664': 'MONTSERRAT',
    '667': 'MD',
    '669': 'CA',
    '671': 'GU',
    '678': 'GA',
    '679': 'MI',
    '680': 'NY',
    '681': 'WV',
    '682': 'TX',
    '684': 'AS',
    '689': 'FL',
    '701': 'ND',
    '702': 'NV',
    '703': 'VA',
    '704': 'NC',
    '705': 'ON',
    '706': 'GA',
    '707': 'CA',
    '708': 'IL',
    '709': 'NL',
    '712': 'IA',
    '713': 'TX',
    '714': 'CA',
    '715': 'WI',
    '716': 'NY',
    '717': 'PA',
    '718': 'NY',
    '719': 'CO',
    '720': 'CO',
    '721': 'ST MAARTEN',
    '724': 'PA',
    '725': 'NV',
    '727': 'FL',
    '730': 'IL',
    '731': 'TN',
    '732': 'NJ',
    '734': 'MI',
    '737': 'TX',
    '740': 'OH',
    '743': 'NC',
    '747': 'CA',
    '754': 'FL',
    '757': 'VA',
    '758': 'ST. LUCIA',
    '760': 'CA',
    '762': 'GA',
    '763': 'MN',
    '765': 'IN',
    '767': 'DOMINICA',
    '769': 'MS',
    '770': 'GA',
    '772': 'FL',
    '773': 'IL',
    '774': 'MA',
    '775': 'NV',
    '778': 'BC',
    '779': 'IL',
    '780': 'AB',
    '781': 'MA',
    '782': 'NS/PEI',
    '784': 'ST. VINCENT & GRENADINES',
    '785': 'KS',
    '786': 'FL',
    '787': 'PUERTO RICO',
    '801': 'UT',
    '802': 'VT',
    '803': 'SC',
    '804': 'VA',
    '805': 'CA',
    '806': 'TX',
    '807': 'ON',
    '808': 'HI',
    '809': 'DOMINICAN REPUBLIC',
    '810': 'MI',
    '812': 'IN',
    '813': 'FL',
    '814': 'PA',
    '815': 'IL',
    '816': 'MO',
    '817': 'TX',
    '818': 'CA',
    '819': 'QC',
    '825': 'AB',
    '828': 'NC',
    '829': 'DOMINICAN REPUBLIC',
    '830': 'TX',
    '831': 'CA',
    '832': 'TX',
    '843': 'SC',
    '845': 'NY',
    '847': 'IL',
    '848': 'NJ',
    '849': 'DOMINICAN REPUBLIC',
    '850': 'FL',
    '854': 'SC',
    '856': 'NJ',
    '857': 'MA',
    '858': 'CA',
    '859': 'KY',
    '860': 'CT',
    '862': 'NJ',
    '863': 'FL',
    '864': 'SC',
    '865': 'TN',
    '867': 'YK/NT/NU',
    '868': 'TRINIDAD & TOBAGO',
    '869': 'ST. KITTS & NEVIS',
    '870': 'AR',
    '872': 'IL',
    '873': 'QC',
    '876': 'JAMAICA',
    '878': 'PA',
    '901': 'TN',
    '902': 'NS/PEI',
    '903': 'TX',
    '904': 'FL',
    '905': 'ON',
    '906': 'MI',
    '907': 'AK',
    '908': 'NJ',
    '909': 'CA',
    '910': 'NC',
    '912': 'GA',
    '913': 'KS',
    '914': 'NY',
    '915': 'TX',
    '916': 'CA',
    '917': 'NY',
    '918': 'OK',
    '919': 'NC',
    '920': 'WI',
    '925': 'CA',
    '928': 'AZ',
    '929': 'NY',
    '930': 'IN',
    '931': 'TN',
    '934': 'NY',
    '936': 'TX',
    '937': 'OH',
    '938': 'AL',
    '939': 'PUERTO RICO',
    '940': 'TX',
    '941': 'FL',
    '947': 'MI',
    '949': 'CA',
    '951': 'CA',
    '952': 'MN',
    '954': 'FL',
    '956': 'TX',
    '959': 'CT',
    '970': 'CO',
    '971': 'OR',
    '972': 'TX',
    '973': 'NJ',
    '975': 'MO',
    '978': 'MA',
    '979': 'TX',
    '980': 'NC',
    '984': 'NC',
    '985': 'LA',
    '986': 'ID',
    '989': 'MI',
}

STATE_PROV_TUPLE =  (
    ('', 'Any'),
    ('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'),
    ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'),
    ('YK/NT/NU', 'Northwest Territories'), ('NS/PEI', 'Nova Scotia'),
    ('YK/NT/NU', 'Nunavut'), ('ON', 'Ontario'),
    ('NS/PEI', 'Prince Edward Island'), ('QC', 'Quebec'),
    ('SK', 'Saskatchewan'), ('YK/NT/NU', 'Yukon'),

    ('', '-----------'),

    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'),
    ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
    ('CT', 'Connecticut'), ('DE', 'Delaware'),
    ('DC', 'District of Columbia'), ('FL', 'Florida'),
    ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'),
    ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
    ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'),
    ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
    ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
    ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
    ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
    ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
    ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'), ('SD', 'South Dakota'),
    ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
    ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
    ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
)

FLAG_CHOICES = (
    ('1', 'Red'),
    ('2', 'Green'),
    ('3', 'Blue'),
    ('4', 'Orange'),
    ('5', 'Yellow'),
    ('6', 'Pink'),
    ('7', 'Pirate'),
    ('', '---')
)

EVENT_ROLES = (
    ('SA', 'Sales'),
    ('SP', 'Sponsorship'),
    ('PD', 'Conference Developer'),
    ('NA', 'Unassigned'),
)

PERSON_MASTER_RELATION_CHOICES = (
    (True, 'Filter'),
    (False, 'Start from scratch'),
)

FLAG_COLORS = {
    'red': '1',
    'green': '2',
    'blue': '3',
    'black': '4',
    'yellow': '5',
    'purple': '6'
}

AC_LOOKUP = {
    'AB': ('403', '587', '780', '825',),
    'AK': ('907',),
    'AL': ('205', '251', '256', '334', '659', '938',),
    'AR': ('327', '479', '501', '870',),
    'AZ': ('480', '520', '602', '623', '928',),
    'BC': ('236', '250', '604', '778',),
    'CA': ('209', '213', '310', '323', '408', '415', '424', '442', '510', '530',
           '559', '562', '619', '626', '628', '650', '657', '661', '669', '707',
           '714', '747', '760', '805', '818', '831', '858', '909', '916', '925',
           '949', '951',),
    'CO': ('303', '719', '720', '970',),
    'CT': ('203', '475', '860', '959',),
    'DC': ('202',),
    'DE': ('302',),
    'FL': ('239', '305', '321', '352', '386', '407', '561', '689', '727', '754',
           '772', '786', '813', '850', '863', '904', '941', '954',),
    'GA': ('229', '404', '470', '478', '678', '706', '762', '770', '912',),
    'HI': ('808',),
    'IA': ('319', '515', '563', '641', '712',),
    'ID': ('208', '986'),
    'IL': ('217', '224', '309', '312', '331', '447', '464', '618', '630', '708',
           '730', '773', '779', '815', '847', '872',),
    'IN': ('219', '260', '317', '463', '574', '765', '812', '930',),
    'KS': ('316', '620', '785', '913',),
    'KY': ('270', '364', '502', '606', '859',),
    'LA': ('225', '318', '337', '504', '985',),
    'MA': ('339', '351', '413', '508', '617', '774', '781', '857', '978',),
    'MB': ('204', '431',),
    'MD': ('227', '240', '301', '410', '443', '667',),
    'ME': ('207',),
    'MI': ('231', '248', '269', '313', '517', '586', '616', '679', '734', '810',
           '906', '947', '989',),
    'MN': ('218', '320', '507', '612', '651', '763', '952',),
    'MO': ('314', '417', '557', '573', '636', '660', '816', '975',),
    'MS': ('228', '601', '662', '769',),
    'MT': ('406',),
    'NB': ('506',),
    'NC': ('252', '336', '704', '743', '828', '910', '919', '980', '984',),
    'ND': ('701',),
    'NE': ('308', '402', '531',),
    'NH': ('603',),
    'NJ': ('201', '551', '609', '732', '848', '856', '862', '908', '973',),
    'NL': ('709',),
    'NM': ('505', '575',),
    'NS/PEI': ('782', '902',),
    'NV': ('702', '725', '775'),
    'NY': ('212', '315', '332', '347', '516', '518', '585', '607', '631', '646',
           '680', '716', '718', '845', '914', '917', '929', '934',),
    'OH': ('216', '220', '234', '283', '330', '380', '419', '440', '513', '567',
           '614', '740', '937',),
    'OK': ('405', '539', '580', '918',),
    'ON': ('226', '249', '289', '343', '365', '416', '437', '519', '548', '613',
           '647', '705', '807', '905',),
    'OR': ('458', '503', '541', '971',),
    'PA': ('215', '267', '272', '412', '484', '570', '610', '717', '724', '814',
           '878',),
    'QC': ('418', '438', '450', '514', '579', '581', '819', '873',),
    'RI': ('401',),
    'SC': ('803', '843', '854', '864',),
    'SD': ('605',),
    'SK': ('306', '639',),
    'TN': ('423', '615', '629', '731', '865', '901', '931',),
    'TX': ('210', '214', '254', '281', '325', '346', '361', '409', '430', '432',
           '469', '512', '682', '713', '737', '806', '817', '830', '832', '903',
           '915', '936', '940', '956', '972', '979',),
    'UT': ('385', '435', '801', ),
    'VA': ('276', '434', '540', '571', '703', '757', '804',),
    'VT': ('802',),
    'WA': ('206', '253', '360', '425', '509', '564',),
    'WI': ('262', '274', '414', '534', '608', '715', '920',),
    'WV': ('304', '681',),
    'WY': ('307',),
    'YK/NT/NU': ('867',),
}
