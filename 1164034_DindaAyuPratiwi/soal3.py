import shapefile #modul1

w=shapefile.Writer(shapeType=1) #deklarasi, dalam kurung boleh dikosongkan boleh tidak sesuai type dan disini menggunakan shapeType 1
w.shapeType #berfungsi menjalankan coding diatasnya
w.shapeType=3
w.shapeType

w.field("kolom1","C") #nama kolom
w.field("kolom2","C") #nama kolom

w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
w.record("ngok","dua") #isi dari kolom 1 ngok, dan kolom 2 dua

w.point(1,1) #titik koordinat
w.point(2,2) #titik koordinat

w.save("soal3") #nama file