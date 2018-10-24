import shapefile #modul1

w=shapefile.Writer() #deklarasi, dalam kurung boleh dikosongkan boleh tidak sesuai type dan disini menggunakan shapeType 1
w.shapeType #berfungsi menjalankan coding diatasnya

w.field("Nama Bidang","Bidang ke ")  #nama kolom
w.field("Nama Bidang","Bidang ke")  #nama kolom

w.record("bujursangkar 1","satu")  #isi dari kolom 1 bujursangkar 1, dan kolom 2 satu
w.record("bujursangkar 2","dua")   #isi dari kolom 1 bujursangkar 2, dan kolom 2 dua
w.record("bujursangkar 3","tiga")  #isi dari kolom 1 bujursangkar 3, dan kolom 2 tiga

w.poly(parts=[[[2,2],[4,2],[4,4],[2,4],[2,2]]],shapeType=shapefile.POLYGON) #titik koordinat
w.poly(parts=[[[2,-2],[4,-2],[4,-4],[2,-4],[2,-2]]],shapeType=shapefile.POLYGON) #titik koordinat
w.poly(parts=[[[-2,2],[-4,2],[-4,4],[-2,4],[-2,2]]],shapeType=shapefile.POLYGON) #titik koordinat

w.save("soal10") #nama file