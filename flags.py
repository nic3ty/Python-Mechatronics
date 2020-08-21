from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White
Y = [0, 0, 255] #Blue

poland = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X ,X, X, X, X, X, X, X
]

sense.set_pixels(poland)
sleep(3)
france = [
X, X, X, O, O, Y, Y, Y,
X, X, X, O, O, Y, Y, Y,
X, X, X, O, O, Y, Y, Y,
X, X, X, O, O, Y, Y, Y,
X, X, X, O, O, Y, Y, Y,
X, X, X, O, O, Y, Y, Y,
X, X, X, O, O, Y, Y, Y,
X, X, X, O, O, Y, Y, Y
]

sense.set_pixels(france)

muse = [
O, X, O, O, O, O, X, O,
O, X, O, O, O, O, X, O,
O, X, O, O, O, O, X, O,
O, X, O, O, O, O, X, O,
O, O, X, O, O, X, O, O,
O, O, X, X, X, O, O, O,
O, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O
]
sleep(3)
sense.set_pixels(muse)

sense.show_message("Yaa yaa asa kara zenkai! Nee nee minna mo ne soukai? Yaa yaa nandemo dekisou da!? Omoitsuita koto ga aru kara Hayaku aitai na hanashitai na Machi kirenakute hayaoki da Asa no kuuki wa midori to shio no kaori Unto unto suikonde Sakamichi kakeashi aa dareka no senaka ga Tooku ni mieru yo ohayou! Te o agetara dasshu da kidzuiteru ne? Kyou wa donna hi kana (Donna hi da? DAY! DAY! DAY!) A~ zettai, genki zenkai DAY!! Nee kiite yo Tanoshiku natchaisouna aidia ga aru kara sa Houkago atsumatte yo (Kotowaru no nashi!) Imishin na koe de ma-ta-ne Yaa yaa asa kara zenkai! Nee nee minna mo ne soukai? Yaa yaa nandemo dekisou da!? Ohiru tabete nemuku natta kara Sukoshi me o tojita nenai yo nenai Yasumu dake dayo honno chotto ne Mado no soto no zawameki wa komori uta ...Nanda nanda okinakya Nobi~ shita ushiro de aa dareka ga yonderu Neguse o komakasu konchiwa! Terewarai de pinchi da kidzukareta ka? Nani kara hanasou ka (Nani kara hanasou?) Sono toki ni kimeyou Kyou wa donna hi kana (Donna hi da? DAY! DAY! DAY!) A~ zettai, genki zenkai DAY!! Nee kiite yo Tanoshiku natchaisouna aidia ga aru kara sa Houkago atsumatte yo (Kotowaru no nashi!) Imishin na koe de ma-ta-ne", scroll_speed=(0.040), text_colour=[255, 255, 0])