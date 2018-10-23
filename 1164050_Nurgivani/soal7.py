import shapefile #modul1
w=shapefile.Writer() #deklarasi, dalam kurung boleh dikosongkan boleh tidak sesuai type dan disini dikosongkan
w.shapeType #berfungsi menjalankan coding diatasnya
w.field("kolom1","C") #nama kolom
w.field("kolom2","C") #nama kolom
w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
w.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]],shapeType=shapefile.POLYLINE) #titik koordinat
w.save("soal7") #nama file


