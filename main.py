items = {'rifle':    (25, 3, 'в'),
         'gun':      (15, 2, 'п'),
         'ammo':     (15, 2, 'б'),
         'FA kit':   (20, 2, 'а'),
         'inhaler':  (5,  1, 'и'),
         'knife':    (15, 1, 'н'),
         'axe':      (15, 1, 'т'),
         'amulet':   (25, 1, 'о'),
         'bottle':   (15, 1, 'ф'),
         'antidote': (10, 1, 'д'),
         'food':     (20, 2, 'к'),
         'crossbow': (20, 2, 'р')
         }

values = [items[item][0] for item in items]
sizes = [items[item][1] for item in items]
names = [items[item][2] for item in items]

capacity = 9
initPoints = 10

print(values)