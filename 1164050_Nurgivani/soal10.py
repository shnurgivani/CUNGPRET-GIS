import shapefile #mengimport modul yang bernama shapefile 
w=shapefile.Writer() #mendeklarasikan variabel
w.shapeType #menjalankan ini deklarasi variabel
w.field("kolom1","C") #membuat kolom dengan nama kolom1 dengan type data karakter 
w.field("kolom2","C")

w.record("Seokjin","lima") # mengisi record ke dalam kolom yang sudah dibuat
w.record("Yoongi","dua") 
w.record("Taehyung","tiga") 
w.record("Jungkook","empat")
w.record("Namjoon","lima")

w.poly(parts=[[[1,2],[2,2], [2,1], [1,1], [1,2]]],shapeType=shapefile.POLYLINE) #membuat polylgone karena titik awal  sama dengan titik akhir
w.poly(parts=[[[1,6],[2,6], [2,4], [1,4], [1,6]]],shapeType=shapefile.POLYLINE) #membuat polylgone karena titik awal  sama dengan titik akhir
w.poly(parts=[[[1,-2],[2,-2], [2,-1], [1,-1], [1,-2]]],shapeType=shapefile.POLYLINE) #membuat polylgone karena titik awal  sama dengan titik akhir
w.poly(parts=[[[1,-6],[2,-6], [2,-4],[1,-4], [1,-6]]],shapeType=shapefile.POLYLINE) #membuat polylgone karena titik awal  sama dengan titik akhir
w.poly(parts=[[[1,-7],[2,-7], [2,-8],[1,-8], [1,-7]]],shapeType=shapefile.POLYLINE) #membuat polylgone karena titik awal  sama dengan titik akhir

w.save("soal10") #nama file yang disimpan