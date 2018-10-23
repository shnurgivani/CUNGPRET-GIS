import shapefile #modul1
w=shapefile.Writer() #deklarasi, dalam kurung boleh dikosongkan boleh tidak sesuai type dan disini dikosongkan
w.shapeType #berfungsi menjalankan coding diatasnya
w.field("kolom1","C") #nama kolom
w.field("kolom2","C") #nama kolom
w.record("ngek","satu")  #isi dari kolom 1 ngek, dan kolom 2 satu
w.record("crot","dua")  #isi dari kolom 1 crot, dan kolom 2 dua
w.poly(parts=[[[1,3],[5,3], [5,2],[1,2],
[1,3]]],shapeType=shapefile.POLYLINE) #titik koordinat
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9],
[1,6]]],shapeType=shapefile.POLYLINE) #titik koordinat
w.save("soal9") #nama file