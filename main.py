import Telefons as tel 

samsung = tel.Telefons("samsung", "s23", "Februāris 17, 2023","440eur")
xiaomi  = tel.Telefons("xiaomi ", "poco x3", "24 Marts 2021","220")
iphone  = tel.Telefons("iphone  ", "15", "24 Marts 2021","1100")
nothing = tel.Telefons("nothing ", "2a", "12 Marts, 2024", "330")

samsung.printet()
xiaomi .printet()
iphone.printet()
nothing .printet()