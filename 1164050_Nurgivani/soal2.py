import shapefile #modul
w=shapefile.Writer(shapeType=1) #deklarasi, dalam kurung boleh dikosongkan boleh tidak sesuai type, dan di sini menggunakan shapetype=1
w.shapeType #berfungsi menjalankan coding diatasnya
w.field("kolom1","C") #nama kolom
w.field("kolom2","C") #nama kolom
w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
w.record("ngok","dua") #isi dari kolom 1 ngok, dan kolom 2 dua
w.point(1,1) #titik koordinat
w.point(2,2) #titik koordinat
w.save("soal2") #nama file