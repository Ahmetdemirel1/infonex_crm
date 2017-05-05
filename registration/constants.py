"""Constants for use in other modules"""

PAYMENT_METHODS = (('V', 'Visa'),
                   ('M', 'MasterCard'),
                   ('A', 'AMEX'),
                   ('C', 'Cheque'),
                   ('W', 'Wire Transfer'),
                   ('N', 'Credit Note'),
                   ('O', 'Other method'))

REG_STATUS_OPTIONS = (('', '-----------'),
                      ('DU', 'Delegate Unpaid'),
                      ('DP', 'Delegate Paid'),
                      ('DF', 'Delegate Free'),
                      ('K', 'Speaker'),
                      ('SP', 'Sponsor Paid'),
                      ('SU', 'Sponsor Unpaid'),
                      ('SD', 'Sponsor Delegate'),
                      ('SE', 'Sponsor Exhibitor'),
                      ('G', 'Guest'),
                      ('DX', 'Delegate cancelled - paid'),
                      ('UX', 'Delegate cancelled - unpaid'),
                      ('SX', 'Sponsor cancelled'),
                      ('KX', 'Speaker cancelled'),
                      ('B', 'Substituted Out'))

CONTACT_OPTIONS = (('D', 'Attention: delegate'),
                   ('A', 'Attention: assistant'),
                   ('C', 'cc to Assistant'))

ADMIN_REPORTS = (('Delegate', 'Delegate List'),
                 ('NoName', 'No-Name Delegate List'),
                 ('Registration', 'Registration List'),
                 ('Phone', 'Phone/Email List'),
                 ('Onsite', 'Onsite Delegate List'),
                 ('Unpaid', 'Unpaid Delegate List'),
                 ('CE', 'CE Sign-in Sheet'),
                 ('Badges', 'Badges'),
                 ('Counts', 'Registration Counts'),
                 ('Speaker', 'Speaker List'),)
