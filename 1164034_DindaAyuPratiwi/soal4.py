import shapefile #modul1

w=shapefile.Writer(shapefile.POINTM) #deklarasi, dalam kurung boleh dikosongkan boleh tidak sesuai type dan disini menggunakan shapefile.POINTM
w.shapeType #berfungsi menjalankan coding diatasnya

w.field("kolom1","C") #nama kolom
w.field("kolom2","C") #nama kolom

w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
w.record("ngok","dua") #isi dari kolom 1 ngok, dan kolom 2 dua

w.point(1,1) #titik koordinat
w.point(2,2) #titik koordinat

w.save("soal4") #nama file